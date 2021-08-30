### Задание 1

#### 1. Найдите, где перечислены все доступные resource и data_source, приложите ссылку на эти строки в коде на гитхабе.
Если правильно понял вопрос, то все resource и data_source находятся в директории /aws
#### 2. Для создания очереди сообщений SQS используется ресурс aws_sqs_queue у которого есть параметр name.

- Конфликтует с "name_prefix" 
  ```text

		"name": {
			Type:          schema.TypeString,
			Optional:      true,
			Computed:      true,
			ForceNew:      true,
			ConflictsWith: []string{"name_prefix"},
		},```
- Максимальная длина имени будет состоять из 2^64 - lenght("name_prefix")
name = naming.Generate(d.Get("name").(string), d.Get("name_prefix").(string))
  
-^[a-zA-Z0-9_-]{1,75}\.fifo$