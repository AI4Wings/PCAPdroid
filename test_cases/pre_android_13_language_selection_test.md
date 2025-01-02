# Pre-Android 13 Language Selection Test Cases

## Prerequisites
- Android device running Android 12 (API 32) or lower
- PCAPdroid app installed
- Clean app data state

## Test Case 1: Verify Language Preference UI Elements
### Steps
1. Launch PCAPdroid app
2. Navigate to Settings
3. Scroll to language settings section

### Expected Results
- "app_language" dropdown should be visible (appLang.setVisible(true))
- "app_language_external" preference should be hidden (appLangExternal.setVisible(false))
- Dropdown should show currently selected language
- Available language options should be displayed correctly

### Code Path
```java
// SettingsActivity.java:361-405
if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.TIRAMISU) {
    // Android 13+ specific code
} else {
    appLang.setVisible(true);
    appLangExternal.setVisible(false);
    
    String[] langValues = getResources().getStringArray(R.array.pref_app_language_values);
    String[] langNames = getResources().getStringArray(R.array.pref_app_language_names);
    appLang.setEntries(langNames);
    appLang.setEntryValues(langValues);
}
```

## Test Case 2: Language Selection and Application
### Steps
1. Launch PCAPdroid app
2. Navigate to Settings
3. Open language dropdown
4. Select different language
5. Confirm restart dialog
6. Wait for app restart

### Expected Results
- Language options should be displayed in native names
- Selection should trigger app restart dialog
- App should restart automatically
- New language should be applied after restart
- Language preference should persist across restarts

### Code Path
```java
// Utils.java:343-368
public static Configuration getLocalizedConfig(Context context) {
    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.TIRAMISU) {
        // Android 13+ specific code
    } else {
        SharedPreferences prefs = PreferenceManager.getDefaultSharedPreferences(context);
        Configuration config = context.getResources().getConfiguration();
        String lang = prefs.getString(Prefs.PREF_APP_LANGUAGE, "");
        
        if(!lang.isEmpty()) {
            Locale locale = Locale.forLanguageTag(lang);
            config.setLocale(locale);
        }
        return config;
    }
}
```

## Test Case 3: Default Language Handling
### Steps
1. Clear app data
2. Launch PCAPdroid app
3. Check initial language state

### Expected Results
- App should use system default locale if no language selected
- Language dropdown should show "System default"
- UI should reflect system language

## Test Case 4: Language Change Persistence
### Steps
1. Select specific language
2. Force stop app
3. Relaunch app
4. Navigate to different activities
5. Restart device
6. Check app language

### Expected Results
- Selected language should persist across:
  - App force stops
  - Activity transitions
  - Device restarts
- All UI elements should maintain selected language

## Test Case 5: Edge Cases
### Steps
1. Test rapid language changes
2. Test with unsupported system locale
3. Test during background operations
4. Test with missing language resources

### Expected Results
- App should handle rapid changes gracefully
- Unsupported locales should fall back to default
- Background operations should complete normally
- Missing resources should use default language strings

## Test Environment Requirements
1. Android 12 or lower device
2. Multiple language packs installed
3. Clean app state for initial tests
4. Various device configurations:
   - Different Android versions (7-12)
   - Different screen sizes
   - Different system languages

## Test Data Requirements
1. List of supported languages
2. RTL language options
3. Languages with missing translations
4. System locales not in app's language list

## Notes
- These tests focus on pre-Android 13 behavior
- In-app language selection is primary mechanism
- No system settings integration required
- Configuration changes handled through Utils.getLocalizedConfig
