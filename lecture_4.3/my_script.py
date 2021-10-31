#!/usr/bin/env python3

import subprocess
from typing import List

import json
import yaml

service_names = ["drive.google.com", "mail.google.com", "google.com"]
list_ip_now: list[str] = []
dict_ip_now = dict()
dict_ip_old = dict()
list_ip_old = []
trigger = 0
#with open('base.json')
with open('base.json', 'r') as f:
    dict_ip_old = json.load(f)
#f.close()
for service_name in service_names:
    tmp_stdout = subprocess.check_output(['/usr/bin/host', service_name], encoding='utf-8')
    ip_now = []
    for tmp_string in tmp_stdout.split('\n'):
        list_ip_now.append( tmp_string.split(' ')[-1])
    dict_ip_now[service_name] = list_ip_now
    list_ip_now.pop()

for service_name in service_names:
    if dict_ip_now[service_name] != dict_ip_old[service_name]:
        trigger = 1

if trigger == 1
    with open('base.json', 'w') as f:
        json.dump(dict_ip_now, f, indent=4)

    with open("base.yaml", 'w') as f:
        yaml.dump(dict_ip_now, stream=f, default_flow_style=False)