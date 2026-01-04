import requests
import os

API_KEY = os.environ.get("APEX_API_KEY", "17f37ba82ac6149ac19f7ccb42e918a8")
BASE_URL = "https://api.mozambiquehe.re/bridge"

params = {
    "auth": API_KEY,
    "player": "Genburten", # Known player
    "platform": "PC",
    "history": 1
}

print(f"Fetching with params: {params}")
try:
    response = requests.get(BASE_URL, params=params, timeout=10)
    print(f"Status Code: {response.status_code}")
    print(f"Content: {response.text[:500]}") # Print first 500 chars
    response.json()
    print("JSON Decode Success")
except Exception as e:
    print(f"Error: {e}")
