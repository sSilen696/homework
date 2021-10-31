### Задание 1
```shell
mysql> status
--------------
mysql  Ver 8.0.25 for Linux on x86_64 (MySQL Community Server - GPL)

Connection id:		30
Current database:	test_db
Current user:		root@localhost
SSL:			Not in use
Current pager:		stdout
Using outfile:		''
Using delimiter:	;
Server version:		8.0.25 MySQL Community Server - GPL
Protocol version:	10
Connection:		Localhost via UNIX socket
Server characterset:	utf8mb4
Db     characterset:	utf8mb4
Client characterset:	latin1
Conn.  characterset:	latin1
UNIX socket:		/var/run/mysqld/mysqld.sock
Binary data as:		Hexadecimal
Uptime:			4 hours 2 min 58 sec

Threads: 2  Questions: 153  Slow queries: 0  Opens: 231  Flush tables: 3  Open tables: 149  Queries per second avg: 0.010
mysql> SHOW tables;
+-------------------+
| Tables_in_test_db |
+-------------------+
| orders            |
+-------------------+
1 row in set (0.01 sec)
mysql> select * from orders where price > 300;
+----+----------------+-------+
| id | title          | price |
+----+----------------+-------+
|  2 | My little pony |   500 |
+----+----------------+-------+
1 row in set (0.00 sec)

```


### Задание 2


```shell
mysql> SELECT * FROM INFORMATION_SCHEMA.USER_ATTRIBUTES where USER='test';
+------+-----------+---------------------------------------+
| USER | HOST      | ATTRIBUTE                             |
+------+-----------+---------------------------------------+
| test | localhost | {"fname": "JAMES", "sname": "PRETTY"} |
+------+-----------+---------------------------------------+
1 row in set (0.00 sec)
```
Запрос На добавление:
```shell
CREATE USER 'test'@'localhost' 

IDENTIFIED WITH mysql_native_password by 'test-pass' PASSWORD EXPIRE INTERVAL 180 DAY FAILED_LOGIN_ATTEMPTS 3
 ATTRIBUTE '{"fname": "JAMES", "sname": "PRETTY"}';
 
 mysql> GRANT SELECT ON * TO test@localhost;
Query OK, 0 rows affected, 1 warning (0.02 sec)

```

### Задание 3

```shell
mysql> SHOW TABLE STATUS ;
+-------------+--------+---------+------------+------+----------------+-------------+-----------------+--------------+-----------+----------------+---------------------+---------------------+------------+--------------------+----------+----------------+---------+
| Name        | Engine | Version | Row_format | Rows | Avg_row_length | Data_length | Max_data_length | Index_length | Data_free | Auto_increment | Create_time         | Update_time         | Check_time | Collation          | Checksum | Create_options | Comment |
+-------------+--------+---------+------------+------+----------------+-------------+-----------------+--------------+-----------+----------------+---------------------+---------------------+------------+--------------------+----------+----------------+---------+
| copy_orders | MyISAM |      10 | Dynamic    |    5 |           3276 |       16384 |               0 |            0 |         0 |              6 | 2021-07-20 16:54:59 | 2021-07-20 16:54:14 | NULL       | utf8mb4_0900_ai_ci |     NULL |                |         |
| orders      | InnoDB |      10 | Dynamic    |    5 |           3276 |       16384 |               0 |            0 |         0 |              6 | 2021-07-19 16:41:31 | 2021-07-19 16:41:31 | NULL       | utf8mb4_0900_ai_ci |     NULL |                |         |
+-------------+--------+---------+------------+------+----------------+-------------+-----------------+--------------+-----------+----------------+---------------------+---------------------+------------+--------------------+----------+----------------+---------+
2 rows in set (0.01 sec)
mysql> INSERT INTO orders VALUES (6, 'Witcher', 150);
Query OK, 1 row affected (0.01 sec)

mysql> INSERT INTO copy_orders VALUES (6, 'Witcher', 150);
Query OK, 1 row affected (0.01 sec)
|       10 | 0.01063475 | INSERT INTO orders VALUES (6, 'Witcher', 150)      |
|       11 | 0.01558700 | INSERT INTO copy_orders VALUES (6, 'Witcher', 150)
```
Отсюда видно что запрос на запись в MyISAM в полтора раза дольше чем в InnoDB


### Задание 4
```text
[mysqld]
pid-file        = /var/run/mysqld/mysqld.pid
socket          = /var/run/mysqld/mysqld.sock
datadir         = /var/lib/mysql
secure-file-priv= NULL

innodb_file_per_table=1
innodb_log_buffer_size = 100M
innodb_buffer_pool_size = 1M
query_cache_size = 30%
innodb_flush_method = O_DSYNC
innodb_flush_log_at_trx_commit = 2 
```

Полный файл рядом