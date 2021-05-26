#!/usr/bin/env python3

import argparse

import os


parser = argparse.ArgumentParser()
parser.add_argument("--dir")
args = parser.parse_args()
dir = args.dir
if dir == None:
    dir = "cd ~/netology/sysadm-homeworks"

dir = "cd " + dir
print(dir)
bash_command = ["cd ~/git/homework", "git status", "pwd"]
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