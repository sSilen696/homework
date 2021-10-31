### Task 1
```text
TASK [Print fact] **********************************************************************************************************************************************************************************************
ok: [localhost] => {
    "msg": 12
}
```
### Task 2
```text
TASK [Print fact] **********************************************************************************************************************************************************************************************
ok: [localhost] => {
    "msg": "all default fact"
}
```
### task 3-4
ok: [centos7] => {
    "msg": "el"
}
ok: [ubuntu] => {
    "msg": "deb"
}
### task 5-6
ok: [centos7] => {
    "msg": "el default fact"
}
ok: [ubuntu] => {
    "msg": "deb default fact"
}
### Task 7-8
```text
ssilen@Andreys-Mac-mini playbook % ansible-vault encrypt group_vars/deb/examp.yml

New Vault password:

Confirm New Vault password:

Encryption successful
ssilen@Andreys-Mac-mini playbook % ansible-vault encrypt group_vars/el/examp.yml

New Vault password:

Confirm New Vault password:

Encryption successful
ssilen@Andreys-Mac-mini playbook % ansible-playbook -i inventory/prod.yml site.yml --ask-vault-password
--ask-vault-password
Vault password:


PLAY [Print os facts] ******************************************************************************************************************************************************************************************

TASK [Gathering Facts] *****************************************************************************************************************************************************************************************
[DEPRECATION WARNING]: Distribution Ubuntu 20.04 on host ubuntu should use /usr/bin/python3, but is using /usr/bin/python for backward compatibility with prior Ansible releases. A future Ansible release will
 default to using the discovered platform python for this host. See https://docs.ansible.com/ansible/2.11/reference_appendices/interpreter_discovery.html for more information. This feature will be removed in
 version 2.12. Deprecation warnings can be disabled by setting deprecation_warnings=False in ansible.cfg.
ok: [ubuntu]
ok: [centos7]

TASK [Print OS] ************************************************************************************************************************************************************************************************
ok: [centos7] => {
    "msg": "CentOS"
}
ok: [ubuntu] => {
    "msg": "Ubuntu"
}

TASK [Print fact] **********************************************************************************************************************************************************************************************
ok: [centos7] => {
    "msg": "el default fact"
}
ok: [ubuntu] => {
    "msg": "deb default fact"
}

PLAY RECAP *****************************************************************************************************************************************************************************************************
centos7                    : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
ubuntu                     : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

### Task 9-11
Новый факт для local не определял, т.к. попадает под default fact
```text
ok: [local] => {
    "msg": "all default fact"
}
ok: [centos7] => {
    "msg": "el default fact"
}
ok: [ubuntu] => {
    "msg": "deb default fact"
}

```