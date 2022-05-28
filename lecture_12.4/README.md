### Задание 1
Проверил куберспрей на яндексоблаке

Устьановка прошла успешно, инвентори файл прикладываю рядом в репозитории.
Проверил в переменных conterd используется по умолчанию

```shell
ssilen@Andreys-Mac-mini kubespray % ansible-playbook -i ./inventory/mycluster/hosts.yml cluster.yml --become --become-user=root --user=ademin
PLAY RECAP ***********************************************************************************************************************************************************
localhost                  : ok=4    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
master                     : ok=769  changed=156  unreachable=0    failed=0    skipped=1306 rescued=0    ignored=8
node1                      : ok=589  changed=123  unreachable=0    failed=0    skipped=826  rescued=0    ignored=2
node2                      : ok=589  changed=123  unreachable=0    failed=0    skipped=825  rescued=0    ignored=2
node3                      : ok=520  changed=105  unreachable=0    failed=0    skipped=778  rescued=0    ignored=1
node4                      : ok=520  changed=105  unreachable=0    failed=0    skipped=778  rescued=0    ignored=1

суббота 28 мая 2022  19:24:51 +0300 (0:00:00.216)       0:22:15.362 ***********
===============================================================================
download : download_container | Download image if required --------------------------------------------------------------------------------------------------- 40.28s
kubernetes/control-plane : kubeadm | Initialize first master ------------------------------------------------------------------------------------------------- 31.95s
kubernetes/kubeadm : Join to cluster ------------------------------------------------------------------------------------------------------------------------- 26.57s
download : download_file | Validate mirrors ------------------------------------------------------------------------------------------------------------------ 25.31s
kubernetes/preinstall : Install packages requirements -------------------------------------------------------------------------------------------------------- 22.77s
etcd : reload etcd ------------------------------------------------------------------------------------------------------------------------------------------- 20.50s
etcd : Gen_certs | Write etcd member and admin certs to other etcd nodes ------------------------------------------------------------------------------------- 18.12s
etcd : Gen_certs | Write etcd member and admin certs to other etcd nodes ------------------------------------------------------------------------------------- 17.76s
kubernetes-apps/ansible : Kubernetes Apps | Start Resources -------------------------------------------------------------------------------------------------- 16.79s
kubernetes-apps/ansible : Kubernetes Apps | Lay Down CoreDNS templates --------------------------------------------------------------------------------------- 14.24s
download : download_container | Download image if required --------------------------------------------------------------------------------------------------- 13.73s
etcd : Gen_certs | Write node certs to other etcd nodes ------------------------------------------------------------------------------------------------------ 13.13s
etcd : Gen_certs | Write node certs to other etcd nodes ------------------------------------------------------------------------------------------------------ 13.05s
network_plugin/calico : Start Calico resources --------------------------------------------------------------------------------------------------------------- 12.97s
download : download_container | Download image if required --------------------------------------------------------------------------------------------------- 12.68s
download : download_container | Download image if required --------------------------------------------------------------------------------------------------- 11.17s
download : download_container | Download image if required --------------------------------------------------------------------------------------------------- 10.60s
download : download_container | Download image if required ---------------------------------------------------------------------------------------------------- 9.11s
kubernetes/preinstall : Preinstall | wait for the apiserver to be running ------------------------------------------------------------------------------------- 8.58s
network_plugin/calico : Calico | Create calico manifests ------------------------------------------------------------------------------------------------------ 8.26s
```