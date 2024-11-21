import sys
import requests

AUTH_ID = 'YOU_AUTH_ID'
BASE_URL = 'https://api.iot.yandex.net/v1.0/scenarios'

SCENARIOS = {
    'finish_print': 'YOU_SCENARIOS_ID',
    'pause_print': 'YOU_SCENARIOS_ID'  
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

