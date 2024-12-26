/*
 * This file is part of PCAPdroid.
 *
 * PCAPdroid is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * PCAPdroid is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with PCAPdroid.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Copyright 2020-21 - Emanuele Faranda
 */

package com.emanuelef.remote_capture;

import android.content.Context;
import android.util.SparseArray;
import android.util.SparseIntArray;

import androidx.annotation.Nullable;
import androidx.collection.ArraySet;

import com.emanuelef.remote_capture.interfaces.ConnectionsListener;
import com.emanuelef.remote_capture.model.AppDescriptor;
import com.emanuelef.remote_capture.model.AppStats;
import com.emanuelef.remote_capture.model.ConnectionDescriptor;
import com.emanuelef.remote_capture.model.ConnectionUpdate;

import java.net.InetAddress;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Set;

/* A container for the connections. This is used to store active/closed connections until the capture
 * is stopped. Active connections are also kept in the native side.
 *
 * The ConnectionsRegister can store up to _size items, after which rollover occurs and older
 * connections are replaced with the new ones. Via the addListener method it's possible to listen
 * for connections changes (connections added/removed/updated). The usual listener for such events
 * is the ConnectionsFragment, which then forwards them to the ConnectionsAdapter.
 *
 * Connections are added/updated by the CaptureService in a separate thread. The getter methods are
 * instead called on the UI thread, usually by the ConnectionsAdapter. Methods are synchronized to
 * provide threads safety on this class. Concurrent access to the ConnectionDescriptors fields can
 * occur during connectionsUpdates but it's not protected, check out the ConnectionDescriptor class
 * for more details.
 */
public class ConnectionsRegister {
    private static final String TAG = "ConnectionsRegister";

    private final ArrayList<ConnectionDescriptor> mItems;
    private final int mMaxSize;  // Maximum size before cleanup
    private int mUntrackedItems; // number of old connections which were discarded due to cleanup
    private int mNumMalicious;
    private int mNumBlocked;
    private long mLastFirewallBlock;
    private final SparseArray<AppStats> mAppsStats;
    private final SparseIntArray mConnsByIface;
    private final ArrayList<ConnectionsListener> mListeners;
    private final Geolocation mGeo;
    private final AppsResolver mAppsResolver;

    public ConnectionsRegister(Context ctx, int maxSize) {
        mUntrackedItems = 0;
        mMaxSize = maxSize;
        mGeo = new Geolocation(ctx);
        mItems = new ArrayList<>();
        mListeners = new ArrayList<>();
        mAppsStats = new SparseArray<>(); // uid -> AppStats
        mConnsByIface = new SparseIntArray();
        mAppsResolver = new AppsResolver(ctx);
    }

    // returns the oldest connection
    private synchronized ConnectionDescriptor getOldestConnection() {
        return mItems.isEmpty() ? null : mItems.get(0);
    }

    // returns the newest connection
    private synchronized ConnectionDescriptor getNewestConnection() {
        return mItems.isEmpty() ? null : mItems.get(mItems.size() - 1);
    }

    private void processConnectionStatus(ConnectionDescriptor conn, AppStats stats) {
        boolean is_blacklisted = conn.isBlacklisted();

        if(!conn.alerted && is_blacklisted) {
            CaptureService.requireInstance().notifyBlacklistedConnection(conn);
            conn.alerted = true;
            mNumMalicious++;
        } else if(conn.alerted && !is_blacklisted) {
            // the connection was whitelisted
            conn.alerted = false;
            mNumMalicious--;
        }

        if(!conn.block_accounted && conn.is_blocked) {
            mNumBlocked++;
            stats.numBlockedConnections++;
            conn.block_accounted = true;
        } else if(conn.block_accounted && !conn.is_blocked) {
            mNumBlocked--;
            stats.numBlockedConnections--;
            conn.block_accounted = false;
        }

        if(conn.is_blocked)
            mLastFirewallBlock = Math.max(conn.last_seen, mLastFirewallBlock);
    }

    // called by the CaptureService in a separate thread when new connections should be added to the register
    public synchronized void newConnections(ConnectionDescriptor[] conns) {
        if(conns.length > mMaxSize) {
            // take the most recent connections if we exceed max size
            mUntrackedItems += conns.length - mMaxSize;
            conns = Arrays.copyOfRange(conns, conns.length - mMaxSize, conns.length);
        }

        // Calculate how many items we need to remove to stay under maxSize
        int totalSize = mItems.size() + conns.length;
        int itemsToRemove = Math.max(0, totalSize - mMaxSize);
        ConnectionDescriptor[] removedItems = null;

        // Remove old connections if needed
        if(itemsToRemove > 0) {
            removedItems = new ConnectionDescriptor[itemsToRemove];
            for(int i = 0; i < itemsToRemove; i++) {
                ConnectionDescriptor conn = mItems.remove(0);
                removedItems[i] = conn;

                if(conn != null) {
                    if(conn.ifidx > 0) {
                        int num_conn = mConnsByIface.get(conn.ifidx);
                        if(--num_conn <= 0)
                            mConnsByIface.delete(conn.ifidx);
                        else
                            mConnsByIface.put(conn.ifidx, num_conn);
                    }
                    if(conn.isBlacklisted())
                        mNumMalicious--;
                }
            }
            mUntrackedItems += itemsToRemove;
        }

        int insertPos = mItems.size();

        // Add new connections
        for(ConnectionDescriptor conn: conns) {

            // update the apps stats
            int uid = conn.uid;
            AppStats stats = getAppsStatsOrCreate(uid);

            if(conn.ifidx > 0) {
                int num_conn = mConnsByIface.get(conn.ifidx);
                mConnsByIface.put(conn.ifidx, num_conn + 1);
            }

            // Geolocation
            InetAddress dstAddr = conn.getDstAddr();
            conn.country = mGeo.getCountryCode(dstAddr);
            conn.asn = mGeo.getASN(dstAddr);

            AppDescriptor app = mAppsResolver.getAppByUid(conn.uid, 0);
            if(app != null)
                conn.encrypted_payload = Utils.hasEncryptedPayload(app, conn);

            processConnectionStatus(conn, stats);

            stats.numConnections++;
            stats.rcvdBytes += conn.rcvd_bytes;
            stats.sentBytes += conn.sent_bytes;

            // Add to ArrayList
            mItems.add(conn);
        }

        for(ConnectionsListener listener: mListeners) {
            if(removedItems != null && removedItems.length > 0)
                listener.connectionsRemoved(0, removedItems);

            if(conns.length > 0)
                listener.connectionsAdded(insertPos, conns);
        }
    }

    // called by the CaptureService in a separate thread when connections should be updated
    public synchronized void connectionsUpdates(ConnectionUpdate[] updates) {
        if(mItems.isEmpty())
            return;

        int first_id = mItems.get(0).incr_id;
        int last_id = mItems.get(mItems.size() - 1).incr_id;
        int []changed_pos = new int[updates.length];
        int k = 0;

        Log.d(TAG, "connectionsUpdates: items=" + mItems.size() + ", first_id=" + first_id + ", last_id=" + last_id);

        for(ConnectionUpdate update: updates) {
            int id = update.incr_id;

            // Find the connection with matching ID
            for(int i = 0; i < mItems.size(); i++) {
                ConnectionDescriptor conn = mItems.get(i);
                if(conn.incr_id == id) {
                    // update the app stats
                    AppStats stats = getAppsStatsOrCreate(conn.uid);
                    stats.sentBytes += update.sent_bytes - conn.sent_bytes;
                    stats.rcvdBytes += update.rcvd_bytes - conn.rcvd_bytes;

                    //Log.d(TAG, "update " + update.incr_id + " -> " + update.update_type);
                    conn.processUpdate(update);
                    processConnectionStatus(conn, stats);

                    changed_pos[k++] = i;
                    break;
                }
            }
        }

        if(k == 0)
            // no updates for tracked items
            return;

        if(k != updates.length)
            // some untracked items were skipped, shrink the array
            changed_pos = Arrays.copyOf(changed_pos, k);

        for(ConnectionsListener listener: mListeners)
            listener.connectionsUpdated(changed_pos);
    }

    public synchronized void reset() {
        mItems.clear();
        mUntrackedItems = 0;
        mNumMalicious = 0;
        mNumBlocked = 0;
        mLastFirewallBlock = 0;
        mAppsStats.clear();
        mConnsByIface.clear();

        for(ConnectionsListener listener: mListeners)
            listener.connectionsChanges(0);
    }

    public synchronized void addListener(ConnectionsListener listener) {
        mListeners.add(listener);

        // Send the first update to sync it
        listener.connectionsChanges(mItems.size());

        Log.d(TAG, "(add) new connections listeners size: " + mListeners.size());
    }

    public synchronized void removeListener(ConnectionsListener listener) {
        mListeners.remove(listener);

        Log.d(TAG, "(remove) new connections listeners size: " + mListeners.size());
    }

    public int getConnCount() {
        return mItems.size();
    }

    public int getUntrackedConnCount() {
        return mUntrackedItems;
    }

    // get the i-th oldest connection
    public synchronized @Nullable ConnectionDescriptor getConn(int i) {
        if((i < 0) || (i >= mItems.size()))
            return null;
        return mItems.get(i);
    }

    public synchronized int getConnPositionById(int incr_id) {
        if(mItems.isEmpty())
            return -1;

        for(int i = 0; i < mItems.size(); i++) {
            if(mItems.get(i).incr_id == incr_id)
                return i;
        }
        return -1;
    }

    public synchronized @Nullable ConnectionDescriptor getConnById(int incr_id) {
        int pos = getConnPositionById(incr_id);
        if(pos < 0)
            return null;

        return getConn(pos);
    }

    public synchronized AppStats getAppStats(int uid) {
        return mAppsStats.get(uid);
    }

    public synchronized List<AppStats> getAppsStats() {
        ArrayList<AppStats> rv = new ArrayList<>(mAppsStats.size());

        for(int i=0; i<mAppsStats.size(); i++) {
            // Create a clone to avoid concurrency issues
            AppStats stats = mAppsStats.valueAt(i).clone();

            rv.add(stats);
        }

        return rv;
    }

    private synchronized AppStats getAppsStatsOrCreate(int uid) {
        AppStats stats = mAppsStats.get(uid);
        if(stats == null) {
            stats = new AppStats(uid);
            mAppsStats.put(uid, stats);
        }

        return stats;
    }

    public synchronized void resetAppsStats() {
        mAppsStats.clear();
    }

    public synchronized Set<Integer> getSeenUids() {
        ArraySet<Integer> rv = new ArraySet<>();

        for(int i=0; i<mAppsStats.size(); i++)
            rv.add(mAppsStats.keyAt(i));

        return rv;
    }

    public int getNumMaliciousConnections() {
        return mNumMalicious;
    }

    public int getNumBlockedConnections() {
        return mNumBlocked;
    }

    public long getLastFirewallBlock() {
        return mLastFirewallBlock;
    }

    public synchronized boolean hasSeenMultipleInterfaces() {
        return(mConnsByIface.size() > 1);
    }

    // Returns a sorted list of seen network interfaces
    public synchronized List<String> getSeenInterfaces() {
        List<String> rv = new ArrayList<>();

        for(int i=0; i<mConnsByIface.size(); i++) {
            int ifidx = mConnsByIface.keyAt(i);
            String ifname = CaptureService.getInterfaceName(ifidx);

            if(!ifname.isEmpty())
                rv.add(ifname);
        }

        Collections.sort(rv);
        return rv;
    }

    public synchronized void releasePayloadMemory() {
        Log.i(TAG, "releaseFullPayloadMemory called");

        for(ConnectionDescriptor conn: mItems) {
            conn.clearPayload();
        }
    }
}
