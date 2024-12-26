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
                    <topic id="2">
                        <title>UI/UX</title>
                        <children>
                            <topics type="attached">
                                <topic id="2.1">
                                    <title>Navigation and Display</title>
                                    <children>
                                        <topics type="attached">
                                            <topic id="2.1.1">
                                                <title>Navigation Drawer</title>
                                                <children>
                                                    <topics type="attached">
                                                        <topic id="2.1.1.1"><title>Drawer operation</title></topic>
                                                        <topic id="2.1.1.2"><title>Menu item navigation</title></topic>
                                                        <topic id="2.1.1.3"><title>Gesture handling</title></topic>
                                                    </topics>
                                                </children>
                                            </topic>
                                            <topic id="2.1.2">
                                                <title>Connection List</title>
                                                <children>
                                                    <topics type="attached">
                                                        <topic id="2.1.2.1"><title>Real-time updates</title></topic>
                                                        <topic id="2.1.2.2"><title>Scroll performance</title></topic>
                                                        <topic id="2.1.2.3"><title>Detail display</title></topic>
                                                    </topics>
                                                </children>
                                            </topic>
                                            <topic id="2.1.3">
                                                <title>Search Interface</title>
                                                <children>
                                                    <topics type="attached">
                                                        <topic id="2.1.3.1"><title>Search functionality</title></topic>
                                                        <topic id="2.1.3.2"><title>Filter operations</title></topic>
                                                        <topic id="2.1.3.3"><title>State preservation</title></topic>
                                                    </topics>
                                                </children>
                                            </topic>
                                            <topic id="2.1.4">
                                                <title>Compatibility</title>
                                                <children>
                                                    <topics type="attached">
                                                        <topic id="2.1.4.1"><title>Screen size adaptation</title></topic>
                                                        <topic id="2.1.4.2"><title>Orientation handling</title></topic>
                                                        <topic id="2.1.4.3"><title>Layout consistency</title></topic>
                                                    </topics>
                                                </children>
                                            </topic>
                                            <topic id="2.1.5">
                                                <title>Error Handling</title>
                                                <children>
                                                    <topics type="attached">
                                                        <topic id="2.1.5.1"><title>Error display</title></topic>
                                                        <topic id="2.1.5.2"><title>Recovery options</title></topic>
                                                        <topic id="2.1.5.3"><title>State management</title></topic>
                                                    </topics>
                                                </children>
                                            </topic>
                                            <topic id="2.1.6">
                                                <title>Performance</title>
                                                <children>
                                                    <topics type="attached">
                                                        <topic id="2.1.6.1"><title>UI responsiveness</title></topic>
                                                        <topic id="2.1.6.2"><title>Load handling</title></topic>
                                                        <topic id="2.1.6.3"><title>Update efficiency</title></topic>
                                                    </topics>
                                                </children>
                                            </topic>
                                        </topics>
                                    </children>
                                </topic>
                                <topic id="2.2">
                                    <title>Settings Management</title>
                                    <children>
                                        <topics type="attached">
                                            <topic id="2.2.1">
                                                <title>Settings Persistence</title>
                                                <children>
                                                    <topics type="attached">
                                                        <topic id="2.2.1.1"><title>Save and restore</title></topic>
                                                        <topic id="2.2.1.2"><title>Default handling</title></topic>
                                                        <topic id="2.2.1.3"><title>State preservation</title></topic>
                                                    </topics>
                                                </children>
                                            </topic>
                                            <topic id="2.2.2">
                                                <title>Permission Management</title>
                                                <children>
                                                    <topics type="attached">
                                                        <topic id="2.2.2.1"><title>Permission requests</title></topic>
                                                        <topic id="2.2.2.2"><title>State handling</title></topic>
                                                        <topic id="2.2.2.3"><title>Feature access</title></topic>
                                                    </topics>
                                                </children>
                                            </topic>
                                            <topic id="2.2.3">
                                                <title>Feature Toggles</title>
                                                <children>
                                                    <topics type="attached">
                                                        <topic id="2.2.3.1"><title>Toggle behavior</title></topic>
                                                        <topic id="2.2.3.2"><title>Dependencies</title></topic>
                                                        <topic id="2.2.3.3"><title>UI updates</title></topic>
                                                    </topics>
                                                </children>
                                            </topic>
                                            <topic id="2.2.4">
                                                <title>Settings Migration</title>
                                                <children>
                                                    <topics type="attached">
                                                        <topic id="2.2.4.1"><title>Version upgrades</title></topic>
                                                        <topic id="2.2.4.2"><title>Compatibility</title></topic>
                                                        <topic id="2.2.4.3"><title>Data preservation</title></topic>
                                                    </topics>
                                                </children>
                                            </topic>
                                            <topic id="2.2.5">
                                                <title>Configuration Changes</title>
                                                <children>
                                                    <topics type="attached">
                                                        <topic id="2.2.5.1"><title>Device changes</title></topic>
                                                        <topic id="2.2.5.2"><title>UI rebuilding</title></topic>
                                                        <topic id="2.2.5.3"><title>State recovery</title></topic>
                                                    </topics>
                                                </children>
                                            </topic>
                                            <topic id="2.2.6">
                                                <title>Import/Export</title>
                                                <children>
                                                    <topics type="attached">
                                                        <topic id="2.2.6.1"><title>File operations</title></topic>
                                                        <topic id="2.2.6.2"><title>Data validation</title></topic>
                                                        <topic id="2.2.6.3"><title>Restoration</title></topic>
                                                    </topics>
                                                </children>
                                            </topic>
                                        </topics>
                                    </children>
                                </topic>
                            </topics>
                        </children>
                    </topic>
                    <topic id="3">
                        <title>Dump Mode</title>
                        <children>
                            <topics type="attached">
                                <topic id="3.1">
                                    <title>HTTP Server</title>
                                    <children>
                                        <topics type="attached">
                                            <topic id="3.1.1">
                                                <title>Server Setup</title>
                                                <children>
                                                    <topics type="attached">
                                                        <topic id="3.1.1.1"><title>Configuration</title></topic>
                                                        <topic id="3.1.1.2"><title>Port binding</title></topic>
                                                        <topic id="3.1.1.3"><title>Status monitoring</title></topic>
                                                    </topics>
                                                </children>
                                            </topic>
                                            <topic id="3.1.2">
                                                <title>PCAP Generation</title>
                                                <children>
                                                    <topics type="attached">
                                                        <topic id="3.1.2.1"><title>File creation</title></topic>
                                                        <topic id="3.1.2.2"><title>Data updates</title></topic>
                                                        <topic id="3.1.2.3"><title>Integrity checks</title></topic>
                                                    </topics>
                                                </children>
                                            </topic>
                                            <topic id="3.1.3">
                                                <title>Download Features</title>
                                                <children>
                                                    <topics type="attached">
                                                        <topic id="3.1.3.1"><title>File access</title></topic>
                                                        <topic id="3.1.3.2"><title>Resume support</title></topic>
                                                        <topic id="3.1.3.3"><title>Progress tracking</title></topic>
                                                    </topics>
                                                </children>
                                            </topic>
                                            <topic id="3.1.4">
                                                <title>Network Support</title>
                                                <children>
                                                    <topics type="attached">
                                                        <topic id="3.1.4.1"><title>Connection types</title></topic>
                                                        <topic id="3.1.4.2"><title>Access modes</title></topic>
                                                        <topic id="3.1.4.3"><title>Network switching</title></topic>
                                                    </topics>
                                                </children>
                                            </topic>
                                            <topic id="3.1.5">
                                                <title>Security</title>
                                                <children>
                                                    <topics type="attached">
                                                        <topic id="3.1.5.1"><title>Authentication</title></topic>
                                                        <topic id="3.1.5.2"><title>Access control</title></topic>
                                                        <topic id="3.1.5.3"><title>Secure transfer</title></topic>
                                                    </topics>
                                                </children>
                                            </topic>
                                            <topic id="3.1.6">
                                                <title>Error Handling</title>
                                                <children>
                                                    <topics type="attached">
                                                        <topic id="3.1.6.1"><title>Error detection</title></topic>
                                                        <topic id="3.1.6.2"><title>Recovery process</title></topic>
                                                        <topic id="3.1.6.3"><title>Data preservation</title></topic>
                                                    </topics>
                                                </children>
                                            </topic>
                                        </topics>
                                    </children>
                                </topic>
                                <topic id="3.2">
                                    <title>File Operations</title>
                                    <children>
                                        <topics type="attached">
                                            <topic id="3.2.1">
                                                <title>Storage Permissions</title>
                                                <children>
                                                    <topics type="attached">
                                                        <topic id="3.2.1.1"><title>Permission requests</title></topic>
                                                        <topic id="3.2.1.2"><title>Storage access</title></topic>
                                                        <topic id="3.2.1.3"><title>Location selection</title></topic>
                                                    </topics>
                                                </children>
                                            </topic>
                                            <topic id="3.2.2">
                                                <title>File Operations</title>
                                                <children>
                                                    <topics type="attached">
                                                        <topic id="3.2.2.1"><title>Creation and writing</title></topic>
                                                        <topic id="3.2.2.2"><title>Data integrity</title></topic>
                                                        <topic id="3.2.2.3"><title>PCAP format</title></topic>
                                                    </topics>
                                                </children>
                                            </topic>
                                            <topic id="3.2.3">
                                                <title>File Sharing</title>
                                                <children>
                                                    <topics type="attached">
                                                        <topic id="3.2.3.1"><title>Share methods</title></topic>
                                                        <topic id="3.2.3.2"><title>Transfer process</title></topic>
                                                        <topic id="3.2.3.3"><title>Integrity verification</title></topic>
                                                    </topics>
                                                </children>
                                            </topic>
                                            <topic id="3.2.4">
                                                <title>Storage Compatibility</title>
                                                <children>
                                                    <topics type="attached">
                                                        <topic id="3.2.4.1"><title>Storage types</title></topic>
                                                        <topic id="3.2.4.2"><title>Access methods</title></topic>
                                                        <topic id="3.2.4.3"><title>Scoped storage</title></topic>
                                                    </topics>
                                                </children>
                                            </topic>
                                            <topic id="3.2.5">
                                                <title>Error Management</title>
                                                <children>
                                                    <topics type="attached">
                                                        <topic id="3.2.5.1"><title>Storage limits</title></topic>
                                                        <topic id="3.2.5.2"><title>Error recovery</title></topic>
                                                        <topic id="3.2.5.3"><title>Data preservation</title></topic>
                                                    </topics>
                                                </children>
                                            </topic>
                                            <topic id="3.2.6">
                                                <title>File Management</title>
                                                <children>
                                                    <topics type="attached">
                                                        <topic id="3.2.6.1"><title>File operations</title></topic>
                                                        <topic id="3.2.6.2"><title>UI updates</title></topic>
                                                        <topic id="3.2.6.3"><title>Operation validation</title></topic>
                                                    </topics>
                                                </children>
                                            </topic>
                                        </topics>
                                    </children>
                                </topic>
                                <topic id="3.3">
                                    <title>UDP Export</title>
                                    <children>
                                        <topics type="attached">
                                            <topic id="3.3.1">
                                                <title>Connection Setup</title>
                                                <children>
                                                    <topics type="attached">
                                                        <topic id="3.3.1.1"><title>Target configuration</title></topic>
                                                        <topic id="3.3.1.2"><title>Connection validation</title></topic>
                                                        <topic id="3.3.1.3"><title>Status monitoring</title></topic>
                                                    </topics>
                                                </children>
                                            </topic>
                                            <topic id="3.3.2">
                                                <title>Real-time Streaming</title>
                                                <children>
                                                    <topics type="attached">
                                                        <topic id="3.3.2.1"><title>Stream monitoring</title></topic>
                                                        <topic id="3.3.2.2"><title>Statistics tracking</title></topic>
                                                        <topic id="3.3.2.3"><title>Stream controls</title></topic>
                                                    </topics>
                                                </children>
                                            </topic>
                                            <topic id="3.3.3">
                                                <title>Tool Integration</title>
                                                <children>
                                                    <topics type="attached">
                                                        <topic id="3.3.3.1"><title>Wireshark support</title></topic>
                                                        <topic id="3.3.3.2"><title>Custom receivers</title></topic>
                                                        <topic id="3.3.3.3"><title>Format compatibility</title></topic>
                                                    </topics>
                                                </children>
                                            </topic>
                                            <topic id="3.3.4">
                                                <title>Network Compatibility</title>
                                                <children>
                                                    <topics type="attached">
                                                        <topic id="3.3.4.1"><title>Network types</title></topic>
                                                        <topic id="3.3.4.2"><title>Network conditions</title></topic>
                                                        <topic id="3.3.4.3"><title>Network switching</title></topic>
                                                    </topics>
                                                </children>
                                            </topic>
                                            <topic id="3.3.5">
                                                <title>Performance</title>
                                                <children>
                                                    <topics type="attached">
                                                        <topic id="3.3.5.1"><title>Load handling</title></topic>
                                                        <topic id="3.3.5.2"><title>Resource usage</title></topic>
                                                        <topic id="3.3.5.3"><title>Recovery behavior</title></topic>
                                                    </topics>
                                                </children>
                                            </topic>
                                            <topic id="3.3.6">
                                                <title>Error Management</title>
                                                <children>
                                                    <topics type="attached">
                                                        <topic id="3.3.6.1"><title>Error detection</title></topic>
                                                        <topic id="3.3.6.2"><title>Recovery process</title></topic>
                                                        <topic id="3.3.6.3"><title>Data preservation</title></topic>
                                                    </topics>
                                                </children>
                                            </topic>
                                        </topics>
                                    </children>
                                </topic>
                            </topics>
                        </children>
                    </topic>
                    <topic id="4">
                        <title>TLS Decryption</title>
                        <children>
                            <topics type="attached">
                                <topic id="4.1">
                                    <title>Setup Process</title>
                                    <children>
                                        <topics type="attached">
                                            <topic id="4.1.1">
                                                <title>Addon Installation</title>
                                                <children>
                                                    <topics type="attached">
                                                        <topic id="4.1.1.1"><title>Download and install</title></topic>
                                                        <topic id="4.1.1.2"><title>Integration check</title></topic>
                                                        <topic id="4.1.1.3"><title>Status verification</title></topic>
                                                    </topics>
                                                </children>
                                            </topic>
                                            <topic id="4.1.2">
                                                <title>Certificate Management</title>
                                                <children>
                                                    <topics type="attached">
                                                        <topic id="4.1.2.1"><title>CA generation</title></topic>
                                                        <topic id="4.1.2.2"><title>System installation</title></topic>
                                                        <topic id="4.1.2.3"><title>Trust validation</title></topic>
                                                    </topics>
                                                </children>
                                            </topic>
                                            <topic id="4.1.3">
                                                <title>Permission Setup</title>
                                                <children>
                                                    <topics type="attached">
                                                        <topic id="4.1.3.1"><title>System permissions</title></topic>
                                                        <topic id="4.1.3.2"><title>App access</title></topic>
                                                        <topic id="4.1.3.3"><title>State persistence</title></topic>
                                                    </topics>
                                                </children>
                                            </topic>
                                            <topic id="4.1.4">
                                                <title>Version Compatibility</title>
                                                <children>
                                                    <topics type="attached">
                                                        <topic id="4.1.4.1"><title>Android support</title></topic>
                                                        <topic id="4.1.4.2"><title>Security models</title></topic>
                                                        <topic id="4.1.4.3"><title>Permission handling</title></topic>
                                                    </topics>
                                                </children>
                                            </topic>
                                            <topic id="4.1.5">
                                                <title>Security Validation</title>
                                                <children>
                                                    <topics type="attached">
                                                        <topic id="4.1.5.1"><title>Certificate chain</title></topic>
                                                        <topic id="4.1.5.2"><title>Key protection</title></topic>
                                                        <topic id="4.1.5.3"><title>Encryption strength</title></topic>
                                                    </topics>
                                                </children>
                                            </topic>
                                            <topic id="4.1.6">
                                                <title>Error Handling</title>
                                                <children>
                                                    <topics type="attached">
                                                        <topic id="4.1.6.1"><title>Installation errors</title></topic>
                                                        <topic id="4.1.6.2"><title>Recovery process</title></topic>
                                                        <topic id="4.1.6.3"><title>State preservation</title></topic>
                                                    </topics>
                                                </children>
                                            </topic>
                                        </topics>
                                    </children>
                                </topic>
                                <topic id="4.2">
                                    <title>Rule Management</title>
                                    <children>
                                        <topics type="attached">
                                            <topic id="4.2.1">
                                                <title>Rule Creation</title>
                                                <children>
                                                    <topics type="attached">
                                                        <topic id="4.2.1.1"><title>Interface validation</title></topic>
                                                        <topic id="4.2.1.2"><title>Parameter configuration</title></topic>
                                                        <topic id="4.2.1.3"><title>Rule persistence</title></topic>
                                                    </topics>
                                                </children>
                                            </topic>
                                            <topic id="4.2.2">
                                                <title>App-Specific Rules</title>
                                                <children>
                                                    <topics type="attached">
                                                        <topic id="4.2.2.1"><title>App selection</title></topic>
                                                        <topic id="4.2.2.2"><title>Rule application</title></topic>
                                                        <topic id="4.2.2.3"><title>Traffic filtering</title></topic>
                                                    </topics>
                                                </children>
                                            </topic>
                                            <topic id="4.2.3">
                                                <title>Domain Filtering</title>
                                                <children>
                                                    <topics type="attached">
                                                        <topic id="4.2.3.1"><title>Pattern matching</title></topic>
                                                        <topic id="4.2.3.2"><title>Wildcard handling</title></topic>
                                                        <topic id="4.2.3.3"><title>Exclusion rules</title></topic>
                                                    </topics>
                                                </children>
                                            </topic>
                                            <topic id="4.2.4">
                                                <title>Multi-App Support</title>
                                                <children>
                                                    <topics type="attached">
                                                        <topic id="4.2.4.1"><title>App compatibility</title></topic>
                                                        <topic id="4.2.4.2"><title>Security handling</title></topic>
                                                        <topic id="4.2.4.3"><title>Rule inheritance</title></topic>
                                                    </topics>
                                                </children>
                                            </topic>
                                            <topic id="4.2.5">
                                                <title>Conflict Resolution</title>
                                                <children>
                                                    <topics type="attached">
                                                        <topic id="4.2.5.1"><title>Priority management</title></topic>
                                                        <topic id="4.2.5.2"><title>Resolution logic</title></topic>
                                                        <topic id="4.2.5.3"><title>Edge cases</title></topic>
                                                    </topics>
                                                </children>
                                            </topic>
                                            <topic id="4.2.6">
                                                <title>Dynamic Updates</title>
                                                <children>
                                                    <topics type="attached">
                                                        <topic id="4.2.6.1"><title>Live modifications</title></topic>
                                                        <topic id="4.2.6.2"><title>Connection handling</title></topic>
                                                        <topic id="4.2.6.3"><title>State management</title></topic>
                                                    </topics>
                                                </children>
                                            </topic>
                                        </topics>
                                    </children>
                                </topic>
                            </topics>
                        </children>
                    </topic>
                    <topic id="5">
                        <title>Advanced Features</title>
                        <children>
                            <topics type="attached">
                                <topic id="5.1">
                                    <title>DNS Management</title>
                                    <children>
                                        <topics type="attached">
                                            <topic id="5.1.1">
                                                <title>Server Configuration</title>
                                                <children>
                                                    <topics type="attached">
                                                        <topic id="5.1.1.1"><title>Auto-detection</title></topic>
                                                        <topic id="5.1.1.2"><title>Manual override</title></topic>
                                                        <topic id="5.1.1.3"><title>Persistence</title></topic>
                                                    </topics>
                                                </children>
                                            </topic>
                                            <topic id="5.1.2">
                                                <title>Protocol Support</title>
                                                <children>
                                                    <topics type="attached">
                                                        <topic id="5.1.2.1"><title>Protocol selection</title></topic>
                                                        <topic id="5.1.2.2"><title>Settings configuration</title></topic>
                                                        <topic id="5.1.2.3"><title>Resolution testing</title></topic>
                                                    </topics>
                                                </children>
                                            </topic>
                                            <topic id="5.1.3">
                                                <title>DoH Integration</title>
                                                <children>
                                                    <topics type="attached">
                                                        <topic id="5.1.3.1"><title>Server setup</title></topic>
                                                        <topic id="5.1.3.2"><title>Custom endpoints</title></topic>
                                                        <topic id="5.1.3.3"><title>HTTPS validation</title></topic>
                                                    </topics>
                                                </children>
                                            </topic>
                                            <topic id="5.1.4">
                                                <title>IP Protocol Support</title>
                                                <children>
                                                    <topics type="attached">
                                                        <topic id="5.1.4.1"><title>IPv4/IPv6 handling</title></topic>
                                                        <topic id="5.1.4.2"><title>Dual-stack operation</title></topic>
                                                        <topic id="5.1.4.3"><title>Fallback mechanisms</title></topic>
                                                    </topics>
                                                </children>
                                            </topic>
                                            <topic id="5.1.5">
                                                <title>Security Features</title>
                                                <children>
                                                    <topics type="attached">
                                                        <topic id="5.1.5.1"><title>DNSSEC validation</title></topic>
                                                        <topic id="5.1.5.2"><title>Certificate handling</title></topic>
                                                        <topic id="5.1.5.3"><title>Filtering rules</title></topic>
                                                    </topics>
                                                </children>
                                            </topic>
                                            <topic id="5.1.6">
                                                <title>Network Handling</title>
                                                <children>
                                                    <topics type="attached">
                                                        <topic id="5.1.6.1"><title>State transitions</title></topic>
                                                        <topic id="5.1.6.2"><title>Connection management</title></topic>
                                                        <topic id="5.1.6.3"><title>Cache behavior</title></topic>
                                                    </topics>
                                                </children>
                                            </topic>
                                        </topics>
                                    </children>
                                </topic>
                                <topic id="5.2">
                                    <title>Root Capture</title>
                                    <children>
                                        <topics type="attached">
                                            <topic id="5.2.1">
                                                <title>Permission Management</title>
                                                <children>
                                                    <topics type="attached">
                                                        <topic id="5.2.1.1"><title>Access request</title></topic>
                                                        <topic id="5.2.1.2"><title>Permission handling</title></topic>
                                                        <topic id="5.2.1.3"><title>Status verification</title></topic>
                                                    </topics>
                                                </children>
                                            </topic>
                                            <topic id="5.2.2">
                                                <title>Interface Management</title>
                                                <children>
                                                    <topics type="attached">
                                                        <topic id="5.2.2.1"><title>Interface scanning</title></topic>
                                                        <topic id="5.2.2.2"><title>Selection handling</title></topic>
                                                        <topic id="5.2.2.3"><title>Status monitoring</title></topic>
                                                    </topics>
                                                </children>
                                            </topic>
                                            <topic id="5.2.3">
                                                <title>Capture Settings</title>
                                                <children>
                                                    <topics type="attached">
                                                        <topic id="5.2.3.1"><title>Mode configuration</title></topic>
                                                        <topic id="5.2.3.2"><title>Filter management</title></topic>
                                                        <topic id="5.2.3.3"><title>Settings validation</title></topic>
                                                    </topics>
                                                </children>
                                            </topic>
                                            <topic id="5.2.4">
                                                <title>Root Compatibility</title>
                                                <children>
                                                    <topics type="attached">
                                                        <topic id="5.2.4.1"><title>Root solution support</title></topic>
                                                        <topic id="5.2.4.2"><title>Version handling</title></topic>
                                                        <topic id="5.2.4.3"><title>Custom solutions</title></topic>
                                                    </topics>
                                                </children>
                                            </topic>
                                            <topic id="5.2.5">
                                                <title>Capture Stability</title>
                                                <children>
                                                    <topics type="attached">
                                                        <topic id="5.2.5.1"><title>Long-term monitoring</title></topic>
                                                        <topic id="5.2.5.2"><title>Resource management</title></topic>
                                                        <topic id="5.2.5.3"><title>Data integrity</title></topic>
                                                    </topics>
                                                </children>
                                            </topic>
                                            <topic id="5.2.6">
                                                <title>Error Handling</title>
                                                <children>
                                                    <topics type="attached">
                                                        <topic id="5.2.6.1"><title>Root loss recovery</title></topic>
                                                        <topic id="5.2.6.2"><title>Interface errors</title></topic>
                                                        <topic id="5.2.6.3"><title>State restoration</title></topic>
                                                    </topics>
                                                </children>
                                            </topic>
                                        </topics>
                                    </children>
                                </topic>
                            </topics>
                        </children>
                    </topic>
                    <topic id="6">
                        <title>Compatibility Tests</title>
                        <children>
                            <topics type="attached">
                                <topic id="6.1">
                                    <title>Version Support</title>
                                    <children>
                                        <topics type="attached">
                                            <topic id="6.1.1">
                                                <title>Base Compatibility</title>
                                                <children>
                                                    <topics type="attached">
                                                        <topic id="6.1.1.1"><title>Installation verification</title></topic>
                                                        <topic id="6.1.1.2"><title>UI rendering</title></topic>
                                                        <topic id="6.1.1.3"><title>Core functionality</title></topic>
                                                    </topics>
                                                </children>
                                            </topic>
                                            <topic id="6.1.2">
                                                <title>Permission Management</title>
                                                <children>
                                                    <topics type="attached">
                                                        <topic id="6.1.2.1"><title>Runtime permissions</title></topic>
                                                        <topic id="6.1.2.2"><title>Storage access</title></topic>
                                                        <topic id="6.1.2.3"><title>VPN configuration</title></topic>
                                                    </topics>
                                                </children>
                                            </topic>
                                            <topic id="6.1.3">
                                                <title>API Compatibility</title>
                                                <children>
                                                    <topics type="attached">
                                                        <topic id="6.1.3.1"><title>Feature support</title></topic>
                                                        <topic id="6.1.3.2"><title>Fallback mechanisms</title></topic>
                                                        <topic id="6.1.3.3"><title>API deprecation</title></topic>
                                                    </topics>
                                                </children>
                                            </topic>
                                            <topic id="6.1.4">
                                                <title>Installation Scenarios</title>
                                                <children>
                                                    <topics type="attached">
                                                        <topic id="6.1.4.1"><title>Fresh install</title></topic>
                                                        <topic id="6.1.4.2"><title>Version upgrade</title></topic>
                                                        <topic id="6.1.4.3"><title>Data migration</title></topic>
                                                    </topics>
                                                </children>
                                            </topic>
                                            <topic id="6.1.5">
                                                <title>Security Framework</title>
                                                <children>
                                                    <topics type="attached">
                                                        <topic id="6.1.5.1"><title>Security models</title></topic>
                                                        <topic id="6.1.5.2"><title>Certificate handling</title></topic>
                                                        <topic id="6.1.5.3"><title>Encryption support</title></topic>
                                                    </topics>
                                                </children>
                                            </topic>
                                            <topic id="6.1.6">
                                                <title>Edge Cases</title>
                                                <children>
                                                    <topics type="attached">
                                                        <topic id="6.1.6.1"><title>Version transitions</title></topic>
                                                        <topic id="6.1.6.2"><title>Feature availability</title></topic>
                                                        <topic id="6.1.6.3"><title>Error scenarios</title></topic>
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
