###1. Задание   
При скорости 1гб/с и 300мс RTT TCP windows size 37500

Берем формулу V=W/RTT, где V максимальная скорость (Оно же Throughtput), W замер окна TCP (оно же WSS)  
Исходя из формулы выше получаем формулу  
W = RTT * V  
Имея RTT равному 300 мс (переводим в секунды получаем 0.3)
т.к. Размер окна у нас в Килобайтах, переводим скорость в килобайты
1гб равен 131072 кБ
перемножаем  131072 и 0.3 получаем 39321
ссылка на калькулятор дает рекомендуемый размер, возможно поэтому отличаются.

###2. Задание  
<--! Если расмтривать формулу  Throughput =< MSS / (RTT* sqrt(Ploss))  
то при потерять в 1% Пропускная способность упадет в 10 раз. -->
Немного ошибся должно быть так  
V1 = W / RTT * sqrt(Ploss_zero)  
V2 = W / RTT * sqrt(Ploss)  
т.е. соотношение V1 / V2 = sqrt( Ploss / Ploss_zero )  
, где Ploss = 100% - 1% = 0.99 Ploss_zero = 1  
Т.е. нам нужно найти sqrt(0.99)=0.9949
Т.е. упадет примерно на 0.5%

Theoretical network limit  
rough estimation: rate < (MSS/RTT)*(C/sqrt(Loss)) [ C=1 ] (based on the Mathis et.al. formula)  
network limit (MSS 1460 byte, RTT: 300.0 ms, Loss: 1%) : 0.39 Mbit/sec.  
Bandwidth-delay Product and buffer size
BDP (1000 Mbit/sec, 300.0 ms) = 37.50 MByte   
required tcp buffer to reach 1000 Mbps with RTT of 300.0 ms >= 36621.1 KByte   
maximum throughput with a TCP window of 36621 KByte and RTT of 300.0 ms <= 1000.00 Mbit/sec.  
По калькулятору кажется что потери будут в 2564 раза.  



###3. Задание
Оригинальная конфигурация TCP ограничивает скорость передачи буфером 
(опция Window Size — «размер окна») и является полем размером в 2^16 байт (до 64 КБайт).
Стандартным стеком TCP, максимальная скорость передачи данных не превысит 10 Мбит/сек
( 524288 бит / 0.1 сек = 5.24 Мбит/сек не смотря на то что у вас 100 мегабитный линк).

во всех источниках говориться:  
что максимальный размер окна TCP не превышает 64кБ (если не говорим о RFC1323)
считаем 2^16 = 65536 байт = 524288
Далее предполагаем что средние задержки у нас равны 100мс  
итого:  
(524288 бит / 0.1 сек = 5.24 Мбит/сек не смотря на то что у вас 100 мегабитный линк).

#### Пояснение
Я не совсем правильно понял задание. Первый же запрос выдавал ограничение TCP Window 64kb  
и то что есть расширение rfc1323 (О котором я писал выше) которое расширяет это окно до значение около 1гб  
https://www.ietf.org/rfc/rfc1323.txt Описание даного вопроса.  
Сейчас я понял что нужна была такая формула.  
100Мб/с делим на 1500 и умножаем 1460  
100 000 000 / 8 /1500 * 1460 = 12166666 байт/с  или  97.3Мб/с

Я бы лучше понял, если вы бы попросили посчитать максимальный объем данных способные передать по tcp за 1 минуту при скорости 100мб/с

###4. Задание

1. Для начала Нам нужно узнать адрес сайта. Поэтому опрашиваем наш шлюз знает он ли где находиться netology.ru
2. Шлюз не знает, поэтому опрашивает у известного у него DNS сервера об этом адрессе.
3. DNS сервера по очереди ищут запись у себя, если неизвестно у кого опрашивают те что выше.
Если известно, то направляют к тому кто знает. Так наш Шлюз, и наш компьютер узнают адрес netology.ru
4. Зная адрес, наш ПК хочет отправить туда данные. Но куда туда он не знает, поэтому он еще раз посылает на наш шлюз данные
5. Шлюз не знает полный маршрут до этого сервера, поэтому посылает своему шлюзу до тех пор, пока определный шлюз не будет знать куда посылать.
6. В итоге маршрут для наших пакетов построен и наш ПК дальше формируются пакеты по tcp на порт 80 или 443 (скорее на 443) 

P.S. Каждый раз, когда обращаются к какому IP адресу, если неизвестен его MAC из ARP таблицы, 
будут вызываться ARP Запросы, что бы определить куда направить пакеты.  
P.P.S. Да, наш браузер (или другое приложение работающиее по http) формирует http-запрсы и получает ответы по протоколу http.
###5. Задание

В моем случае мой шлюз являелся тем DNS сервером который знал ответ. Поэтому я сделал для теста запрос к
nslookup -norecurse google.*  
получил вот такой результат. Ни один гугловский домен не ответил на данный флаг. Но на рекурсивный вариант отвечает. 

###6. Задание  
/25 доступно 126 адресов
255.248.0.0 2046 адресов

###7. Задание  
Больше в /23 ровно в два раза (ну или почти) в случае /23 доступно 510, а в случае /24 доступно 254

###8. Задание  
Да получиться, маска будет /15