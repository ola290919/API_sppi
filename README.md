# Drone Area Registry Service API

Тесты для сервиса Drone Area Registry, используемого в СППИ

- [Роли](https://docs.google.com/spreadsheets/d/1DFgbV-dRgdI0ARPRAnqC8w505sMK-S36jFZDWbMf2GA/edit?usp=sharing)
- [Репозиторий](https://git.monitorsoft.ru/spppi/drone-area-registry)
- [API документация](https://git.monitorsoft.ru/spppi/drone-area-registry/-/blob/2.0.0-rc.13/spec/v1_openapi.yaml)

## Установка

Перед запуском установить Python 3.12 и выше.

Загрузить все необходимые пакеты через ```pip install -r requirements.txt```.

Необходимые для запуска проекта переменные указаны в файле ```.env.example```.

Генерация локально отчета allure (прописать свой путь) ```C:\Users\mx\Downloads\allure-2.29.0\allure-2.29.0\bin\allure.bat generate allure-results --clean```

Установка переменной java ```$Env:JAVA_HOME = "C:\Program Files\Java\jre1.8.0_421"```

## Запуск

Тесты используют заранее созданных пользователей в системе. Логины и пароли указываются в переменных окружения.

`pytest`

Запуск в jenkins через jenkinsfile

В проекте используются теги (pytest marks) для более удобного запуска тестов, например, для того, чтобы запустить только
тесты, которые проверяют доступ, можно использовать команду `pytest -m access`.

Для запуска в несколько потоков можно использовать `pytest -n 4`, где `-n` - количество потоков.

В pytest.ini заданы параметры запуска с автоматическим созданием отчета allure  `--alluredir allure-results`.

### Структура

```text
/
│
├── models/
│   │── fields/
│   └── ...
│
├── utils/
│   │── api_client.py
│   └── ...
│
├── tests/
│   └── ...
```

В директории [models](models) находятся модели данные, соответствующие моделям в openapi. Для описания и валидации моделей 
используется библиотека [pydantic](https://docs.pydantic.dev/latest/). Вместе с моделью в одном файле может находиться 
factory, для их создания используется [Factory Boy](https://factoryboy.readthedocs.io/en/stable/) и [Faker](https://faker.readthedocs.io/en/master/).

В директории [models/fields](models/fields) находятся кастомные поля, имеющие особенную валидацию или необходимые
для переиспользования в разных моделях.

В директории [utils](utils) находятся разнообразные утилиты, помогающие в тестировании.

В директории [tests](tests) находятся директории с тестами, разбитые аналогично группам в openapi.

### Утилиты

#### api_client

Для запросов вместо requests используется [класс ApiClient](utils/api_client.py), который вынесен в pytest fixtures (`api_client`).

Класс предоставляет методы для переключения между пользователями, которые начинаются с `as_`, например `as_pilot()`.
Класс предоставляет методы для генерации URL, которые соответствуют эндпоинтам в openapi, например `federation-entities()`.

Методы класса используют method chaining, что позволяет их вызывать друг за другом, например вызов `as_admin().internal().drone-areas()`
означает, что в запросе будет использован пользователь администратор, а url будет склеен следующим образом: `/internal/drone-areas`.

#### sppi_api_client

[Класс SppiApiClient](utils/sppi_api_client.py) используется для обращения к API СППИ, включая получение токенов авторизации. 
Используется в _ApiClient_.

#### base_client

[Класс BaseClient](utils/base_client.py) является сервисным и наследуется классами для запросов. Класс не содержит большого количества
методов и предполагает изучение перед началом работы с ним.