### Задача 1


1. Высоконагруженное приложение можно оформить как в контейнере так и на виртуальной машине. Если приложение одно, то профита от докера будет не так много.
2. Go-микросервис преимущество у докера, т.к. он будет брать данные из базы и выдавать в какой то вывод результат (отчеты)
3. Думаю лучше подойдет докер. Если приложение одно и не будет хранить в себе данные то докер. 
4. Два контейнера для Android и Ios версии каждое в своем контейнере. У мобильного приложения постоянных данных нет и логи с конфигами можно вынести отдельно.
5. докер контейнер. Кеш не важен и не является данными нужными для сохранения
6. Если я правильно понимаю что такое 'шинна данных для Apache Kafka' (Это узел обрабокт данных для БД кафка) то подойдет докер контейнер. Если данные хроняться на другом узле (брокере?)
7. Предполагаю, можно засунуть reddis в docker контейнер подключив внешнее хранилище (на случай перезапуска контейнера, чтобы не потерять очередь) Очередь как Кеш, е> не нужно хранить всю, что выполнено можно чистить.
8. Как понимаю структуру. мы можем расположить logstah и kibana в докер контейнер а базу elasticsearch в вирталку
9. grafanu и prometeus в отдельные контейнера с конфигом на внешнем хранилище. Место хранение данных для прометея подключаем так же на внешнем хранилище
10. Виртуальная машина, т.к. не очень хорошо хранить базу с данными в контейнере.
11. jenkins для CI поэтому данных хранить не будет в себе и можно закинуть в контейнер. 


### Задача 2
https://hub.docker.com/repository/docker/ssilen696/repo_for_test/general

### Задача 3

ssilen@Andreys-Mac-mini info % docker exec -ti test-centos bash  
[root@e4cc8c63aba1 /]# echo "This is first string!" > /share/info/first_file  
[root@e4cc8c63aba1 /]# exit  
exit  
ssilen@Andreys-Mac-mini info % ll  
total 8  
drwxr-xr-x  3 ssilen  staff    96B 22 июн 23:28 .  
drwxr-xr-x  4 ssilen  staff   128B 19 июн 16:41 ..  
-rw-r--r--  1 ssilen  staff    22B 22 июн 23:28 first_file  
ssilen@Andreys-Mac-mini info % echo "This is another string!" > second file  
ssilen@Andreys-Mac-mini info % docker exec -ti test-debian bash  
root@83be06845a14:/# ls -lah /info/  
total 12K  
drwxr-xr-x 4 root root  128 Jun 22 20:29 .  
drwxr-xr-x 1 root root 4.0K Jun 22 16:32 ..  
-rw-r--r-- 1 root root   22 Jun 22 20:28 first_file  
-rw-r--r-- 1 root root   28 Jun 22 20:29 second  
root@83be06845a14:/# cat /info/first_file  
This is first string!  
root@83be06845a14:/# cat /info/second  
This is another string file  