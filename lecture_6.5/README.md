### Задние 1

```dockerfile
FROM centos:7

RUN yum update ; \
    yum install -y wget \
    sudo \
    perl-Digest-SHA

RUN wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.13.4-linux-x86_64.tar.gz && \
    wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.13.4-linux-x86_64.tar.gz.sha512 && \
    shasum -a 512 -c elasticsearch-7.13.4-linux-x86_64.tar.gz.sha512 && \
    tar -xzf elasticsearch-7.13.4-linux-x86_64.tar.gz
RUN mkdir /var/lib/nodes && \
    useradd es && \
    chown -R es /var/lib/nodes && \
    chown -R es /elasticsearch-7.13.4
EXPOSE 9200
COPY elasticsearch.yml /elasticsearch-7.13.4/config/

CMD ["sudo", "-u", "es" "/elasticsearch-7.13.4/bin/elasticsearch", "-d"]
```



```json
{
  "name" : "netology_test",
  "cluster_name" : "my-application",
  "cluster_uuid" : "cnOXDCpWQrGMvJK1ihewLw",
  "version" : {
    "number" : "7.13.4",
    "build_flavor" : "default",
    "build_type" : "tar",
    "build_hash" : "c5f60e894ca0c61cdbae4f5a686d9f08bcefc942",
    "build_date" : "2021-07-14T18:33:36.673943207Z",
    "build_snapshot" : false,
    "lucene_version" : "8.8.2",
    "minimum_wire_compatibility_version" : "6.8.0",
    "minimum_index_compatibility_version" : "6.0.0-beta1"
  },
  "tagline" : "You Know, for Search"
}
```


### Задание 2
```shell
ssilen@Andreys-Mac-mini ~ % curl -X GET 'http://localhost:9200/_aliases?pretty=true'
{
  "ind-2" : {
    "aliases" : { }
  },
  ".kibana_1" : {
    "aliases" : {
      ".kibana" : { }
    }
  },
  "ind-1" : {
    "aliases" : { }
  },
  "ind-3" : {
    "aliases" : { }
  }
}
ssilen@Andreys-Mac-mini ~ % curl -X GET 'http://localhost:9200/_cat/indices?v'
health status index     uuid                   pri rep docs.count docs.deleted store.size pri.store.size
green  open   ind-1     hG3jXuFiTayZ8ZV-3o5-hg   1   0          0            0       208b           208b
green  open   .kibana_1 D6mOYpObSKqvjzVRfZGCEw   1   0         19           64     41.7kb         41.7kb
yellow open   ind-3     v7Name1MThOyEdMGOyr30A   4   2          0            0       832b           832b
yellow open   ind-2     z_VTRDP0TV2nKRKzUkh4oA   2   1          0            0       416b           416b
ssilen@Andreys-Mac-mini ~ % curl -X GET 'http://localhost:9200/_cluster/health?pretty'
{
  "cluster_name" : "my-application",
  "status" : "yellow",
  "timed_out" : false,
  "number_of_nodes" : 1,
  "number_of_data_nodes" : 1,
  "active_primary_shards" : 8,
  "active_shards" : 8,
  "relocating_shards" : 0,
  "initializing_shards" : 0,
  "unassigned_shards" : 10,
  "delayed_unassigned_shards" : 0,
  "number_of_pending_tasks" : 0,
  "number_of_in_flight_fetch" : 0,
  "task_max_waiting_in_queue_millis" : 0,
  "active_shards_percent_as_number" : 44.44444444444444
}
```
Состояние кластера и нод в жолтом, потмоу что одна нода. Индекс которому не нужны реплики находиться в зеленом состояние. Тем кому нужны реплики в желтом. Отсюда весь кластер в желтом состояние
### Задание 3

```json
PUT /_snapshot/netology_backup
{
  "type": "fs",
  "settings": {
    "location": "/elasticsearch-7.13.4/snapshots",
    "compress": true
  }
}
{
  "acknowledged" : true
}

```
```shell
ssilen@Andreys-Mac-mini ~ % curl -X GET 'http://localhost:9200/_cat/indices?v'
health status index     uuid                   pri rep docs.count docs.deleted store.size pri.store.size
green  open   test      n-60L9a2SoaojZNzr2OS9g   1   0          0            0       208b           208b
green  open   .kibana_1 sk3S9PNqQpuNnuFcSJOw8g   1   0         20            2       33kb           33kb
[root@2b2404f066fc /]# ll /elasticsearch-7.13.4/snapshots/
total 28
-rw-r--r-- 1 es es  755 Jul 28 12:08 index-0
-rw-r--r-- 1 es es    8 Jul 28 12:08 index.latest
drwxr-xr-x 4 es es 4096 Jul 28 12:08 indices
-rw-r--r-- 1 es es 8694 Jul 28 12:08 meta-ueCBFiv5SqKiQ2PM8XICZQ.dat
-rw-r--r-- 1 es es  354 Jul 28 12:08 snap-ueCBFiv5SqKiQ2PM8XICZQ.dat

ssilen@Andreys-Mac-mini ~ % curl -X GET 'http://localhost:9200/_aliases?pretty=true'
{
  ".kibana_1" : {
    "aliases" : {
      ".kibana" : { }
    }
  },
  "test-2" : {
    "aliases" : { }
  }
}
```
Восстановление вот так POST /_snapshot/netology_backup/snapshot_1/_restore

```json
ssilen@Andreys-Mac-mini ~ % curl -X GET 'http://localhost:9200/_aliases?pretty=true'
{
  ".kibana_1" : {
    "aliases" : {
      ".kibana" : { }
    }
  },
  "test-2" : {
    "aliases" : { }
  },
  "test" : {
    "aliases" : { }
  }
}
```


