# PCAP JSON Generation Test Cases

## Test Category: File Generation
### Test Case PJ-GEN-001: Basic JSON File Generation
**Objective**: Verify that a device information JSON file is generated when saving a PCAP file.
**Preconditions**: 
- PCAPdroid app is installed and running
- Packet capture is active
- Storage permissions granted

**Test Steps**:
1. Start packet capture
2. Capture some network traffic
3. Stop capture
4. Save PCAP file with name "test_capture.pcap"
5. Verify JSON file generation
6. Check JSON file name format

**Expected Results**:
- JSON file is generated automatically
- JSON filename is "test_capture_device_info.json"
- JSON file is in same directory as PCAP
- File permissions are correct

### Test Case PJ-GEN-002: Multiple File Generation
**Objective**: Verify correct JSON file generation with multiple PCAP saves.
**Preconditions**: 
- PCAPdroid app is installed and running
- Multiple capture sessions completed

**Test Steps**:
1. Save first capture as "capture1.pcap"
2. Verify first JSON generation
3. Save second capture as "capture2.pcap"
4. Verify second JSON generation
5. Check both JSON files exist
6. Verify unique content in each

**Expected Results**:
- Separate JSON files for each PCAP
- Correct naming for each JSON file
- No file overwrites
- Unique device info in each file

### Test Case PJ-GEN-003: Special Characters in Filename
**Objective**: Verify JSON file generation with special characters in PCAP filename.
**Preconditions**: 
- PCAPdroid app is installed and running
- Capture ready to save

**Test Steps**:
1. Save PCAP with spaces in name
2. Save PCAP with unicode characters
3. Save PCAP with special characters
4. Verify JSON generation for each
5. Check filename handling

**Expected Results**:
- Correct JSON files generated
- Special characters handled properly
- No filename corruption
- Files accessible after save

### Test Case PJ-GEN-004: Storage Location Handling
**Objective**: Verify JSON file generation across different storage locations.
**Preconditions**: 
- PCAPdroid app is installed and running
- Access to different storage locations

**Test Steps**:
1. Save to internal storage
2. Save to external storage
3. Save to custom directory
4. Verify JSON generation in each location
5. Check file accessibility

**Expected Results**:
- JSON files generated in correct locations
- Proper handling of storage permissions
- Files accessible from all locations
- Consistent naming across locations

### Test Case PJ-GEN-005: Concurrent Operations
**Objective**: Verify JSON generation during concurrent operations.
**Preconditions**: 
- PCAPdroid app is installed and running
- Multiple captures ready to save

**Test Steps**:
1. Start saving multiple PCAP files
2. Monitor JSON file generation
3. Check for file locks/conflicts
4. Verify file integrity
5. Test rapid sequential saves

**Expected Results**:
- All JSON files generated correctly
- No file corruption
- Proper handling of concurrent saves
- All files contain correct data
