### Задание 1

- При обычном сложении получаешь ошибку попытки сложить int и str
- если мы сделаем str(a), то получим 12
- если мы сделаем int(b), то получим 3

### Задание 2
````python
#!/usr/bin/env python3

import os

bash_command = ["cd ~/netology/sysadm-homeworks", "git status", "pwd"]
result_os = os.popen(' && '.join(bash_command)).read()
is_change = False
list_changed = ('modified', 'изменено' )
full_dir = result_os.split('\n')[-2]
for result in result_os.split('\n'):
    for now_change in list_changed:
        if result.find(now_change) != -1:
            now_change = '\t' + now_change + ':'
            prepare_result = result.replace(now_change, '')
            prepare_result = full_dir + '/' + prepare_result
            prepare_result = prepare_result.replace('  ', '')
            print(prepare_result)
````

### 3 задание
```python

#!/usr/bin/env python3

import argparse

import os


parser = argparse.ArgumentParser()
parser.add_argument("--dir")
args = parser.parse_args()
dir = args.dir
if dir == None:
    dir = "~/netology/sysadm-homeworks"

dir = "cd " + dir
temp = dir + ' && ' + 'ls -a | grep .git | wc -l'
test_dir = int(os.popen(temp).read())
if test_dir == 0:
    print(' This directory hasnt git repostitory' )
    quit()
bash_command = [dir, "git status", "pwd"]
result_os = os.popen(' && '.join(bash_command)).read()
is_change = False
list_changed = ('modified', 'изменено')
full_dir = result_os.split('\n')[-2]
for result in result_os.split('\n'):
    for now_change in list_changed:
        if result.find(now_change) != -1:
            now_change = '\t' + now_change + ':'
            prepare_result = result.replace(now_change, '')
            prepare_result = full_dir + '/' + prepare_result
            prepare_result = prepare_result.replace('  ', '')
            print(prepare_result)
            #break
```


### 4 Задание

```python
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
```