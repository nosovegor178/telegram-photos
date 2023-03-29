# Скачанивае фото NASA и SpaceX

Этот проект для того, чтобы скачивать фото с разных разделов NASA, а именно: APOD (A Picture Of The Day) и EPIC (Earth Polychromatic Imaging Camera), а также с серверов SpaceX в больщих количествах.

### Как установить

На компьютере пользователя должен быть установлен Python3.
Затем используйте `pip` (или `pip3`, есть конфликт Python2) для установки зависимостей:
```
pip install -r requirments.txt
``` 
Рекомендуется использовать [virtulenv/venv](https://docs.pythpn.org/3/library/venv.html) для изоляци проекта.

### Переменные окружения

В данном проекте переменной окружения является NASA_API.  В этой переменной хранится api key от сайта NASA. Чтобы в этой переменной хранился ваш ключ вам надо создать файл .env и в нём написать строку
```
NASA_API="Ваш ключ"
``` 
, где вместо "Ваш ключ" надо подставить api key без кавычек


### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org).