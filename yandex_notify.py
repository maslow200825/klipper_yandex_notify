import sys
import requests

AUTH_ID = 'сюда вписать свой' #получить auth_id https://oauth.yandex.ru/client/new/
BASE_URL = 'https://api.iot.yandex.net/v1.0/scenarios'

# Сюда надо вписать ID сценария который создается в сценариях умного дома алисы, я сделал два, на смену прутка и на завершение печати. запуск сценария по фразе
# туда вписать билиберду чтобы он не запускался случайно, а команда прочитать текст на нужной колонке
SCENARIOS = {
    'finish_print': '',
    'pause_print': ''  # id сценария можно узнать по ссылке https://iot.quasar.yandex.ru/m/user/scenarios, предварительно авторизовавшись под той же учетной записью под которой подключена яндекс станция.
}

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

