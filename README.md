# DRF

## Продолжаем проект DRF

### Задание 1

* Подключить и настроить вывод документации для проекта. Убедиться, что каждый из реализованных эндпоинтов описан в
  документации верно, при необходимости описать вручную.

      Для работы с документацией проекта воспользуйтесь библиотекой
      drf-yasg (https://drf-yasg.readthedocs.io/en/stable/) или
      drf-spectacular (https://drf-spectacular.readthedocs.io/en/latest/).
      
      Как вручную можно сформировать документацию в drf-yasg можно почитать по ссылки https://habr.com/ru/articles/733942/,
      в drf-spectacular — тут https://habr.com/ru/articles/733942/ или тут https://drf-spectacular.readthedocs.io/en/latest/customization.html.      

### Задание 2

* Подключить возможность оплаты курсов через https://stripe.com/docs/api. Доступы можно получить напрямую из
  документации, а также пройти простую регистрацию по адресу https://dashboard.stripe.com/register.

  Для работы с учебным проектом достаточно зарегистрировать аккаунт и не подтверждать его — аккаунт будет находиться в
  тестовом режиме.

* Для работы с запросами вам понадобится реализовать обращение к эндпоинтам:

      https://stripe.com/docs/api/products/create — создание продукта;
      https://stripe.com/docs/api/prices/create — создание цены;
      https://stripe.com/docs/api/checkout/sessions/create — создание сессии для получения ссылки на оплату.


* При создании цены и сессии обратите внимание на поля, которые вы передаете в запросе. Внимательно изучите значение
  каждого поля и проанализируйте ошибки при их возникновении, чтобы создать корректную запись.

При создании сессии нужно передавать id цены, которая соответствует конкретному продукту.

* Для тестирования можно использовать номера карт из документации:

      https://stripe.com/docs/terminal/references/testing#standard-test-cards.

### Примечание

      Подключение оплаты лучше всего рассматривать как обычную задачу подключения к стороннему API.

      Основной путь: запрос на покупку → оплата. Статус проверять не нужно.

      Каждый эквайринг предоставляет тестовые карты для работы с виртуальными деньгами.

### Подсказка

      Необходимо связать данные от сервиса платежей со своим приложением. Все взаимодействия с платежным сервисом опишите в
      сервисных функциях. Сервисные функции взаимодействуют с платежным сервисом (Stripe) и отдают ответы в виде JSON. Далее
      результаты работы сервисных функций мы используем в соответствующих View: при создании платежа в нашей системе мы должны
      создать продукт, цену и сессию для платежа в Stripe, сохранить ссылку на оплату в созданном платеже в нашей системе и
      отдать пользователю в ответе на POST-запрос ссылку на оплату или данные о платеже (которые будут включать ссылку на
      оплату).

      При необходимости проверки статуса платежа можно реализовать дополнительную View, которая будет обращаться на Session
      Retrieve (https://stripe.com/docs/api/checkout/sessions/retrieve) по id созданной в Stripe сессии и отдавать
      пользователю данные о статусе платежа. Статус платежа также можно дополнительно хранить в модели платежей в нашей
      системе.

      Перед созданием сессии необходимо создать продукт и цену. Все эти данные мы можем получить из модели платежа (модель
      платежа связана с продуктом, в продукте есть название и цена).

      Обратите внимание, что цены при передаче в Strip указываются в копейках (то есть текущую цену продукта нужно умножить на
      100).

###              * Дополнительное задание

* Реализуйте проверку статуса с помощью эндпоинта https://stripe.com/docs/api/checkout/sessions/retrieve — получение
  данных о сессии по идентификатору.

#### Дополнительное задание, помеченное звездочкой, желательно, но не обязательно выполнять.