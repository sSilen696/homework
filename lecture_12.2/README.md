### Задание 1

```shell
ssilen@Andreys-Mac-mini ~ % kubectl get po
NAME                          READY   STATUS    RESTARTS   AGE
hello-node-6b89d599b9-jg96t   1/1     Running   0          24m
hello-node-6b89d599b9-mcxgt   1/1     Running   0          12s
ssilen@Andreys-Mac-mini ~ %  kubectl get deployment
NAME         READY   UP-TO-DATE   AVAILABLE   AGE
hello-node   2/2     2            2           49m
```


### Задание 2

Просмотр логов

```shell
kubectl logs hello-node-6b89d599b9-jg96t
127.0.0.1 - - [12/May/2022:19:02:26 +0000] "GET / HTTP/1.1" 200 674 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15"
127.0.0.1 - - [12/May/2022:19:02:26 +0000] "GET /favicon.ico HTTP/1.1" 200 639 "http://localhost:8080/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15"
```

### Задание 3
```shell
ssilen@Andreys-Mac-mini ~ % kubectl get po
NAME                          READY   STATUS    RESTARTS   AGE
hello-node-6b89d599b9-6btc2   1/1     Running   0          17m
hello-node-6b89d599b9-jg96t   1/1     Running   0          46m
hello-node-6b89d599b9-l2bsv   1/1     Running   0          17m
hello-node-6b89d599b9-mcxgt   1/1     Running   0          22m
hello-node-6b89d599b9-p6v5x   1/1     Running   0          17m
ssilen@Andreys-Mac-mini ~ % kubectl get deployment
NAME         READY   UP-TO-DATE   AVAILABLE   AGE
hello-node   5/5     5            5           69m
```
