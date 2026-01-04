from api_client import get_map_rotation
import json

maps = get_map_rotation()
if maps and 'ranked' in maps:
    print("RANKED DATA:")
    print(json.dumps(maps['ranked'], indent=2))
else:
    print("No ranked data found")
