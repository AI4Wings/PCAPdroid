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
 * Copyright 2020-22 - Emanuele Faranda
 */

package com.emanuelef.remote_capture;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;

public class Log {
    public static final int LOG_LEVEL_INFO = 4;
    public static int DEFAULT_LOGGER;
    public static int MITMADDON_LOGGER;

    public static void init(String basedir) {
        DEFAULT_LOGGER = CaptureService.initLogger(basedir + "/pcapdroid.log", LOG_LEVEL_INFO);
        MITMADDON_LOGGER = CaptureService.initLogger(basedir + "/mitmaddon.log", LOG_LEVEL_INFO);
        android.util.Log.e("tag", basedir);
    }

    public static void writeLog(int logger, int level, @Nullable String tag, @NonNull String message) {
        CaptureService.writeLog(logger, level, "[" + tag + "] " + message);
    }

    public static void d(@Nullable String tag, @NonNull String message) {
        android.util.Log.d(tag, message);
    }

    public static void i(@Nullable String tag, @NonNull String message) {
        android.util.Log.i(tag, message);
        writeLog(DEFAULT_LOGGER, android.util.Log.INFO, tag, message);
    }

    public static void w(@Nullable String tag, @NonNull String message) {
        android.util.Log.w(tag, message);
        writeLog(DEFAULT_LOGGER, android.util.Log.WARN, tag, message);
    }

    public static void e(@Nullable String tag, @NonNull String message) {
        android.util.Log.e(tag, message);
        writeLog(DEFAULT_LOGGER, android.util.Log.ERROR, tag, message);
    }

    public static void wtf(@Nullable String tag, @NonNull String message) {
        android.util.Log.wtf(tag, message);
        writeLog(DEFAULT_LOGGER, android.util.Log.ASSERT, tag, message); // ANDROID_LOG_FATAL
    }
}