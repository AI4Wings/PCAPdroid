package com.emanuelef.remote_capture.pcap_dump;

import android.content.Context;
import android.net.Uri;

import com.emanuelef.remote_capture.CaptureService;
import com.emanuelef.remote_capture.Log;
import com.emanuelef.remote_capture.Utils;
import com.emanuelef.remote_capture.interfaces.PcapDumper;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.IOException;
import java.io.OutputStream;
import java.nio.charset.StandardCharsets;

public class FileDumper implements PcapDumper {
    public static final String TAG = "FileDumper";
    private final Context mContext;
    private final Uri mPcapUri;
    private final Uri mJsonUri;
    private boolean mSendHeader;
    private OutputStream mOutputStream;

    public FileDumper(Context ctx, Uri pcap_uri) {
        mContext = ctx;
        mPcapUri = pcap_uri;
        mJsonUri = Uri.parse(pcap_uri.toString().replaceFirst("\\.pcap$", "_device_info.json"));
        mSendHeader = true;
    }

    private void writeDeviceInfo() throws IOException {
        try {
            JSONObject deviceInfo = new JSONObject();
            deviceInfo.put("device_name", Utils.getDeviceName(mContext));
            deviceInfo.put("device_model", Utils.getDeviceModel());
            deviceInfo.put("os_version", Utils.getOsVersion());
            deviceInfo.put("build_info", Utils.getBuildInfo(mContext));
            deviceInfo.put("app_version", Utils.getAppVersionString(mContext));
            deviceInfo.put("capture_time", System.currentTimeMillis());

            OutputStream jsonOut = mContext.getContentResolver().openOutputStream(mJsonUri, "rwt");
            jsonOut.write(deviceInfo.toString(2).getBytes(StandardCharsets.UTF_8));
            jsonOut.close();
        } catch (JSONException e) {
            throw new IOException("Failed to create device info JSON: " + e.getMessage());
        }
    }

    @Override
    public void startDumper() throws IOException {
        Log.d(TAG, "PCAP URI: " + mPcapUri);
        mOutputStream = mContext.getContentResolver().openOutputStream(mPcapUri, "rwt");
        writeDeviceInfo();
    }

    @Override
    public void stopDumper() throws IOException {
        mOutputStream.close();
    }

    @Override
    public String getBpf() {
        return "";
    }

    @Override
    public void dumpData(byte[] data) throws IOException {
        if(mSendHeader) {
            mSendHeader = false;
            mOutputStream.write(CaptureService.getPcapHeader());
        }

        mOutputStream.write(data);
    }
}
