import requests
import os

# TODO: Replace with your actual API Key or set the environment variable 'APEX_API_KEY'
API_KEY = os.environ.get("APEX_API_KEY", "17f37ba82ac6149ac19f7ccb42e918a8")

BASE_URL = "https://api.mozambiquehe.re/bridge"

def get_player_stats(player_name, platform="PC"):
    """
    Fetch player stats from Apex Legends Status API.
    
    Args:
        player_name (str): The username of the player.
        platform (str): The platform (PC, PS4, X1). Default is PC.
        
    Returns:
        dict: The player's stats or an error message.
    """
    if API_KEY == "YOUR_API_KEY_HERE":
        return {"error": "API Key is missing. Please set APEX_API_KEY."}

    params = {
        "auth": API_KEY,
        "player": player_name,
        "platform": platform
    }
    
    try:
        response = requests.get(BASE_URL, params=params, timeout=5)
        
        if response.status_code == 429:
            return {"error": "تم تجاوز الحد المسموح للطلبات (Rate Limit). يرجى الانتظار دقيقة والمحاولة مرة أخرى."}
            
        if response.status_code == 404:
            return {"error": "اللاعب غير موجود! تأكد من الاسم والمنصة (PC/PS4/XBOX)."}
            
        response.raise_for_status()
        
        # The API can return 200 OK but with an internal error string, so we check content
        data = response.json()
        
        if "Error" in data:
            return {"error": data["Error"]}
            
        return data
        
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

def get_map_rotation():
    """Fetch current and next map rotation."""
    url = "https://api.mozambiquehe.re/maprotation?version=2"
    try:
        response = requests.get(url, params={"auth": API_KEY}, timeout=5)
        return response.json()
    except:
        return None

def get_crafting_rotation():
    """Fetch daily/weekly crafting rotation."""
    url = "https://api.mozambiquehe.re/crafting"
    try:
        response = requests.get(url, params={"auth": API_KEY}, timeout=5)
        return response.json()
    except:
        return None

def get_server_status():
    """Fetch Apex server status."""
    url = "https://api.mozambiquehe.re/servers"
    try:
        response = requests.get(url, params={"auth": API_KEY}, timeout=5)
        return response.json()
    except:
        return None

def get_predator_cap():
    """Fetch RP needed for Predator rank."""
    url = "https://api.mozambiquehe.re/predator"
    try:
        response = requests.get(url, params={"auth": API_KEY}, timeout=5)
        return response.json()
    except:
        return None

def get_game_news():
    """Fetch latest Apex news."""
    url = "https://api.mozambiquehe.re/news"
    try:
        response = requests.get(url, params={"auth": API_KEY}, timeout=5)
        return response.json()
    except:
        return None
