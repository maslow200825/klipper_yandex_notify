# Инструкция: Получение AUTH_ID для управления Яндекс Станцией
## 1. Получение AUTH_ID
### 1.1 Создание нового приложения
1. Перейдите по ссылке: [https://oauth.yandex.ru/client/new](https://oauth.yandex.ru/client/new).
2. Авторизуйтесь под аккаунтом, к которому привязана ваша Яндекс Станция.
3. Укажите:
   - **Имя приложения**: любое (например, "klipper_notify").
   - **Платформы**: выберите **Веб-сервисы**.
   - **Redirect URI**: `https://oauth.localhost.local/auth`.
   - **Suggest Hostname**: `https://oauth.localhost.local`.
4. В разделе **Доступ к данным** выберите два пункта:
   - `iot:view`
   - `iot:control`
5. Почту можно указать любую.
6. После создания приложения получите **Client ID**.

### 1.2 Получение токена доступа (AUTH_ID)
1. Перейдите по ссылке: [https://oauth.yandex.ru/authorize?response_type=token&client_id=ВАШ_CLIENT_ID]
   Замените `ВАШ_CLIENT_ID` на ID приложения, полученный на предыдущем шаге.
2. Нажмите **"Войти как ..."**.
3. После входа вас перенаправит на несуществующий сайт `https://oauth.localhost.local/auth`.
4. В адресной строке найдите фрагмент: https://oauth.localhost.local/auth#access_token=ВАШ_ACCESS_TOKEN
5. Скопируйте значение `ВАШ_ACCESS_TOKEN` — это и есть ваш **AUTH_ID**. его необходимо прописать в yandex_notify.py
6. ```markdown
AUTH_ID =
```
---
## 2. Получение ID сценария
### 2.1 Создание сценариев в Яндекс Умном доме
1. Создайте сценарий в приложении "Яндекс".
- Например:
  - Для завершения печати: "Печать завершена".
  - Для смены прутка: "Сменить пруток".
2. Укажите фразу, которую не используете в повседневной речи, чтобы случайно не запускать сценарий.
3. Добавьте действие: **прочитать текст на нужной колонке**.

### 2.2 Получение ID сценария
1. Перейдите по ссылке: [https://iot.quasar.yandex.ru/m/user/scenarios](https://iot.quasar.yandex.ru/m/user/scenarios).
2. Авторизуйтесь под тем же аккаунтом, который используется с Яндекс Станцией.
3. Слева вверху включите опцию **"Автоформатирование"**.
4. Найдите ваш сценарий по имени и скопируйте его ID. его необходимо прописать в yandex_notify.py
```markdown
SCENARIOS = {
    'finish_print': '',
    'pause_print': ''
}
```
---
## 3. Использование ID сценария в yandex_notify.py
1. Укажите ID сценария в скрипте yandex_notify.py.
## 4. Установка и настройка скрипта на машине с Klipper
### 4.1 Размещение скрипта
1. Скопируйте скрипт `yandex_notify.py` на машину с установленным Klipper.
2. Поместите файл в папку, к которой есть доступ у пользователя, под которым работает Klipper. Например: /home/username/yandex_notify.py

### 4.2 Установка поддержки G-Code Shell Command
1. В интерфейсе **KIAUH** перейдите в раздел **[Advanced]**.
2. Установите модуль **[G-Code Shell Command]**.
3. После установки в конфигурации **fluidd** появится файл `shell_command.cfg`.

### 4.3 Настройка команды в `shell_command.cfg`
1. Откройте файл `shell_command.cfg` для редактирования.
2. Добавьте следующий код:

```markdown
```ini
[gcode_shell_command ya_print_command]
command: python3 /home/linaro/yandex_notify.py
timeout: 2.
verbose: True

[gcode_macro FINISH_PRINT_YA]
gcode:
    RUN_SHELL_COMMAND CMD=ya_print_command PARAMS="finish_print"

[gcode_macro CHANGE_FILAMENT_YA]
gcode:
    RUN_SHELL_COMMAND CMD=ya_print_command PARAMS="pause_print"

### Ну и собственно эти макросы прописать в макрос завершения печати и смены филамента

