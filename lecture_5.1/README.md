### Задание 1
1. Паравертуализация позволяет использовать разные ОС, тогда как виртуализация на основе ОС позволяет использовать только конкретную ОС (или приходиться эмулировать)
2. В Паравиртаулизации требуется гипервизор. 
3. В паравиртуализации на одном сервере может быть много компонентов, тогда когда виртуализация на основе ОС подразумевает архитектуру микросервисов (каждый сервис на своем отельном контейнере)
4. Виртуализация на основе ОС требует меньше системных ресурсов, т.к. не приходиться держать полноценную ОС


### Задание 2

* Высоконагруженная база данных, чувствительная к отказу. Кластер из физических серверов с подключенной СХД. Причина, раз база данных высоконагруженная то нужны большие ресурсы. Тратить ресурсы на виртуализацию необходимости нет. 
* Различные Java-приложения. Виртуализация уровня ОС. Каждое java приложение можно запихнуть в отдельный контейнер. тем самым они не будут мешать друг другу и можно легко сделать взаимодействие между ними. Так же мы не будем тратить много ресурсов в отличие от паравиртуализации. 
* Windows системы для использования бухгалтерским отделом. Т.к. это Windows, то лучше использовать паравиртуализацию. Там можно будет использовать отдельный терминальный сервер. Отдельные сервера для других приложений, баз и так далее. Это позволит использовать нужные нам ОС, тогда как сам бехгалтерский отдел будет работать с Windows
* Системы, выполняющие высокопроизводительные расчеты на GPU. Либо физические сервера, либо контейниризация. От виртуализации придеться отказаться потому что из за гипервизора, может упасть производительность системы.

### Задание 3


Да можно совмещать Разные типы виртуализации. К Примеру на одном физическом хосте паравиртуализации можно разместить контейнейры который будут мониторить состояние других виртуальных машин. Так же можно койнтейнера запускать в виртуальных машинах.


#### Скажите, чем паравиртуализация отличается от других виртуальных машин с гипервизорами? Например, от ESX?  

Паравиртуализация это некоторый апгрейд программной виртуализации. Там требовалось изменение ядра системы, что бы вызовы от гостевых машин посылались не ядру, а сразу на гипервизор. 
Сейчас преимуществено используется аппаратная виртуализация. Т.к. у неё больше производительность. 
 ESX это апратная виртуализация от VMware которая устанавливалось прямо на железо. 
Если детально сравнить, То в случае ESX гипервизор посылает команды сразу на железо, а паравиртуализая на гипервизор посылает на отдельные модули виртуализации которые в обход ядра ОС посылают команды на железо.