### Задание 1

Изначальная установка была с CNI Calico

```shell
[root@master ~]# kubectl create ns policy-my
namespace/policy-my created
[root@master ~]# kubectl create deployment --namespace=policy-my nginx --image=nginx
deployment.apps/nginx created
[root@master ~]# kubectl expose --namespace=policy-my deployment nginx --port=80
service/nginx exposed
[root@master ~]# kubectl run --namespace=policy-my access --rm -ti --image busybox /bin/sh
If you don't see a command prompt, try pressing enter.
/ # wget -q nginx -O -
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
html { color-scheme: light dark; }
body { width: 35em; margin: 0 auto;
font-family: Tahoma, Verdana, Arial, sans-serif; }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
/ #
[root@master ~]# calicoctl get nodes
NAME
master
node1
node2
node3
node4

[root@master ~]# calicoctl get ipPool
NAME           CIDR             SELECTOR
default-pool   10.233.64.0/18   all()

[root@master ~]# calicoctl get profile
NAME
projectcalico-default-allow
kns.default
kns.kube-node-lease
kns.kube-public
kns.kube-system
kns.policy-my
ksa.default.default
ksa.kube-node-lease.default
ksa.kube-public.default
ksa.kube-system.attachdetach-controller
ksa.kube-system.bootstrap-signer
ksa.kube-system.calico-kube-controllers
ksa.kube-system.calico-node
ksa.kube-system.certificate-controller
ksa.kube-system.clusterrole-aggregation-controller
ksa.kube-system.coredns
ksa.kube-system.cronjob-controller
ksa.kube-system.daemon-set-controller
ksa.kube-system.default
ksa.kube-system.deployment-controller
ksa.kube-system.disruption-controller
ksa.kube-system.dns-autoscaler
ksa.kube-system.endpoint-controller
ksa.kube-system.endpointslice-controller
ksa.kube-system.endpointslicemirroring-controller
ksa.kube-system.ephemeral-volume-controller
ksa.kube-system.expand-controller
ksa.kube-system.generic-garbage-collector
ksa.kube-system.horizontal-pod-autoscaler
ksa.kube-system.job-controller
ksa.kube-system.kube-proxy
ksa.kube-system.namespace-controller
ksa.kube-system.node-controller
ksa.kube-system.nodelocaldns
ksa.kube-system.persistent-volume-binder
ksa.kube-system.pod-garbage-collector
ksa.kube-system.pv-protection-controller
ksa.kube-system.pvc-protection-controller
ksa.kube-system.replicaset-controller
ksa.kube-system.replication-controller
ksa.kube-system.resourcequota-controller
ksa.kube-system.root-ca-cert-publisher
ksa.kube-system.service-account-controller
ksa.kube-system.service-controller
ksa.kube-system.statefulset-controller
ksa.kube-system.token-cleaner
ksa.kube-system.ttl-after-finished-controller
ksa.kube-system.ttl-controller
ksa.policy-my.default

[root@master ~]# kubectl get pods --all-namespaces
NAMESPACE     NAME                                       READY   STATUS    RESTARTS      AGE
kube-system   calico-kube-controllers-58dfb4874f-lwg49   1/1     Running   1 (39m ago)   39m
kube-system   calico-node-65sp6                          1/1     Running   0             40m
kube-system   calico-node-9tbhg                          1/1     Running   0             40m
kube-system   calico-node-bdwg8                          1/1     Running   0             40m
kube-system   calico-node-kjfvj                          1/1     Running   0             40m
kube-system   calico-node-lknr7                          1/1     Running   0             40m
kube-system   coredns-76b4fb4578-4q4bg                   1/1     Running   0             38m
kube-system   coredns-76b4fb4578-j58pc                   1/1     Running   0             39m
kube-system   dns-autoscaler-7979fb6659-t27tq            1/1     Running   0             38m
kube-system   kube-apiserver-master                      1/1     Running   1             42m
kube-system   kube-controller-manager-master             1/1     Running   1             42m
kube-system   kube-proxy-84mhm                           1/1     Running   0             41m
kube-system   kube-proxy-ct7tg                           1/1     Running   0             41m
kube-system   kube-proxy-d8bt9                           1/1     Running   0             41m
kube-system   kube-proxy-nnp5q                           1/1     Running   0             41m
kube-system   kube-proxy-vfj2m                           1/1     Running   0             41m
kube-system   kube-scheduler-master                      1/1     Running   1             42m
kube-system   nginx-proxy-node1                          1/1     Running   0             41m
kube-system   nginx-proxy-node2                          1/1     Running   0             41m
kube-system   nginx-proxy-node3                          1/1     Running   0             41m
kube-system   nginx-proxy-node4                          1/1     Running   0             41m
kube-system   nodelocaldns-b4j86                         1/1     Running   0             38m
kube-system   nodelocaldns-cwpf2                         1/1     Running   0             38m
kube-system   nodelocaldns-jzc7j                         1/1     Running   0             38m
kube-system   nodelocaldns-nmgfr                         1/1     Running   0             38m
kube-system   nodelocaldns-wc5hp                         1/1     Running   0             38m
policy-my     nginx-85b98978db-bmkt5                     1/1     Running   0             4m43s

```