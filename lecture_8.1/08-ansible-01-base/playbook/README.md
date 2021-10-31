# Самоконтроль выполненения задания

1. /playbooks/group_vars/all/example.yml
2. ansible-playbooks site.yaml inventory/test.yaml
3.  ansible-vault encrypt group_vars/el/examp.yml
4.  ansible-vault encrypt group_vars/el/examp.yml
5.  ansible-vault edit group_vars/el/examp.yml
6. ansible-playbook -i inventory/prod.yml site.yml --ask-vault-password
7. winrm                          Run tasks over Microsoft's WinRM
8. ansible-doc -t connection ssh
9. ````text
   remote_user
        User name with which to login to the remote server, normally set by the remote_user keyword.
        If no user is supplied, Ansible will let the ssh client binary choose the user as it normally
        [Default: (null)]
        set_via:
          env:
          - name: ANSIBLE_REMOTE_USER
          ini:
          - key: remote_user
            section: defaults
          vars:
          - name: ansible_user
          - name: ansible_ssh_user

        cli:
        - name: user
   ````