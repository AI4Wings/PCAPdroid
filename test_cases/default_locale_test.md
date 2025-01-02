# Default Locale Handling Test Cases

## Prerequisites
- Clean device state
- No previous PCAPdroid installation
- Android device (any supported version)

## Test Case 1: Fresh Installation Default Locale
### Steps
1. Ensure no previous PCAPdroid installation exists
2. Clear any residual app data if necessary
3. Install PCAPdroid
4. Launch application

### Expected Results
- Default locale should be "en-US" as specified in resources.properties
- All UI elements should display in English
- No explicit locale configuration should be present in preferences

### Code Path
```java
// resources.properties
unqualifiedResLocale=en-US

// Utils.java:343-368
public static Configuration getLocalizedConfig(Context context) {
    Configuration config = context.getResources().getConfiguration();
    SharedPreferences prefs = PreferenceManager.getDefaultSharedPreferences(context);
    
    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.TIRAMISU) {
        // Android 13+ specific handling
        return config;
    } else {
        String lang = prefs.getString(Prefs.PREF_APP_LANGUAGE, "");
        if(lang.isEmpty()) {
            // Default locale handling - will use en-US from resources.properties
            return config;
        }
    }
}
```

## Test Case 2: UI Language Verification
### Steps
1. Launch fresh installation
2. Navigate through all main UI screens:
   - Main activity
   - Settings
   - Connection details
   - Capture controls
   - Status fragments

### Expected Results
- All UI elements should display in English
- No untranslated strings should appear
- Text alignment should be correct (LTR)
- All system dialogs should use English

## Test Case 3: System Language Override Test
### Steps
1. Set system language to non-English
2. Install PCAPdroid fresh
3. Launch application
4. Check language display

### Expected Results
- App should still use English by default
- resources.properties setting should take precedence
- No language preference should be set in app settings

## Test Case 4: Configuration Change Handling
### Steps
1. Fresh install PCAPdroid
2. Rotate device
3. Put app in background
4. Change system configuration
5. Return to app

### Expected Results
- English locale should persist
- UI should remain in English
- No unexpected language changes

## Test Environment Requirements
1. Clean device state
2. Multiple test devices with different:
   - Android versions
   - System languages
   - Screen configurations

## Test Data Requirements
1. Fresh installation APK
2. List of UI screens to verify
3. System configuration changes to test

## Notes
- Default locale is controlled by resources.properties
- No user interaction required for default locale
- Behavior consistent across Android versions
- Important for first-launch experience
