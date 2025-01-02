# PCAP JSON Format Test Cases

## Test Category: JSON Format Validation
### Test Case PJ-FMT-001: JSON Structure Validation
**Objective**: Verify that generated JSON files follow the required structure and format.
**Preconditions**: 
- PCAPdroid app is installed and running
- Generated JSON file available

**Test Steps**:
1. Generate device info JSON file
2. Open JSON file
3. Verify required fields:
   - Device name
   - Manufacturer
   - Android version
   - Hardware info
4. Check JSON syntax
5. Validate data types

**Expected Results**:
- Valid JSON syntax
- All required fields present
- Correct data types used
- Proper nesting structure

### Test Case PJ-FMT-002: Data Field Accuracy
**Objective**: Verify accuracy of data fields in JSON file.
**Preconditions**: 
- PCAPdroid app is installed and running
- Access to system settings

**Test Steps**:
1. Generate device info JSON
2. Compare device name field
3. Compare manufacturer field
4. Compare Android version
5. Compare hardware info
6. Verify timestamps if present

**Expected Results**:
- All fields match device settings
- Correct formatting of values
- No data truncation
- Accurate timestamps

### Test Case PJ-FMT-003: Character Encoding
**Objective**: Verify proper handling of character encoding in JSON.
**Preconditions**: 
- PCAPdroid app is installed and running
- Device with non-ASCII characters in settings

**Test Steps**:
1. Set device name with special characters
2. Generate JSON file
3. Verify character encoding
4. Check string escaping
5. Validate UTF-8 compliance

**Expected Results**:
- Proper UTF-8 encoding
- Special characters preserved
- Correct string escaping
- No encoding corruption


### Test Case PJ-FMT-004: Optional Fields Handling
**Objective**: Verify handling of optional device information fields.
**Preconditions**: 
- PCAPdroid app is installed and running
- Various device configurations

**Test Steps**:
1. Generate JSON with all fields available
2. Generate JSON with some fields unavailable
3. Check optional field handling
4. Verify null value handling
5. Check field omission logic

**Expected Results**:
- Optional fields properly handled
- Null values correctly represented
- No missing required fields
- Consistent format maintained

### Test Case PJ-FMT-005: JSON File Size
**Objective**: Verify reasonable JSON file size and content optimization.
**Preconditions**: 
- PCAPdroid app is installed and running
- Multiple device configurations

**Test Steps**:
1. Generate JSON files
2. Check file sizes
3. Verify no redundant data
4. Check whitespace handling
5. Validate content efficiency

**Expected Results**:
- Reasonable file sizes
- No unnecessary whitespace
- Efficient data representation
- No redundant information
