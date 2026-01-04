import requests
import json

# The key provided by the user
API_KEY = "17f37ba82ac6149ac19f7ccb42e918a8"
URL = "https://api.mozambiquehe.re/bridge"

params = {
    "auth": API_KEY,
    "player": "chs_minato",
    "platform": "PC"
}

print(f"Testing API access for player: {params['player']}...")

try:
    response = requests.get(URL, params=params)
    print(f"Status Code: {response.status_code}")
    print("Response Headers:")
    print(json.dumps(dict(response.headers), indent=2))
    
    if response.status_code == 200:
        print("Success! Data received:")
        # Print only the first 200 chars to avoid spam
        print(response.text[:200] + "...")
    else:
        print("Error Response:")
        print(response.text)

except Exception as e:
    print(f"Exception occurred: {e}")
