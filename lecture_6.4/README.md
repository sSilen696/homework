### Задание 1

- \l list databse
- \c connect to database
- \dt  all , \dt *name_of_cheme*.*
- \dt+
- \q quit


### Задание 2

```shell

test_database=# select * from pg_stats where tablename='orders';
 schemaname | tablename | attname | inherited | null_frac | avg_width | n_distinct | most_common_vals | most_common_freqs |                                                                 histogram_bounds                                                                  | co
rrelation | most_common_elems | most_common_elem_freqs | elem_count_histogram
------------+-----------+---------+-----------+-----------+-----------+------------+------------------+-------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+---
----------+-------------------+------------------------+----------------------
 public     | orders    | id      | f         |         0 |         4 |         -1 |                  |                   | {1,2,3,4,5,6,7,8}                                                                                                                                 |
        1 |                   |                        |
 public     | orders    | title   | f         |         0 |        16 |         -1 |                  |                   | {"Adventure psql time",Dbiezdmin,"Log gossips","Me and my bash-pet","My little database","Server gravity falls","WAL never lies","War and peace"} |  -
0.3809524 |                   |                        |
 public     | orders    | price   | f         |         0 |         4 |     -0.875 | {300}            | {0.25}            | {100,123,499,500,501,900}                                                                                                                         |
0.5952381 |                   |                        |
(3 rows)
```

Из которого берем avg_width нужное нам titile

### Задание 3
```shell
test_database=# create table orders_1 as
select * from orders where price > 499;
SELECT 3
test_database=# create table orders_2 as
select * from orders where price <= 499;
SELECT 5
```
Можно было изначально спроектировать таблицу с секционированием
как то так

CREATE TABLE orders (
id int NOT NULL primary,
TITLE character varying(80),
price int,
) PARTITION BY RANGE (price);

### Задание 4

сделать дамп можно так  
pg_dump -U postgres -p5432 test_database > 1.sql  
что бы поменять сделать изменение в дампе, добавить уникальность. В директиве CREATE TABLE public.orders (или аналогичной)  
добавляем в конец UNIQUE(title) 