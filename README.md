# Drone Area Registry Service API

Тесты для сервиса Drone Area Registry, используемого в СППИ

- [Роли](https://docs.google.com/spreadsheets/d/1DFgbV-dRgdI0ARPRAnqC8w505sMK-S36jFZDWbMf2GA/edit?usp=sharing)
- [Репозиторий](https://git.monitorsoft.ru/spppi/drone-area-registry)
- [API документация](https://git.monitorsoft.ru/spppi/drone-area-registry/-/blob/master/spec/v1_openapi.yaml)

## Установка

Необходим python 3.12 (на меньших версиях не тестировался).

`pip install -r requirements.txt`

Опционально `cp .env.example .env` для создания файла с переменными окружения.

## Переменные окружения

Возможные переменные окружения указаны в [.env.example](.env.example). Для удобства разработки используется 
библиотека [dotenv](https://pypi.org/project/python-dotenv/).

## Запуск

Тесты используют заранее созданных пользователей в системе. Логины и пароли указываются в переменных окружения.

`pytest tests/`

В проекте используются тега (pytest marks) для более удобного запуска тестов, например, для того, чтобы запустить только
тесты, которые проверяют доступ, можно использовать команду `pytest -m access`.

Для запуска в несколько потоков можно использовать `pytest -n 4`, где `-n` - количество потоков, однако рекомендуется
запускать в один поток, так как верная работа тестов не гарантирована.

Для запуска с созданием отчета allure в несколько потоков: `pytest --alluredir allure-results -n 6`.

## Разработка

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

### Коммиты

Перед коммитом необходимо убедиться в том, что все файлы верно отформатированы. 

Сообщение коммита формируется согласно [conventional commits](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13).
