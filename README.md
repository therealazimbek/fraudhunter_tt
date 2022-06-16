# Тестовое задание FraudHunter Junior Backend
## _Азимбек, Абдипаттаев_

Технические требования
● Django
● PostgreSQL
● Python 3
При выполнении тестового задания Вы можете дополнительно использовать любые
сторонние Python библиотеки, без всяких ограничений. Все 3rd
party Python библиотеки должны быть добавлены в проект через
pip если библиотека поддерживает такой способ установки.

Часть No1 (обязательная)
Создайте API, которая будет выводить иерархию сотрудников.
1. Информация о каждом сотруднике должна храниться в базе данных и
содержать следующие данные:
○ ФИО; ✅
○ Должность; ✅ (здесь  я указал ранк сотрутника чтобы показать иерархию)
○ Дата приема на работу;✅
○ Размер заработной платы;✅
2. У каждого сотрудника есть 1 начальник;✅
3. База данных должна содержать не менее 50 000 сотрудников и 5 уровней
иерархий.✅
4.  Не забудьте отобразить должность сотрудника.✅


Часть No2 (опциональная)
1. Создайте базу данных используя миграции Django.✅
2. Используйте DB seeder для Django ORM для заполнения
базы данных.✅ (создал вручную seed.py, в котором заполнил базу данных)
3. Создайте еще один запрос и отправляйте на ней список сотрудников со всей
имеющейся о сотруднике информацией из базы данных.✅ (использовал команду python manage.py seed для заполниние базу данных)
4. Добавьте возможность поиска сотрудников по любому полю.✅ (можно указать параметры поиска в url)
5. Добавьте возможность сортировать.✅ (также можно указать по какой поле нужно сортировать в url)
6. Осуществите аутентификацию пользователя для
зарегистрированных пользователей. ✅
7. Сделайте функционал разработанный в задачах 3, 4 и 5 доступный только для
зарегистрированных пользователей.✅ (изпользовал djangorestframwork_simplejwt)
8. В разделе доступном только для зарегистрированных пользователей,
реализуйте остальные CRUD операции для записей сотрудников. Пожалуйста
заметьте, что все поля касающиеся пользователей должны быть
редактируемыми, включая начальника каждого сотрудника.✅(авторизованный пользователь может удалить/изменить данные сотрудников)


## Как запустить проект?

Требование
1. Python версии 3.8 или более новые версии
2. Django версии 4.0.5 или более новые
3. DjangoREST Framework 3.13 или более новые
4. Djangorestframework-simplejwt версии 5.2.0 или более новые
5. django-filter~=21.1
6. django-seed==0.3.1

##### А также, в проекте есть файл requirements.txt, откуда можно установить все необходимые библиотеки

```sh
git clone https://github.com/therealazimbek/fraudhunter_tt.git
cd fraudhunter_tt
python manage.py runserver
```

## Как тестировать проект?
1. https://www.postman.com/therealazimbek/workspace/azimbeks/collection/20335173-53c37976-1c5c-4d11-a751-a8b02ee1c832?ctx=documentation можно через postman (у меня вы найдёте базовые api запросы)
2. А также в проекте есть файл Fraudhunter_tt.postman_collection.json откуда можно импортировать в postman
3. Можно также через админку реализовать операции crud/sort/search


#### Aдмин аккаунт:
username: admin
password: admin

## Базы данных
В проекте я использовал postggresql и sqlite3(чтобы было удобно и быстро использовать). Вы можете выбрать какой из них использовать в settings.py. В корневой папке есть dump file postgresql. Если решите использовать postgresql можете из dump file восстановить базу данных. (Подробно об этом: https://www.postgresqltutorial.com/postgresql-administration/postgresql-copy-database/)

# Спасибо за внимение!


[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>

