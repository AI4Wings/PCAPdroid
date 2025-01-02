# PCAPdroid Device Information Feature Test Cases

## 1. Device Information Page UI Tests

### 1.1 Navigation and Access (DI-NAV)
| ID | Test Case | Description | Steps | Expected Result |
|----|-----------|-------------|--------|-----------------|
| DI-NAV-001 | Access from Main Menu | Verify device info page access | 1. Open PCAPdroid app<br>2. Navigate to main menu<br>3. Select device info option | Device info page opens successfully |
| DI-NAV-002 | State Preservation | Check page state preservation | 1. Open device info page<br>2. Scroll through content<br>3. Navigate away<br>4. Return to page | Page state and scroll position preserved |
| DI-NAV-003 | Back Navigation | Test back button functionality | 1. Open device info page<br>2. Press back button | Returns to previous screen |

### 1.2 Display and Layout (DI-DISP)
| ID | Test Case | Description | Steps | Expected Result |
|----|-----------|-------------|--------|-----------------|
| DI-DISP-001 | Basic Information Display | Verify core device info display | 1. Open device info page | Shows device name, manufacturer, Android version |
| DI-DISP-002 | Layout Responsiveness | Test layout on different screen sizes | 1. View on different devices/orientations | Layout adapts properly |
| DI-DISP-003 | Scroll Behavior | Verify scrolling with large content | 1. Scroll through all information | Smooth scrolling, all content accessible |
| DI-DISP-004 | Text Scaling | Test with different text sizes | 1. Change system text size<br>2. View device info page | Text scales appropriately |
| DI-DISP-005 | Dark Mode | Verify dark mode compatibility | 1. Enable system dark mode<br>2. View device info page | Colors adjust correctly |

### 1.3 Information Accuracy (DI-ACC)
| ID | Test Case | Description | Steps | Expected Result |
|----|-----------|-------------|--------|-----------------|
| DI-ACC-001 | Device Name | Verify device name accuracy | 1. Compare with Settings app | Matches system device name |
| DI-ACC-002 | Manufacturer Info | Check manufacturer details | 1. Compare with Settings app | Matches system manufacturer info |
| DI-ACC-003 | Android Version | Verify OS version display | 1. Compare with Settings app | Matches system Android version |
| DI-ACC-004 | Hardware Info | Validate hardware details | 1. Compare with Settings app | Matches system hardware info |
| DI-ACC-005 | Real-time Updates | Check info updates | 1. Change device settings<br>2. Refresh page | Information updates accordingly |

## 2. PCAP JSON File Generation Tests

### 2.1 File Generation (PJ-GEN)
| ID | Test Case | Description | Steps | Expected Result |
|----|-----------|-------------|--------|-----------------|
| PJ-GEN-001 | Basic Generation | Test basic JSON file creation | 1. Start packet capture<br>2. Save PCAP file | Device info JSON created with "_device_info.json" suffix |
| PJ-GEN-002 | Multiple Files | Test multiple file saves | 1. Save multiple PCAP files | Separate JSON files created for each PCAP |
| PJ-GEN-003 | Special Characters | Test filenames with special chars | 1. Save PCAP with special chars | JSON created with correct name handling |
| PJ-GEN-004 | Storage Location | Test different save locations | 1. Save to different directories | JSON saves in same location as PCAP |
| PJ-GEN-005 | Concurrent Operations | Test simultaneous operations | 1. Save while capturing | JSON generates without corruption |

### 2.2 JSON Format (PJ-FMT)
| ID | Test Case | Description | Steps | Expected Result |
|----|-----------|-------------|--------|-----------------|
| PJ-FMT-001 | Structure | Verify JSON structure | 1. Generate JSON file<br>2. Validate format | Valid JSON with required fields |
| PJ-FMT-002 | Data Fields | Check required fields | 1. Generate JSON file<br>2. Check fields | Contains device name, manufacturer, Android version, hardware info |
| PJ-FMT-003 | Character Encoding | Test special characters | 1. Generate with special chars | UTF-8 encoding handled properly |
| PJ-FMT-004 | Optional Fields | Test optional information | 1. Generate with varying info | Optional fields properly formatted |
| PJ-FMT-005 | File Size | Check file size limits | 1. Generate with full device info | Reasonable file size (<1MB) |

## 3. Compatibility Tests

### 3.1 Device Compatibility (DI-COMP)
| ID | Test Case | Description | Steps | Expected Result |
|----|-----------|-------------|--------|-----------------|
| DI-COMP-001 | Android Versions | Test on different Android versions | 1. Test on Android 8-13 | Functions on all supported versions |
| DI-COMP-002 | Manufacturers | Test various device brands | 1. Test on different brands | Works across major manufacturers |
| DI-COMP-003 | Screen Sizes | Test different screen sizes | 1. Test on various displays | Adapts to all common screen sizes |
| DI-COMP-004 | Languages | Test different system languages | 1. Change system language | Displays correctly in all languages |
| DI-COMP-005 | Hardware Specs | Test different hardware configs | 1. Test on various specs | Works with all hardware variations |

### 3.2 Error Handling (DI-ERR)
| ID | Test Case | Description | Steps | Expected Result |
|----|-----------|-------------|--------|-----------------|
| DI-ERR-001 | Storage Permission | Test storage permission handling | 1. Deny storage permission | Shows appropriate error message |
| DI-ERR-002 | Storage Space | Test insufficient space | 1. Fill storage<br>2. Try to save | Clear error message about space |
| DI-ERR-003 | Info Access | Test info access failures | 1. Restrict device info access | Graceful error handling with message |
| DI-ERR-004 | File Operations | Test file operation failures | 1. Make location read-only | Proper error message for write failure |
| DI-ERR-005 | Concurrent Errors | Test error during other operations | 1. Cause error during capture | Handles errors without crashing |

## Test Environment Requirements

### Minimum Test Coverage
- Android versions: 8.0 to 13.0
- Screen sizes: Small (4"), Medium (5.5"), Large (7"+)
- Languages: English, non-Latin script
- Network conditions: Online, Offline
- Storage states: Adequate space, Low space

### Test Devices
- Budget Android device (e.g., Xiaomi Redmi)
- Mid-range Android device (e.g., Samsung Galaxy A series)
- High-end Android device (e.g., Google Pixel)
- Tablet device (e.g., Samsung Galaxy Tab)
- Different manufacturer devices (Samsung, Xiaomi, Google, etc.)

### Test Tools
- Android Studio for debugging
- Device file explorer for JSON verification
- JSON validator for format checking
- Storage space analyzer for space tests
