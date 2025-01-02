import zipfile
import json
import os
from datetime import datetime
import uuid

def generate_uuid():
    return str(uuid.uuid4())

def create_topic(title, children=None):
    topic = {
        "id": generate_uuid(),
        "title": title
    }
    if children:
        topic["children"] = {"attached": children}
    return topic

def create_xmind_content():
    # Create test case topics
    core_functionality = create_topic("Core Functionality", [
        create_topic("Device Information Display", [
            create_topic("DI-DISP-001: Basic Device Information Display"),
            create_topic("DI-DISP-002: Layout Responsiveness"),
            create_topic("DI-DISP-003: Scroll Behavior"),
            create_topic("DI-DISP-004: Text Scaling Compatibility"),
            create_topic("DI-DISP-005: Dark Mode Compatibility")
        ]),
        create_topic("Device Information Accuracy", [
            create_topic("DI-ACC-001: Device Name Accuracy"),
            create_topic("DI-ACC-002: Manufacturer Information Accuracy"),
            create_topic("DI-ACC-003: Android Version Accuracy"),
            create_topic("DI-ACC-004: Hardware Information Accuracy"),
            create_topic("DI-ACC-005: Real-time Information Updates")
        ])
    ])

    ui_functionality = create_topic("User Interface", [
        create_topic("Navigation and Interaction", [
            create_topic("DI-NAV-001: Access from Main Menu"),
            create_topic("DI-NAV-002: State Preservation"),
            create_topic("DI-NAV-003: Multiple Access Points"),
            create_topic("DI-NAV-004: Navigation During Updates"),
            create_topic("DI-NAV-005: Accessibility Navigation")
        ])
    ])

    data_handling = create_topic("Data Handling", [
        create_topic("PCAP JSON Generation", [
            create_topic("PJ-GEN-001: Basic JSON File Generation"),
            create_topic("PJ-GEN-002: Multiple File Generation"),
            create_topic("PJ-GEN-003: Special Characters in Filename"),
            create_topic("PJ-GEN-004: Storage Location Handling"),
            create_topic("PJ-GEN-005: Concurrent Operations")
        ]),
        create_topic("JSON Format Validation", [
            create_topic("PJ-FMT-001: JSON Structure Validation"),
            create_topic("PJ-FMT-002: Data Field Accuracy"),
            create_topic("PJ-FMT-003: Character Encoding"),
            create_topic("PJ-FMT-004: Optional Fields Handling"),
            create_topic("PJ-FMT-005: JSON File Size")
        ])
    ])

    compatibility = create_topic("Compatibility", [
        create_topic("Device Compatibility", [
            create_topic("DI-COMP-001: Android Version Compatibility"),
            create_topic("DI-COMP-002: Device Manufacturer Compatibility"),
            create_topic("DI-COMP-003: Screen Size Compatibility"),
            create_topic("DI-COMP-004: System Language Compatibility"),
            create_topic("DI-COMP-005: Hardware Variation Compatibility")
        ])
    ])

    error_handling = create_topic("Error Handling", [
        create_topic("Error Scenarios", [
            create_topic("DI-ERR-001: Storage Permission Handling"),
            create_topic("DI-ERR-002: Storage Space Handling"),
            create_topic("DI-ERR-003: Device Information Access Errors"),
            create_topic("DI-ERR-004: File Operation Errors"),
            create_topic("DI-ERR-005: Concurrent Operation Errors")
        ])
    ])

    # Create root topic with all sections
    root_topic = create_topic("PCAPdroid Device Info Feature Test Cases", [
        core_functionality,
        ui_functionality,
        data_handling,
        compatibility,
        error_handling
    ])

    # Create workbook structure
    workbook = {
        "id": generate_uuid(),
        "class": "workbook",
        "sheets": [{
            "id": generate_uuid(),
            "class": "sheet",
            "title": "PCAPdroid Device Info Feature Test Cases",
            "rootTopic": root_topic
        }]
    }
    return workbook

def create_xmind():
    # Create directories if they don't exist
    os.makedirs('Thumbnails', exist_ok=True)
    
    # Create a new ZIP file
    with zipfile.ZipFile('test_cases_mind_map.xmind', 'w', zipfile.ZIP_DEFLATED) as zf:
        # Add content.json
        content = create_xmind_content()
        zf.writestr('content.json', json.dumps({
            "format": "xmind",
            "version": "2.0",
            "content": [content]
        }, indent=2))
        
        # Add manifest.json
        manifest = {
            "file-entries": {
                "content.json": {"type": "application/json"},
                "metadata.json": {"type": "application/json"},
                "Thumbnails/thumbnail.png": {"type": "image/png"},
                "styles.json": {"type": "application/json"}
            }
        }
        zf.writestr('manifest.json', json.dumps(manifest, indent=2))
        
        # Add metadata.json
        metadata = {
            "creator": {
                "name": "PCAPdroid Test Cases",
                "version": "2.0"
            },
            "created": datetime.now().isoformat(),
            "generator": {
                "name": "Python XMind Generator",
                "version": "1.0"
            }
        }
        zf.writestr('metadata.json', json.dumps(metadata, indent=2))
        
        # Add styles.json
        styles = {
            "styles": [],
            "master-styles": {}
        }
        zf.writestr('styles.json', json.dumps(styles, indent=2))
        
        # Create and add empty thumbnail
        zf.writestr('Thumbnails/thumbnail.png', b'')

if __name__ == '__main__':
    create_xmind()
    print("XMind file created successfully!")
