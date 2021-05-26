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
list_changed = ('modified', 'new file', 'изменено', 'новый файл')
full_dir = result_os.split('\n')[-2]
for result in result_os.split('\n'):
    for now_change in list_changed:
        if result.find(now_change) != -1:
            now_change = '\t' + now_change + ':'
            prepare_result = result.replace(now_change, '')
            prepare_result = full_dir + '/' + prepare_result
            prepare_result = prepare_result.replace('  ', '')
            print(prepare_result)
            break
````

### 3 задание
