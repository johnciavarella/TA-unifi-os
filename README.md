# TA_unifi_os


🛑🛑🛑**THE OUTPUT IS NOT SANATIZED AND WILL INCLUDE PASSWORDS AND OTHER SENSITIVE INFORMATION**🛑🛑🛑


This is a Splunk Unifi TA leveraging the API calls. It is intended to close the gap on the lack of fidelity from syslog messages generated. 

Eventually will roll in syslog messages and SNMP to get a 360 view of Unifi and UISP products 

# Setup 
Use the configuration menu to add: 
- Controller IP = The IP address of your Unifi device (Ex. 192.0.0.1)
- Username = Admin username (may be Unifi login) 
- Password = That password 

# Suggestions

- Set your polling slower.

# API endpoints for Ubiquiti

https://ubntwiki.com/products/software/unifi-controller/api 

|Dropdown|Option|Path	Notes|
|----|------|------|
|unifi:wlan|rest/wlanconf|List WLANs, edit current WLANs and create new WLANs|
|unifi:users|rest/user|List of all configured/known clients on the site|
|unifi:user_info|self|Logged in user|
|unifi:system_info|stat/sysinfo|Some high-level information about the controller|
|unifi:switch_ports|rest/portconf|Switch port profiles|
|unifi:settings|rest/setting|Detailed site settings, updating requires adding key and _id to path for PUT ../setting/{key}/{_id}|
|unifi:routes_userdefined|rest/routing|User defined routes (HTTP response 500 per controller version 7.1.66)|
|unifi:routes_active|stat/routing|All active routes on the device|
|unifi:radius_profile|rest/radiusprofile|Radius profiles|
|unifi:radius_accounts|rest/account|Radius accounts|
|unifi:macs_tagged|rest/tag|Tagged macs (api.err.Invalid per controller version 7.1.66)|
|unifi:health|stat/health|Health status of the site|
|unifi:firewall_rules_userdefined|rest/firewallrule|User defined firewall rules. This does not show auto-generated rules|
|unifi:firewall_portforwarding|rest/portforward|List all port forwards configured on the site|
|unifi:firewall_groups_userdefined|rest/firewallgroup|​User defined firewall groups.|
|unifi:events|stat/event|List site events by most recent first, 3000 result limit|
|unifi:dns_dynamic_config|rest/dynamicdns|DynamicDNS configuration|
|unifi:dns_dynamic|stat/dynamicdns|DynamicDNS information and status like current ip, last changed, and status|
|unifi:device_mac_address|stat/device/{mac}|(UDM only) Detailed list of device filtered by mac address|
|unifi:device_basic|stat/device-basic|List of site devices with only 'adopted', 'disabled', 'mac', 'state', 'type' keys, useful for filtering on type|
|unifi:device_advanced|stat/device|Detailed list of all devices on site. (Controller only) Can be filtered by POSTing {"macs": ["mac1", ... ]}|
|unifi:country_codes_rf|stat/current-channel|List of all RF channels based on the site country code|
|unifi:country_codes|stat/ccode|List of country codes|
|unifi:clients|stat/sta|List of all _active_ clients on the site|
|unifi:ap_spectrumscan|stat/spectrumscan|Get RF scan results, can be for a specific mac by appending to endpoint|
|unifi:ap_rouge|stat/rogueap|Neighboring APs optional json post 'within' = seen in the last x hours|
|unifi:alarm|stat/alarm|List alarms by most recent, 3000 result limit?|
