### 1 Задание
ssilen@Andreys-Mac-mini ~ % a=1  
ssilen@Andreys-Mac-mini ~ % b=2  
ssilen@Andreys-Mac-mini ~ % c=a+b  
ssilen@Andreys-Mac-mini ~ % echo $c  
a+b Такой вывод потому что мы не брали значение переменных a и b это символы '+' аналогичный символ 
ssilen@Andreys-Mac-mini ~ % d=$a+$b  
ssilen@Andreys-Mac-mini ~ % echo $d  
1+2 здесь мы достали из переменных а и б значение и склеили все в переменой d  
ssilen@Andreys-Mac-mini ~ % e=$(($a+$b))  
ssilen@Andreys-Mac-mini ~ % echo $e  
3  Благодаря скобкам (()) мы смогли экранировать и выполнить арифметическую операцию

### 2 Задание 

Рабочий скрипт будет выглядить так  
;#!/bin/bash  
while [[ 1 == 1 ]]  
do  
curl -s  http://127.0.0.1:19999 > /dev/null  
if [[ $? != 0 ]]; then  
date >> ./curl.log  
fi  
done  
exit  
Для управление предлагаю ввести еще один простенький скрипт  
;#!/bin/bash  

case "$1" in  
        'start')  
        ./error.sh &  
        echo $! > ./pid  
        ;;  
        'stop')  
        kill -9 `cat ./pid`  
        rm -f ./pid  
        ;;  
        *)  
        echo "usage start-stop"  
        ;;  
esac  
exit  

Срипт можно модифицировать дополнительными проверками, и выводом статуса.  

###3 Задание

        #!/bin/bash  

        HOSTS=('192.168.0.1 173.194.222.113 87.250.250.242')  


        for host in $HOSTS; do  
                echo $host >> ./access.log  
                for i in {0..5}; do  
                        nmap -Pn -p 80 $host | grep 80/ | awk '{print $2}' >> ./access.log  
                done  
        done  
        exit  

###4 Задание


        #!/bin/bash

        HOSTS=('192.168.0.1 173.194.222.113 87.250.250.242')


        for host in $HOSTS; do
                echo $host >> ./access.log
                for i in {0..5}; do
                        RESULT=$(nmap -Pn -p 80 $host | grep 80/ | awk '{print $2}')
                        if [[ $RESULT == 'filtered' ]]; then
                                echo  $HOST >> ./error.log
                                exit
                        fi
                        echo $RESULT >> ./access.log
                done
        done
        exit