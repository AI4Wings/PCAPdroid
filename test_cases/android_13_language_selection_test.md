# Android 13+ Language Selection Test Cases

## Prerequisites
- Android device running Android 13 (API 33) or higher
- PCAPdroid app installed
- Clean app data state

## Test Case 1: Verify Language Preference UI Elements
### Steps
1. Launch PCAPdroid app
2. Navigate to Settings
3. Scroll to language settings section

### Expected Results
- "app_language" dropdown should be hidden (appLang.setVisible(false))
- "app_language_external" preference should be visible (appLangExternal.setVisible(true))
- If no language selected, summary should show "System default" (R.string.system_default)
- If language selected, summary should show language name in its native form

### Code Path
```java
// SettingsActivity.java:361-405
if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.TIRAMISU) {
    appLang.setVisible(false);
    appLangExternal.setVisible(true);
    
    LocaleList locales = requireContext().getSystemService(LocaleManager.class)
            .getApplicationLocales();
    if (locales.equals(LocaleList.getEmptyLocaleList()))
        appLangExternal.setSummary(getString(R.string.system_default));
    else if (!locales.isEmpty())
        appLangExternal.setSummary(locales.get(0).getDisplayName());
}
```

## Test Case 2: System Language Picker Integration
### Steps
1. Launch PCAPdroid app
2. Navigate to Settings
3. Click on language preference
4. Change language in system picker

### Expected Results
- Clicking preference should open system language settings (Settings.ACTION_APP_LOCALE_SETTINGS)
- System settings should show PCAPdroid package
- Selected language should be applied to app
- Returning to PCAPdroid settings should show selected language name

### Code Path
```java
// SettingsActivity.java:377-382
appLangExternal.setOnPreferenceClickListener(preference -> {
    Intent intent = new Intent(Settings.ACTION_APP_LOCALE_SETTINGS);
    intent.setData(Uri.fromParts("package", requireContext().getPackageName(), null));
    startActivity(intent);
    return true;
});
```

## Test Case 3: Configuration Changes
### Steps
1. Launch PCAPdroid app
2. Change system language for app
3. Verify configuration changes

### Expected Results
- App should use system-selected language
- Configuration should be obtained through getLocalizedConfig()
- No manual locale setting should occur on Android 13+

### Code Path
```java
// Utils.java:343-368
public static Configuration getLocalizedConfig(Context context) {
    // On Android 33+, app language is configured from the system settings
    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.TIRAMISU) {
        if (Prefs.useEnglishLanguage(prefs)) {
            Log.i(TAG, "Migrate from in-app language picker to system picker");
            prefs.edit().remove(Prefs.PREF_APP_LANGUAGE).apply();

            context.getSystemService(LocaleManager.class)
                    .setApplicationLocales(new LocaleList(Locale.forLanguageTag("en-US")));
        }
        return config;
    }
}
```

## Test Case 4: Default Locale Handling
### Steps
1. Clear app data
2. Launch PCAPdroid app
3. Check initial language state

### Expected Results
- App should use system default locale
- No explicit locale setting should occur unless previously configured
- LocaleList should be empty (LocaleList.getEmptyLocaleList())

## Test Case 5: Edge Cases
### Steps
1. Test with unsupported language
2. Test with multiple language changes
3. Test with app in background during language change

### Expected Results
- App should handle unsupported languages gracefully
- Multiple language changes should be applied correctly
- Background app should reflect language changes on resume

## Test Environment Requirements
1. Android 13+ device
2. Multiple language packs installed
3. Clean app state for initial tests
4. Various device configurations (screen size, density)

## Test Data Requirements
1. Supported languages list
2. Unsupported languages list
3. RTL language options
4. Multi-locale configurations

## Notes
- These tests focus on Android 13+ specific behavior
- UI verification is critical for language display
- System integration testing is essential
- Migration from older versions tested separately
