from api_client import get_server_status
import json

status = get_server_status()
print(json.dumps(status, indent=2))
