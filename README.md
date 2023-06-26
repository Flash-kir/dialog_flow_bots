# bot_speaker

Программа

## Установка и запуск

Клонируйте реппозиторий:

```bash
$ git clone git@github.com:Flash-kir/dialog_flow_bots.git
```

Выполните команду:

```bash
$ pip install -r requirenments.txt
```

Укажите токены бота telegram(`TELEGRAM_BOT_TOKEN=`), группы VK(`VK_GROUP_TOKEN=`), api(`API_KEY=`, [включите API](https://cloud.google.com/dialogflow/es/docs/quick/setup#api)) и project id(`PROJECT_ID=`, [создать проект](https://cloud.google.com/dialogflow/docs/quick/setup) и [агента](https://cloud.google.com/dialogflow/docs/quick/build-agent)) DialogFlow, путь к файлу с ключами от google cloud аккаунта(`GOOGLE_APPLICATION_CREDENTIALS=`, [создать токен](https://cloud.google.com/docs/authentication/api-keys)) в файле .env, предварительно выполнив команду:

```bash
$ cp example.env .env
```

Запустите бот telegram командой:

```bash
$ python bot_tm.py
```

Запустите бот vk командой:

```bash
$ python bot_vk.py
```

## Установка и запуск с использованием Docker

Клонируйте реппозиторий:

```bash
$ git clone git@github.com:Flash-kir/dialog_flow_bots.git
```

Установите [Docker](https://docs.docker.com/engine/install/)

Укажите токены бота telegram(`TELEGRAM_BOT_TOKEN=`), группы VK(`VK_GROUP_TOKEN=`), api(`API_KEY=`, [включите API](https://cloud.google.com/dialogflow/es/docs/quick/setup#api)) и project id(`PROJECT_ID=`, [создать проект](https://cloud.google.com/dialogflow/docs/quick/setup) и [агента](https://cloud.google.com/dialogflow/docs/quick/build-agent)) DialogFlow, путь к файлу с ключами от google cloud аккаунта(`GOOGLE_APPLICATION_CREDENTIALS=`, [создать токен](https://cloud.google.com/docs/authentication/api-keys)) в файле .env, предварительно выполнив команду:

```bash
$ cp example.env .env
```

Файл с ключами от гугл аккаунта поместите по пути, указанном в переменной `GOOGLE_APPLICATION_CREDENTIALS` в файле `.env`.

### тренировка бота

Тренировку бота можно осуществить через интерфейс `DialogFlow`, либо загрузить из `.json` файла c помощью программы `load_questions.py`, выполнив команду:

```bash
$ python load_questions.py {путь до файла с тренировочными фразами и его имя}.json
```

Для примера в корне проекта лежит файл `questions.json`, который содержит тренировочные фразы и ответы для бота.

### Создание образа и запуск локально

Создайте образ, выполнив команду(команда выполняется в папке с файлом `Dockerfile`):

```bash
$ docker build -f Dockerfile -t bot-speaker .
```

#### бот telegram

Запустите его(команда выполняется в папке с файлом `bot_tm.py`):

```bash
$ docker run -d --env-file {Полный путь до .env файла}.env --mount type=bind,source={Полный путь до key.json файла}/,target=/app flashkir/bot-speaker "python" "bot_tm.py"
```

#### бот telegram

Запустите его(команда выполняется в папке с файлом `bot_vk.py`):

```bash
$ docker run -d --env-file {Полный путь до .env файла}.env --mount type=bind,source={Полный путь до key.json файла}/,target=/app flashkir/bot-speaker "python" "bot_vk.py"
```

#### Клонирование и запуск образа на сервере

Создайте образ командой:

```bash
$ docker build -f Dockerfile -t bot-speaker .
```

либо получите его пул реквестом:

```bash
$ docker pull flashkir/bot-speaker
```

#### бот telegram

Запустите его(команда выполняется в папке с файлом `bot_tm.py`):

```bash
$ docker run -d --env-file {Полный путь до .env файла}.env --mount type=bind,source={Полный путь до key.json файла}/,target=/app flashkir/bot-speaker "python" "bot_tm.py"
```

Имя действующего бота `@speaker_dvmn_bot`.

#### бот telegram

Запустите его(команда выполняется в папке с файлом `bot_vk.py`):

```bash
$ docker run -d --env-file {Полный путь до .env файла}.env --mount type=bind,source={Полный путь до key.json файла}/,target=/app flashkir/bot-speaker "python" "bot_vk.py"
```

Действующий бот запущен в группе ВК по [ссылке](https://vk.com/public221141443).
