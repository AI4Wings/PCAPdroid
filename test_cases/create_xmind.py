import zipfile
import os

# Create temporary directory structure
os.makedirs('temp_xmind/META-INF', exist_ok=True)

# Create manifest.xml
manifest_content = '''<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<manifest xmlns="urn:xmind:xmap:xmlns:manifest:1.0">
    <file-entry full-path="content.xml" media-type="text/xml"/>
    <file-entry full-path="META-INF/manifest.xml" media-type="text/xml"/>
    <file-entry full-path="styles.xml" media-type="text/xml"/>
    <file-entry full-path="meta.xml" media-type="text/xml"/>
</manifest>'''

# Create content.xml
content_xml = '''<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<xmap-content xmlns="urn:xmind:xmap:xmlns:content:2.0" xmlns:fo="http://www.w3.org/1999/XSL/Format" xmlns:svg="http://www.w3.org/2000/svg" xmlns:xhtml="http://www.w3.org/1999/xhtml" xmlns:xlink="http://www.w3.org/1999/xlink" timestamp="1735191895000" version="2.0">
    <sheet id="1" timestamp="1735191895000">
        <topic id="root" structure-class="org.xmind.ui.map.unbalanced" timestamp="1735191895000">
            <title>PCAPdroid Test Cases</title>
            <children>
                <topics type="attached">
                    <topic id="1" timestamp="1735191895000">
                        <title>Core Functionality</title>
                        <children>
                            <topics type="attached">
                                <topic id="1.1">
                                    <title>VPN Service Management</title>
                                    <children>
                                        <topics type="attached">
                                            <topic id="1.1.1">
                                                <title>Initial Setup</title>
                                                <children>
                                                    <topics type="attached">
                                                        <topic id="1.1.1.1"><title>Launch app and start capture</title></topic>
                                                        <topic id="1.1.1.2"><title>VPN permission handling</title></topic>
                                                        <topic id="1.1.1.3"><title>Status indicators verification</title></topic>
                                                    </topics>
                                                </children>
                                            </topic>
                                            <topic id="1.1.2">
                                                <title>Battery Optimization</title>
                                                <children>
                                                    <topics type="attached">
                                                        <topic id="1.1.2.1"><title>Background operation</title></topic>
                                                        <topic id="1.1.2.2"><title>Service continuity</title></topic>
                                                        <topic id="1.1.2.3"><title>Battery state handling</title></topic>
                                                    </topics>
                                                </children>
                                            </topic>
                                        </topics>
                                    </children>
                                </topic>
                                <topic id="1.2">
                                    <title>Network Traffic Capture</title>
                                    <children>
                                        <topics type="attached">
                                            <topic id="1.2.1">
                                                <title>Basic Capture</title>
                                                <children>
                                                    <topics type="attached">
                                                        <topic id="1.2.1.1"><title>Real-time connection monitoring</title></topic>
                                                        <topic id="1.2.1.2"><title>Traffic detail accuracy</title></topic>
                                                        <topic id="1.2.1.3"><title>Clean capture termination</title></topic>
                                                    </topics>
                                                </children>
                                            </topic>
                                            <topic id="1.2.2">
                                                <title>Traffic Filtering</title>
                                                <children>
                                                    <topics type="attached">
                                                        <topic id="1.2.2.1"><title>App-specific filtering</title></topic>
                                                        <topic id="1.2.2.2"><title>Protocol filtering</title></topic>
                                                        <topic id="1.2.2.3"><title>Search functionality</title></topic>
                                                    </topics>
                                                </children>
                                            </topic>
                                            <topic id="1.2.3">
                                                <title>Connection Tracking</title>
                                                <children>
                                                    <topics type="attached">
                                                        <topic id="1.2.3.1"><title>Status monitoring</title></topic>
                                                        <topic id="1.2.3.2"><title>Protocol detection</title></topic>
                                                        <topic id="1.2.3.3"><title>Connection cleanup</title></topic>
                                                    </topics>
                                                </children>
                                            </topic>
                                            <topic id="1.2.4">
                                                <title>Performance</title>
                                                <children>
                                                    <topics type="attached">
                                                        <topic id="1.2.4.1"><title>Resource monitoring</title></topic>
                                                        <topic id="1.2.4.2"><title>Packet loss tracking</title></topic>
                                                        <topic id="1.2.4.3"><title>UI responsiveness</title></topic>
                                                    </topics>
                                                </children>
                                            </topic>
                                            <topic id="1.2.5">
                                                <title>Protocol Support</title>
                                                <children>
                                                    <topics type="attached">
                                                        <topic id="1.2.5.1"><title>TCP/UDP handling</title></topic>
                                                        <topic id="1.2.5.2"><title>ICMP support</title></topic>
                                                        <topic id="1.2.5.3"><title>IPv6 compatibility</title></topic>
                                                    </topics>
                                                </children>
                                            </topic>
                                        </topics>
                                    </children>
                                </topic>
                            </topics>
                        </children>
                    </topic>
                </topics>
            </children>
        </topic>
    </sheet>
</xmap-content>'''

# Create styles.xml
styles_xml = '''<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<xmap-styles xmlns="urn:xmind:xmap:xmlns:style:2.0" xmlns:fo="http://www.w3.org/1999/XSL/Format" version="2.0"/>'''

# Create meta.xml
meta_xml = '''<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<meta xmlns="urn:xmind:xmap:xmlns:meta:2.0" version="2.0"/>'''

# Write files
with open('temp_xmind/META-INF/manifest.xml', 'w') as f:
    f.write(manifest_content)
with open('temp_xmind/content.xml', 'w') as f:
    f.write(content_xml)
with open('temp_xmind/styles.xml', 'w') as f:
    f.write(styles_xml)
with open('temp_xmind/meta.xml', 'w') as f:
    f.write(meta_xml)

# Create XMind file (ZIP archive)
with zipfile.ZipFile('test_cases_mind_map.xmind', 'w', zipfile.ZIP_DEFLATED) as zf:
    zf.write('temp_xmind/META-INF/manifest.xml', 'META-INF/manifest.xml')
    zf.write('temp_xmind/content.xml', 'content.xml')
    zf.write('temp_xmind/styles.xml', 'styles.xml')
    zf.write('temp_xmind/meta.xml', 'meta.xml')

# Clean up
import shutil
shutil.rmtree('temp_xmind')
