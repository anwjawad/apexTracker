from api_client import get_map_rotation
import json

maps = get_map_rotation()
print(json.dumps(maps, indent=2))
