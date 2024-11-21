import sys
import requests

AUTH_ID = 'сюда вписать свой'   # получить auth_id https://oauth.yandex.ru/client/new/ после авторизации под почтой к которой привязана яндекс станция
                                # имя приложения любое, платформы "веб сервисы", Redirect URI = "https://oauth.localhost.local/auth" Suggest Hostname = "https://oauth.localhost.local"
                                # доступ к данным, надо выбрать два iot:view И iot:control, почту указать любую, после создания приложения будет доступен client ID
                                # url для получения самого токена после создания приложения https://oauth.yandex.ru/authorize?response_type=token&client_id="сюда client ID"
                                # после нажатия "войти как ..." перекинет на несуществующий сайт https://oauth.localhost.local/auth, в адресе будет заветный https://ouath.localhost.local/auth#access_token=
                                # вот этот acces_token и есть AUTH_ID
BASE_URL = 'https://api.iot.yandex.net/v1.0/scenarios'

# Сюда надо вписать ID сценария который создается в сценариях умного дома алисы, я сделал два, на смену прутка и на завершение печати. запуск сценария по фразе
# туда вписать билиберду чтобы он не запускался случайно, а команда прочитать текст на нужной колонке
SCENARIOS = {
    'finish_print': '',
    'pause_print': ''  
}
# id сценария можно узнать по ссылке https://iot.quasar.yandex.ru/m/user/scenarios, предварительно авторизовавшись под той же учетной записью под которой подключена яндекс станция.
# для удобства слева вверху поставить галочку "автоформатирование", находим по имени сценарий который создали и копируем id, finish_print и pause_print это параметр который передается скрипту
# поэтому что тут указывать можно придумать самому, главное в клиппере это название и передавать

def execute_command(command):
    scenario_id = SCENARIOS.get(command)
    if not scenario_id:
        print(f"Unknown command: {command}")
        return
    
    url = f"{BASE_URL}/{scenario_id}/actions"
    headers = {
        'Authorization': f'Bearer {AUTH_ID}'
    }

    response = requests.post(url, headers=headers)
    if response.status_code == 200:
        print(f"Command '{command}' executed successfully.")
    else:
        print(f"Failed to execute '{command}'. Status code: {response.status_code}")
        print("Response:", response.text)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <command>")
    else:
        command = sys.argv[1]
        execute_command(command)

