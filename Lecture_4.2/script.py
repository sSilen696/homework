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