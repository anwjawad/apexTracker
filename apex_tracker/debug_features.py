from api_client import get_player_stats
import json

# Fetch stats for a known active player (e.g., Genburten or ImperialHal or user's player if known)
# Using a pro player likely to have data
data = get_player_stats("ImperialHal", "PC")
if data and 'realtime' in data:
    print("REALTIME DATA FOUND:")
    print(json.dumps(data['realtime'], indent=2))
else:
    print("No realtime data found.")

if data and 'global' in data:
    print("\nGLOBAL DATA (Check for Club):")
    # limit output
    print(str(data['global'])[:500])
