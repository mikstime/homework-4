# Тестовый отчет команды `undefined`


## Расположение файлов

`components` – скрывают за фасадом логику для взаимодействия с элементами страницы 

`pages` – Делегируют компонентам взаимодействие со страницей и осуществляют открытие нужной страницы

`setup` – Часто используемые тестовые окружения

`tests` – Тестовые случаи, вызывающие конкретную последовательность вызовов событий через pages.

___
Тестируемые проекты: [контакты mail.ru](contacts.mail.ru) и [Имя отправителя и подпись](https://e.mail.ru/settings/general)
___

## Распределение ролей:

* Балицкий Михаил – `tests/signatures`

* Ишимбаев Марат – `tests/other`

* Болдин Дмитрий – `tests/contacts`

* Петренко Сергей – `tests/editor`

###### Подробная информация о тестах лежит в соответствующей директории

## Запуск тестового окружения:

`./grid.sh` – запуск selenium

`./node.sh` – запуск chromedriver и geckodriver

## Запуск самих тестов

```
LOGIN=<email> PASSWORD=<password> ./run_tests.py
``` 
