# Пульт охраны банка

Это внутренний репозиторий для сотрудников банка «Сияние». Если вы попали в этот репозиторий случайно, то вы не сможете его запустить, т.к. у вас нет доступа к БД, но можете свободно использовать код вёрстки или посмотреть как реализованы запросы к БД.

Пульт охраны — это сайт, который можно подключить к удалённой базе данных с визитами и карточками пропуска сотрудников нашего банка.

### Как установить

Запросите доступ к БД у менеджера вашего банка. Для доступа вам понадобятся `DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD`.

`DEBUG`- переменная окружения, которая включает / выключает режим отладки. При `DEBUG = True` отладка включена. В случае возникновения ошибок в браузере отобразится отладочная информация.
Поэтому перед запуском сайта необходимо отключить режим отладки, установив `DEBUG = False`.

`SECRET_KEY` - Секретный ключ. Используется для криптографической подписи, должен быть случайным и сложным для подбора.

Значения переменных следует указать в файле `project/settings.py`

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Как запустить сайт

Сайт запускается из терминала командой: `python manage.py runserver 0.0.0.0:8000`
Для просмотра сайта перейти в браузере по ссылке: [localhost:8000] (http://127.0.0.1:8000)

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).