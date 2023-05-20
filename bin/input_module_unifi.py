
# encoding = utf-8

import os
import sys
import time
import datetime

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning


conversion_dict = {
    'rest/wlanconf': 'unifi:wlan',
    'rest/user': 'unifi:users',
    'self': 'unifi:user_info',
    'stat/sysinfo': 'unifi:system_info',
    'rest/portconf': 'unifi:switch_ports',
    'rest/setting': 'unifi:settings',
    'rest/routing': 'unifi:routes_userdefined',
    'stat/routing': 'unifi:routes_active',
    'rest/radiusprofile': 'unifi:radius_profile',
    'rest/account': 'unifi:radius_accounts',
    'rest/tag': 'unifi:macs_tagged',
    'stat/health': 'unifi:health',
    'rest/firewallrule': 'unifi:firewall_rules_userdefined',
    'rest/portforward': 'unifi:firewall_portforwarding',
    'rest/firewallgroup': 'unifi:firewall_groups_userdefined',
    'stat/event': 'unifi:events',
    'rest/dynamicdns': 'unifi:dns_dynamic_config',
    'stat/dynamicdns': 'unifi:dns_dynamic',
    'stat/device/{mac}': 'unifi:device_mac_address',
    'stat/device-basic': 'unifi:device_basic',
    'stat/device': 'unifi:device_advanced',
    'stat/current-channel': 'unifi:country_codes_rf',
    'stat/ccode': 'unifi:country_codes',
    'stat/sta': 'unifi:clients',
    'stat/spectrumscan': 'unifi:ap_spectrumscan',
    'stat/rogueap': 'unifi:ap_rouge',
    'stat/alarm': 'unifi:alarm'
}




def validate_input(helper, definition):
    """Implement your own validation logic to validate the input stanza configurations"""
    # This example accesses the modular input variable
    # server = definition.parameters.get('server', None)
    pass

def collect_events(helper, ew):



    # Auth - Get username and password
    usr = helper.get_global_setting("username")
    password = helper.get_global_setting("password")
    auth_url = 'https://'+helper.get_global_setting("unifi_controller")+'/api/auth/login'

    #Acutal API Call
    rest_path = helper.get_arg("rest_endpoint")
    rest_url = 'https://'+helper.get_global_setting("unifi_controller")+'/proxy/network/api/s/default/'+rest_path

    #Authenticate
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    headers = {"Accept": "application/json","Content-Type": "application/json"}
    data = {'username': usr, 'password': password}
    s = requests.Session()
    r = s.post(auth_url, headers = headers,  json = data , verify = False, timeout = 1)

    #convert REST to sourcetype
    sourcetype_converted = conversion_dict[rest_path]

    #Get the data
    data = s.get(rest_url, headers = headers, verify = False, timeout = 1)
    # sourcetype_name = "unifi - "+helper.get_arg("rest_endpoint")
    if data.status_code == 404:
        payload=f"ERROR: 404 accessing {helper.get_arg('rest_endpoint')}"
    else:
        payload = data.text

    event = helper.new_event(source=helper.get_input_type(), index=helper.get_output_index(), sourcetype=sourcetype_converted, data=payload)
    ew.write_event(event)
