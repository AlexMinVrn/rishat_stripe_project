# rishat_stripe_project

### Описание
Оплата товаров с помощью сервиса Stripe Payments.
#### >Сервис размещен на сервере Yandex Cloud и доступен по адресу:
#### >http://51.250.66.16/item/1/  
#### >Админка доступна по адресу http://51.250.66.16/admin/  
#### >Пользователь: admin Пароль: admin

### Технологии
- [Python] v3.7
- [Django] v2.2.16
- [Docker]
- Gunicorn
- nginx
### Запуск проекта
### Клонируйте проект и задайте настройки, для этого:

#### Подключитесь к своему серверу
ssh <server user>@<server IP>
Например: ssh root@00.000.00.00

#### Клонируйте проект на сервер:
git@github.com:AlexMinVrn/rishat_stripe_project.git

#### Подготовьте дополнительные данные (.env и nginx.conf):

##### Скопируйте в директорию проекта infra/ файл nginx.conf 

##### В файле nginx.conf в строке server_name укажите данные ip вашего сервера.

##### Создайте в директории проекта infra/ файл .env и наполните его следующими данными
DEBUG=0  
SECRET_KEY=<Длинная строка с латинскими буквами, цифрами и символами>  
STRIPE_PUBLIC_KEY = <Публичный ключ аккаунта Stripe>  
STRIPE_SECRET_KEY = <Секретный ключ аккаунта Stripe>  

#### Подготовьте сервер для работы с проектом:

##### Установите docker и docker-compose:
sudo apt install docker.io  
sudo apt install docker-compose

##### Соберите контейнеры:

sudo docker-compose up -d --build

##### Выполните миграции
sudo docker-compose exec backend python manage.py makemigrations  
sudo docker-compose exec backend python manage.py migrate

##### Создайте суперюзера:
sudo docker-compose exec backend python manage.py createsuperuser

##### Cоберите статику
sudo docker-compose exec backend python manage.py collectstatic --no-input


### Автор
- [Александр Минаев]

[//]: # 
  [Python]: <https://www.python.org>
  [Django]: <https://www.djangoproject.com>
  [Docker]: <https://www.docker.com>
  [Александр Минаев]: <https://github.com/AlexMinVrn>