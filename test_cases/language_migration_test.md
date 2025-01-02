# Language Selection Migration Test Cases

## Prerequisites
- Android 13+ (API 33) device
- Previous version of PCAPdroid with in-app language selection
- New version of PCAPdroid with system language integration
- Clean app data state for initial installation

## Test Case 1: English Language Migration
### Steps
1. Install previous version of PCAPdroid
2. Set language to English using in-app picker
3. Verify English is applied
4. Update to new version (Android 13+ compatible)
5. Open app settings

### Expected Results
- Previous English preference should be detected
- Migration log message should appear: "Migrate from in-app language picker to system picker"
- PREF_APP_LANGUAGE should be removed from SharedPreferences
- System LocaleManager should show "en-US" in application locales

### Code Path
```java
// Utils.java:343-368
if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.TIRAMISU) {
    if (Prefs.useEnglishLanguage(prefs)) {
        Log.i(TAG, "Migrate from in-app language picker to system picker");
        prefs.edit().remove(Prefs.PREF_APP_LANGUAGE).apply();

        context.getSystemService(LocaleManager.class)
                .setApplicationLocales(new LocaleList(Locale.forLanguageTag("en-US")));
    }
    return config;
}
```

## Test Case 2: Non-English Language Migration
### Steps
1. Install previous version of PCAPdroid
2. Set language to non-English option using in-app picker
3. Verify selected language is applied
4. Update to new version (Android 13+ compatible)
5. Open app settings

### Expected Results
- Non-English preference should be preserved
- App should use system language settings
- Previous in-app language preference should be cleared
- UI should reflect system language selection

## Test Case 3: Default Language Migration
### Steps
1. Install previous version of PCAPdroid
2. Leave language as system default
3. Update to new version (Android 13+ compatible)
4. Check language settings

### Expected Results
- No migration should occur (no existing preference)
- System default language should be used
- LocaleList should be empty
- UI should show "System default"

## Test Case 4: Migration Edge Cases
### Steps
1. Test interrupted update process
2. Test with corrupted preferences
3. Test with multiple language changes before update
4. Test with app in use during update

### Expected Results
- Migration should be resilient to interruptions
- Corrupted preferences should be handled gracefully
- Final language state should be consistent
- User experience should remain smooth

## Test Environment Requirements
1. Android 13+ device
2. Access to previous app version
3. Multiple language packs installed
4. Various device configurations:
   - Different Android 13+ versions
   - Different system languages
   - Different update scenarios

## Test Data Requirements
1. Previous version with English preference
2. Previous version with non-English preference
3. Previous version with default language
4. Corrupted preference scenarios

## Notes
- Migration is one-way process
- Only occurs on Android 13+ devices
- English preference has special migration path
- System language integration is permanent after migration
