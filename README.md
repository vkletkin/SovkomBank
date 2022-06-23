# SovkomBank
Были выполнены пункты: 
1)Вывести самый популярный (продаваемый) и самый не популярный товар за последние 2 месяца.
Результат: одна строка; поля: популярный товар, не популярный товар.

2)1. Модели
Модель данных в БД описана выше (товары, продажи). 
Каждая модель может содержать дополнительные поля на усмотрение кандидата. Могут быть введены дополнительные модели. 

3)а) Страница авторизации
Авторизация заранее созданного пользователя, без возможности регистрации новых пользователей. После авторизации переходим на страницу просмотра информации о продажах. (Дополнительно добавил регистрацию)

4)в) Страница просмотра товаров
Таблица содержит поля модели «Товары» (за исключением идентификатора) и дополнительно указано количество и сумма выручки по каждому товару за текущий календарный месяц. Редактирование данных товаров не требуется.


Тестовое задание:
Имеем следующую модель данных:
Таблица с товарами:
 - идентификатор 
 - наименование 
- стоимость
Таблица с информацией о продажах:
- Дата продажи
- Товар
- Количество товара (в штуках)
Связь между таблицами товары и продажи один ко многим.
 Подготовить скрипты по каждой из задач ниже:
1. Вывести самый популярный (продаваемый) и самый не популярный товар за последние 2 месяца.
Результат: одна строка; поля: популярный товар, не популярный товар.

2. Вывести 3 товара с максимальной разницей дней между продажами за всю историю.
Результат: 3 строки; поля: наименование товара, дата продажи, дата предыдущей продажи,
кол-во дней между продажами 

3. Написать небольшое веб-приложение на Python Django, соответствующее описанному ниже техническому заданию, и выложить результат в GitHub в публичный репозиторий.
Техническое задание:
1. Модели
Модель данных в БД описана выше (товары, продажи). 
Каждая модель может содержать дополнительные поля на усмотрение кандидата. Могут быть введены дополнительные модели. 
2. Интерфейс
Необходимо реализовать минимальный интерфейс для просмотра и редактирования моделей. Желательно в качестве фреймворка использовать Bootstrap. Необходимо реализовать следующие страницы:

а) Страница авторизации
Авторизация заранее созданного пользователя, без возможности регистрации новых пользователей. После авторизации переходим на страницу просмотра информации о продажах.

б) Страница просмотра и редактирования информации о продажах.
Информация представлена в виде таблицы, содержащей дату, наименование товара, кол-во, сумму продажи и доп. поля на усмотрение кандидата. Доступные опции:
– Редактирование информации (строки) – переход на новую страницу на базе формы;
– Добавление информации о продажи товара – переход на новую страницу на базе формы;
– Скрыть информацию о продажах за дату – кнопка визуально скрывает данные о продажах за целый день со страницы без сохранения изменений в БД. После перезагрузки данные снова отображается на странице. 

Визуальное размещение элементов на странице на усмотрение кандидата. В верху страницы кнопка для перехода на страницу с перечнем товаров.

в) Страница просмотра товаров
Таблица содержит поля модели «Товары» (за исключением идентификатора) и дополнительно указано количество и сумма выручки по каждому товару за текущий календарный месяц. Редактирование данных товаров не требуется.

3. Покрытие тестами (дополнительно, если останется время)
Написать по 1-2 теста на каждую сущность Django: модель, форма и вью.

По выбору дополнительных пакетов для Django ограничений нет.

Срок 1-2д.
