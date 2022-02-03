# selenium_saucedemo_ui_tests
[![CircleCI](https://circleci.com/gh/Twilighters/selenium_saucedemo_ui_tests/tree/main.svg?style=svg)](https://circleci.com/gh/Twilighters/selenium_saucedemo_ui_tests/tree/main)

# Тесты для приложения ["uitestingplayground"](http://uitestingplayground.com/sampleapp) на Selenium WebDriver

## Установка
***
1. Создайте отдельную директорию на локальном компьютере
2. https://github.com/Twilighters/selenium_saucedemo_ui_tests.git
3. Откройте проект
4. Установите все пакеты, которые указаны в файле requirements.txt <br>
pip install -r /path/to/requirements.txt


## Описание проекта
***
Целью написания данного набора тестов является проверка корректной работы основного функционала приложения. <br> В данный тестовый набор вошли следующие проверки:
### Тест проверки формы авторизации
Позитивная проверка:
* проверка на то что мы можем авторизоваться в системе с валидным логином и паролем<br>

Негативные проверки:
* неверный логин и пароль
* пустой логин
* пустой пароль

__Запуск в файле__: tests/auth/test_auth.py
