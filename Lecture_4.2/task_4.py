#!/usr/bin/env python3

import subprocess
from typing import List

service_names = ["drive.google.com", "mail.google.com", "google.com"]
list_ip_now: list[str] = []
dict_ip_now = dict()
list_ip_old = []
f = open('base', 'r')
for tmp_line in f:
    list_ip_old.append([tmp_line.split('-')[0], tmp_line.split('-')[1].replace('\n', '')])

#f.close()
for service_name in service_names:
    tmp_stdout = subprocess.check_output(['/usr/bin/host', service_name], encoding='utf-8')
    for tmp_string in tmp_stdout.split('\n'):
        list_ip_now.append([tmp_string.split(' ')[0], tmp_string.split(' ')[-1]])
    list_ip_now.pop()
for i in range(len(list_ip_now)):
    if list_ip_old[i] != list_ip_now[i]:
        print(f"[ERROR] {list_ip_now[i][0]} IP mismatch: {list_ip_old[i][1]} {list_ip_now[i][1]}")
f = open('base', 'w')
for index in list_ip_now:
    f.write(index[0] + '-' + index[1] + '\n')
f.close()