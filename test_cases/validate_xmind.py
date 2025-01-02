import json
import zipfile
import sys
from pathlib import Path

def validate_xmind(filepath):
    print(f"Validating XMind file: {filepath}")
    print("\n=== ZIP Structure ===")
    
    try:
        with zipfile.ZipFile(filepath, 'r') as zf:
            files = zf.namelist()
            print("Files in archive:")
            for f in files:
                print(f"- {f}")
            
            required_files = [
                'content.json',
                'manifest.json',
                'metadata.json',
                'styles.json',
                'Thumbnails/thumbnail.png'
            ]
            
            missing = [f for f in required_files if f not in files]
            if missing:
                print("\nERROR: Missing required files:")
                for f in missing:
                    print(f"- {f}")
                return False
            
            print("\n=== JSON Validation ===")
            
            # Validate content.json
            content = json.loads(zf.read('content.json'))
            assert content.get('format') == 'xmind', "Invalid format in content.json"
            assert content.get('version') == '2.0', "Invalid version in content.json"
            print("content.json: Valid")
            
            # Validate manifest.json
            manifest = json.loads(zf.read('manifest.json'))
            assert 'file-entries' in manifest, "Missing file-entries in manifest.json"
            print("manifest.json: Valid")
            
            # Validate metadata.json
            metadata = json.loads(zf.read('metadata.json'))
            assert 'creator' in metadata, "Missing creator in metadata.json"
            print("metadata.json: Valid")
            
            # Validate styles.json
            styles = json.loads(zf.read('styles.json'))
            assert 'styles' in styles, "Missing styles in styles.json"
            print("styles.json: Valid")
            
            print("\nAll validations passed successfully!")
            return True
            
    except Exception as e:
        print(f"\nERROR: Validation failed - {str(e)}")
        return False

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python validate_xmind.py <xmind_file>")
        sys.exit(1)
        
    xmind_file = Path(sys.argv[1])
    if not xmind_file.exists():
        print(f"ERROR: File not found: {xmind_file}")
        sys.exit(1)
        
    success = validate_xmind(xmind_file)
    sys.exit(0 if success else 1)
