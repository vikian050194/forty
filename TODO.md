# TODO

## Todo

- [x] Вынести кучу разного кода из `utils.py`
- [x] Редьюсеры сегодняшнего прошедшего и оставлегося рабочего времени
- [ ] ~~Редьюсер накопленного оставлегося рабочего времени~~
- [x] Корректно обрабатывать переработку
- [x] Вычисление прошедшего времени на день и всего
- [x] Вычисление остатка на день и всего
- [x] Работа над несколькими проектами
- [x] Вынести комманды и покрыть тестами
- [x] Добавить `notify-send` в `py`
- [x] Отделить форматирование сообщения от `emmit`
- [x] [Изменить команды](./todo/feature/command.md)
- [x] Автодополнение
- [x] Удобный `API` для `SDK`
- [x] Журнал действий
- [x] Время окончания работы сегодня
- [ ] ~~Реализовать одно redo~~
- [x] Рефакторинг `to_hms` и других функций
- [x] Выводить `whatsup` более понятно
  - [x] Завести отдельную вьюшку для статус контроллера
  - [x] Завести отдельные вьюшки для всех роутов статус контроллера
  - [x] Улучшить понятность вывода новой вьюшки
  - [x] Время в формате `hh:mm:ss`
- [x] Команды в формате `noun verb`
- [x] [Статус имеет неправильное значение](./todo/bug/whatsup.md) в `whatsup`
- [x] Сохранять конфигурацию проекта и действия в форматированном виде
- [x] [Можно пересоздать проект](./todo/bug/project.md)
- [x] Покрыть код моделей юнит тестами
  - [x] project
    - [x] new
    - [x] get
    - [x] set
    - [x] list
  - [x] history
    - [x] reset
    - [x] undo
    - [x] log
  - [x] status
    - [x] all
    - [x] only
    - [x] today
    - [x] total
    - [x] passed
    - [x] remained
    - [x] interval
  - [x] work
    - [x] start
    - [x] finish
- [ ] ~~Выделить модель log~~
- [x] Покрыть код контроллеров юнит тестами
  - [x] history
    - [x] default
    - [x] reset
    - [x] undo
    - [x] log
  - [x] project
    - [x] default
    - [x] new
    - [x] get
    - [x] set
    - [x] list
  - [x] status
    - [x] default
    - [x] all
    - [x] only
    - [x] today
    - [x] total
    - [x] passed
    - [x] remained
    - [x] interval
  - [x] work
    - [x] start
    - [x] finish
- [x] `get` [падает при большом интервале](./todo/bug/get.md)
- [x] Печать в `JSON` при [завершении работы](./todo/bug/finish.md)
- [x] Упростить [подкоманды](./todo/feature/subcommand.md)
- [x] [Дата начала работы](./todo/feature/start.md)
- [x] Автоматическое начало и завершение работы
  - [x] Добавить в README инструкцию
  - [x] Добавить пример `forty.service`
- [ ] Автодополнение через приложение
- [ ] Актуализировать help
  - [ ] Помощь
  - [ ] Автодополнение
  - [ ] Тесты
- [ ] [Дефолтные значения](./todo/feature/default.md)
- [ ] Механизм подтверждения опасных операций
- [ ] Настройки проекта и работа с ними
  - [ ] Дневной лимит
  - [ ] Общий лимит
- [ ] Глобальные настройки и работа с ними
  - [ ] Дневной лимит
  - [ ] Общий лимит
- [ ] Редактирование уже добавленных действий
- [ ] Команда `brake`
- [ ] Команда `lunch`
    - [ ] Добавить в глобальные и проектовые настройки
    - [ ] Добавить команду для добавления обеда
- [ ] Удаление проекта
- [ ] Подтверждение автоматического начала работы
- [ ] Нотификация при завершении времени
- [ ] Выбор проекта при автоматическом старте
- [ ] Выводить информацию по дням
- [ ] Цвета для журнала действий
- [ ] Поддержка env переменных для отключения цветов
  - [ ] `FORTY_COLOR`
  - [ ] `NO_COLOR`
- [ ] Реализовать `undo` и `redo` на `N` шагов
  - [ ] Настройка количества хранимых версий
  - [ ] Хранение необходимого числа версий
  - [ ] Возможность откатиться на любую из них
- [ ] [Добавить какого-то количества времени](./todo/feature/time.md)
- [ ] exit code

## Backlog

Empty

## Old

- [x] autocomplete
- [ ] single version source

## Actions

**Work**

- [x] start
- [x] start hh:mm:ss
- [x] finish
- [x] finish hh:mm:ss
- [ ] pause
- [ ] resume

## Commands

**Work**

- [ ] plus hh:mm:ss
- [ ] minus hh:mm:ss
- [ ] set hh:mm:ss
- [ ] break
- [ ] break hh:mm:ss

**Status**

- [x] only
- [x] full
- [x] status
- [x] today
- [x] total
- [x] passed
- [x] remained
- [x] interval

**Log**

- [x] log
- [ ] log yyyy-mm-dd


**Check**

- [x] check
- [x] check yyyy-mm-dd

**Project**

- [x] project list
- [x] project get
- [x] project set

**History**

- [x] undo
- [x] undo n
- [ ] redo
- [ ] redo n

**Config**

- [ ] config

## Configuration

**Flags**

- [ ] output format

**Environment**

- [x] home directory
- [x] output format

**Project**

- [x] day limit
- [x] total limit
- [ ] break

**Global**

- [ ] concurrency
- [ ] break
