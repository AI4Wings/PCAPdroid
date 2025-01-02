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
 * Copyright 2020-24 - Emanuele Faranda
 */

package com.emanuelef.remote_capture.activities;

import android.os.Bundle;
import android.widget.TextView;

import com.emanuelef.remote_capture.R;
import com.emanuelef.remote_capture.Utils;

public class DeviceInfoActivity extends BaseActivity {
    private static final String TAG = "DeviceInfoActivity";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setTitle(R.string.device_info);
        setContentView(R.layout.device_info_activity);
        displayBackAction();

        // Collect device information
        String deviceName = Utils.getDeviceName(this);
        String deviceModel = Utils.getDeviceModel();
        String osVersion = Utils.getOsVersion();
        String buildInfo = Utils.getBuildInfo(this);

        // Display device information
        TextView deviceNameView = findViewById(R.id.device_name);
        TextView deviceModelView = findViewById(R.id.device_model);
        TextView osVersionView = findViewById(R.id.os_version);
        TextView buildInfoView = findViewById(R.id.build_info);

        if (deviceName != null)
            deviceNameView.setText(getString(R.string.device_name_format, deviceName));
        deviceModelView.setText(getString(R.string.device_model_format, deviceModel));
        osVersionView.setText(getString(R.string.os_version_format, osVersion));
        buildInfoView.setText(buildInfo);
    }
}
