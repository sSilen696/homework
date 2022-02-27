### Задание 1
Push Удобна для использование динамической среде. Из плюсов,  новые инстансы  могут добавляться автоматом.  
Из минусов, данные передаются в откром виде и есть шанс потерять данные, если принимающий сервер будет отключен.  
Pull наоборот, плохо подходит для динамической среды, но если у тебя статическая сеть, ты знаешь все сервера которые будут обращаться ты можешь добавить все хосты добавить, более высокий контроль метрик, можно избежать потерь данных при отключение сервера мониторинга

### Задание 2

- Prometheus Pull (Думал что push-gateway работает push но прометеус с него все равно забирает pull) 
- TICK PUSH
- Zabbix PULL, Так же у него есть методы push (Активные проверки)
- VictoriaMetrics PUSH
- Nagios PULL

### Задание 3
Скриншоты в репозитории рядом
```sh
ssilen@Andreys-Mac-mini ~ % curl -v http://localhost:9092/kapacitor/v1/ping
*   Trying ::1:9092...
* Connected to localhost (::1) port 9092 (#0)
> GET /kapacitor/v1/ping HTTP/1.1
> Host: localhost:9092
> User-Agent: curl/7.77.0
> Accept: */*
>
* Mark bundle as not supporting multiuse
< HTTP/1.1 204 No Content
< Content-Type: application/json; charset=utf-8
< Request-Id: 252b32f2-97ef-11ec-8f56-000000000000
< X-Kapacitor-Version: 1.6.3
< Date: Sun, 27 Feb 2022 17:03:11 GMT
<
* Connection #0 to host localhost left intact
ssilen@Andreys-Mac-mini ~ % curl -v http://localhost:8086/ping
*   Trying ::1:8086...
* Connected to localhost (::1) port 8086 (#0)
> GET /ping HTTP/1.1
> Host: localhost:8086
> User-Agent: curl/7.77.0
> Accept: */*
>
* Mark bundle as not supporting multiuse
< HTTP/1.1 204 No Content
< Content-Type: application/json
< Request-Id: 8209c0a2-97f1-11ec-9079-0242ac120003
< X-Influxdb-Build: OSS
< X-Influxdb-Version: 1.8.10
< X-Request-Id: 8209c0a2-97f1-11ec-9079-0242ac120003
< Date: Sun, 27 Feb 2022 17:20:06 GMT
<
* Connection #0 to host localhost left intact
ssilen@Andreys-Mac-mini ~ % curl http://localhost:8888 -v
*   Trying ::1:8888...
* Connected to localhost (::1) port 8888 (#0)
> GET / HTTP/1.1
> Host: localhost:8888
> User-Agent: curl/7.77.0
> Accept: */*
>
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< Accept-Ranges: bytes
< Cache-Control: public, max-age=3600
< Content-Length: 336
< Content-Security-Policy: script-src 'self'; object-src 'self'
< Content-Type: text/html; charset=utf-8
< Etag: "33625191427"
< Last-Modified: Tue, 25 Jan 2022 19:14:27 GMT
< Vary: Accept-Encoding
< X-Chronograf-Version: 1.9.3
< X-Content-Type-Options: nosniff
< X-Frame-Options: SAMEORIGIN
< X-Xss-Protection: 1; mode=block
< Date: Sun, 27 Feb 2022 17:21:51 GMT
<
* Connection #0 to host localhost left intact
<!DOCTYPE html><html><head><meta http-equiv="Content-type" content="text/html; charset=utf-8"><title>Chronograf</title><link rel="icon shortcut" href="/favicon.fa749080.ico"><link rel="stylesheet" href="/src.14d28054.css"></head><body> <div id="react-root" data-basepath=""></div> <script src="/src.bb2cd140.js"></script> </body></html>%
ssilen@Andreys-Mac-mini ~ %
```