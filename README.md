# Boilerplate flask

Базовый шаблон для flask 

## Каталоги

- tests для тестов
- templates для html шаблонов
- static для статичных файлов (css/js/etc)

## Файлы
- run.py главный файл, запускает сервер
- app.py иницинилизирует приложение
- init_venv.bat опциональный файл, иницилизирует виртуальную среду

## endpoints
- / рендерит index.html шаблон
- /hello/<who> поприветствовать who
- /jsonreceive GET вернуть пустой json 
{ "data": [] }
- /jsonreceive POST эхо-вернуть json
{ "data": <входящие данные> }
## Фичи
- шаблоны
- поддержка JSON
- flask