from api_client import get_server_status
import json

status = get_server_status()
if status:
    print("Keys found:", list(status.keys()))
    # Check if 'Xbox-API' is directly in keys
    if 'Xbox-API' in status:
        print("Xbox-API is at root.")
    else:
        print("Xbox-API NOT at root. Searching values...")
        for k, v in status.items():
            if isinstance(v, dict) and 'Xbox-API' in v:
                print(f"Found 'Xbox-API' inside '{k}'")
else:
    print("Status is None")
