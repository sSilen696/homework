### Задание 1

- NoSQL тип СУДБ, желательно те кто хранит в json например mongodb
- Реляционная база. Потому что можно сделать схему и установить индексы для более быстрых запросов. Например Постгрес
- Можно как в реляционной базе. Где будет схема, которая будет учитывать наследователькость, поколение. Можно в NoSQL используя документы. где будут документы содержащие всю информацию (о родителях и детях)
- NoSQL, вида ключ-значение, базы для кеширования. Например Reddis 
- Реляционная база. Например MySQL. позволяет иметь базу объектов с которыми будет взаимодействовать покупатель. Наполнять корзину, id объектами, по которым будет легко и быстро выстраиваеться в корзине другие значение (цена, количество. Проверки на наличие, время доставки и другие переменные)

### Задание 2


- так как нам не нужна согласованость, по CAP схеме используем PA, PA\EC потому что  в случае когда нету разделение он работает по предыдущей схему, но в случае разделения, он стремиться все равно согласоваться поэтому в сторону латенси он не смотрит
- Так как система может разделиться тут ненужна разделеность то CA, PA\EL потому что в случае разрыва важнее доступность, иначе скорость ответа (т.к. данные могут разделиться)
- Так как в системе могут быть не солгалованные данные или сбросить соединения тут нету доступности то PC, PC\EL D в случае разрыва он ведет так же, важны данные поэтому может сбросить соединение до  тех пор пока данные не появятся, иначе высокая доступность.


### Задание 3

Думаю в одной СУБД могут быть принципы и ASID и BASE, но абсолютно отвечать как под один принцип так и под другой принцип нельзя. Возможно совмещать одни функции с другими, но не все разом. Хороший пример MySQL. 

### Задание 4

Два главных вопрос, реализация очередей и Асинхроность

т.е. как будут решаться вопросы, очереди сообщений, когда подписчик посылает системе сообщение,  
далее что будет если читатель не успеет обработать предыдущее сообщение. Что будет если читатель не получит сообщение  
Как поведет система, если один читатель будет долго обработать. В зависимости от каждой релиазиции данных субд проблема решается по своему. 