### Задание 1

Т.к. нет требований по дисковому пространству беру примерные цифры из головы
Коэфициент надежности 1.5 (если выйдет из строя одна нода)

База данных:  

 Ресурсы | 1 копия| кол-во копий | Коэфициент надежности | Итого 
 --- | --- | --- | --- | ---|
Озу | 4gb | 3 | 1.5 |  18gb|
CPU| 1core| 3 | 1.5| 4.5 core |
HDD| 20gb| 3| 1.5| 90gb|

Cache:

 Ресурсы | 1 копия| кол-во копий | Коэфициент надежности | Итого 
 --- | --- | --- | --- | ---|
Озу | 4gb | 3 | 1.5 |  18gb|
CPU| 1core| 3 | 1.5| 4.5 core |
HDD| 20gb| 3| 1.5| 90gb|

frontend:

 Ресурсы | 1 копия| кол-во копий | Коэфициент надежности | Итого 
 --- | --- | --- | --- | ---|
Озу | 50mb | 5 | 1.5 |  375mb|
CPU| 0.2 core| 5 | 1.5| 1.5 core |
HDD| 1gb| 5| 1.5| 7.5gb|

backend

 Ресурсы | 1 копия| кол-во копий | Коэфициент надежности | Итого 
 --- | --- | --- | --- | ---|
Озу | 600mb | 10 | 1.5 |  9000mb|
CPU| 1core| 10 | 1.5| 15 core |
HDD| 1gb| 5| 1.5| 7.5gb|


Общий итог для сервиса   
RAM 18gb + 18gb + 375mb + 900mb = 18432 + 18432 + 375 + 9000 = 46239mb = 45.155gb  
CPU 4.5+4.5+1.5+15=25.5  
HDD 90+90+7.5+7.5=195

Предполагаю что три рабочих ноды справятся с такой нагрузкой. Так же предлагаю контрольные ноды вынести отдельно, в итоге получаем 6 нод.

Ресурсы для ОС  
1 CPU, 1gb RAM, 10gb  
Ресурсы контроль ноды  
2 cpu, 2gb RAM, 100gb  
Ресурсы рабочей ноды  
1 cpu, 1gb RAM, 100gb

Итого нам нужно для контрл ноды: 
3 CPU, 3 gb RAM, 110gb
для рабочих нод нам нужно (с округлением)
10 CPU , 17gb, 200gb