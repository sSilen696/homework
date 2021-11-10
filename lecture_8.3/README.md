### My playbook
Данный playbook устанавливает ElastikSearch, Kibana и filebeat для них.  
В директориях group_vars/elastiksearch.yml находятся параметр Версии приложений.
Так же в плейбуке есть разграничение по тегам:
- filebeat для установки filebeat
- kibana для установки kibana
- elastik для установки elastiksearch

P.S. удачного использования