### Задание 1

```dockerfile
version: '3.9'

volumes:
  pg_project:

services:
  pg_db:
    image: postgres
    restart: always
    environment:
      - POSTGRES_PASSWORD=secret
      - POSTGRES_USER=postgres
      - POSTGRES_DB=test
    volumes:
      - ./pg_project:/var/lib/postgresql/data
      - ./pg_backup:/tmp/pg_backup
    ports:
      - "${POSTGRES_PORT:-5433}:5432"
```

### Задание 2

Список бд:
```shell
test_db=# \l
                                     List of databases
   Name    |  Owner   | Encoding |  Collate   |   Ctype    |       Access privileges        
-----------+----------+----------+------------+------------+--------------------------------
 postgres  | postgres | UTF8     | en_US.utf8 | en_US.utf8 | 
 template0 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres                   +
           |          |          |            |            | postgres=CTc/postgres
 template1 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres                   +
           |          |          |            |            | postgres=CTc/postgres
 test      | postgres | UTF8     | en_US.utf8 | en_US.utf8 | 
 test_db   | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =Tc/postgres                  +
           |          |          |            |            | postgres=CTc/postgres         +
           |          |          |            |            | "test-admin-user"=CTc/postgres
(5 rows)

```
описание таблиц
```shell
test_db=# \d+ orders
                                       Table "public.orders"
   Column   |     Type     | Collation | Nullable | Default | Storage  | Stats target | Description 
------------+--------------+-----------+----------+---------+----------+--------------+-------------
 id         | integer      |           | not null |         | plain    |              | 
 trade_name | text         |           |          |         | extended |              | 
 price      | integer      |           |          |         | plain    |              | 
Indexes:
    "orders_pkey" PRIMARY KEY, btree (id)
Referenced by:
    TABLE "clients" CONSTRAINT "clients_number_order_fkey" FOREIGN KEY (number_order) REFERENCES orders(id)
Access method: heap

test_db=# \d+ clients
                                        Table "public.clients"
    Column    |     Type     | Collation | Nullable | Default | Storage  | Stats target | Description 
--------------+--------------+-----------+----------+---------+----------+--------------+-------------
 id           | integer      |           | not null |         | plain    |              | 
 second_name  | text         |           |          |         | extended |              | 
 country      | text         |           |          |         | extended |              | 
 number_order | integer      |           |          |         | plain    |              | 
Indexes:
    "clients_pkey" PRIMARY KEY, btree (id)
    "country" btree (country)
Foreign-key constraints:
    "clients_number_order_fkey" FOREIGN KEY (number_order) REFERENCES orders(id)
Access method: heap
```

проверка пользователей

```shell
SELECT table_catalog, table_schema, table_name, privilege_type, grantee                                                                             
FROM information_schema.table_privileges  
WHERE table_name = 'orders';

 table_catalog | table_schema | table_name | privilege_type |     grantee      
---------------+--------------+------------+----------------+------------------
 test_db       | public       | orders     | INSERT         | postgres
 test_db       | public       | orders     | SELECT         | postgres
 test_db       | public       | orders     | UPDATE         | postgres
 test_db       | public       | orders     | DELETE         | postgres
 test_db       | public       | orders     | TRUNCATE       | postgres
 test_db       | public       | orders     | REFERENCES     | postgres
 test_db       | public       | orders     | TRIGGER        | postgres
 test_db       | public       | orders     | INSERT         | test-admin-user
 test_db       | public       | orders     | SELECT         | test-admin-user
 test_db       | public       | orders     | UPDATE         | test-admin-user
 test_db       | public       | orders     | DELETE         | test-admin-user
 test_db       | public       | orders     | TRUNCATE       | test-admin-user
 test_db       | public       | orders     | REFERENCES     | test-admin-user
 test_db       | public       | orders     | TRIGGER        | test-admin-user
 test_db       | public       | orders     | INSERT         | test-simple-user
 test_db       | public       | orders     | SELECT         | test-simple-user
 test_db       | public       | orders     | UPDATE         | test-simple-user
 test_db       | public       | orders     | DELETE         | test-simple-user
(18 rows)
```


В предыдущем ответе есть спсико пользователей над таблицей

### Задание 3

```shell

test_db=# select count(*) from orders;
 count 
-------
     5
(1 row)

test_db=# select count(*) from clients;
 count 
-------
     5
(1 row)

test_db=# 
```

### Задание 4


```shell

UPDATE public.clients SET
number_order = '5'::integer WHERE
id = 3;
UPDATE public.clients SET
number_order = '4'::integer WHERE
id = 2;
UPDATE public.clients SET
number_order = '3'::integer WHERE
id = 1;
```
так же вместе id можно использовать 'second_name'

### Задание 5

```shell
test_db=# explain select * from clients where id>'0';
                                 QUERY PLAN                                  
-----------------------------------------------------------------------------
 Bitmap Heap Scan on clients  (cost=6.24..19.62 rows=270 width=72)
   Recheck Cond: (id > 0)
   ->  Bitmap Index Scan on clients_pkey  (cost=0.00..6.18 rows=270 width=0)
         Index Cond: (id > 0)
(4 rows)
```
как понимаю это расшифровка всего запроса, он сначала сканирует таблицу клиент, написал какое количество записей проверил с определенной ценой. следующий момент он проверил условие.

### Задние 6

pg_dumpall -U postgres -p 5432 > /tmp/pg_backup
psql -U postgres -p5432 -f /tmp/pg_backup