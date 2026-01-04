from api_client import get_map_rotation, get_crafting_rotation, get_predator_cap, get_game_news
import time
import json

print("Testing Map Rotation...")
maps = get_map_rotation()
print(f"Maps: {str(maps)[:50]}...")
time.sleep(1.5) # Respect rate limit

print("Testing Crafting...")
crafting = get_crafting_rotation()
print(f"Crafting: {str(crafting)[:50]}...")
time.sleep(1.5)

print("Testing Predator...")
pred = get_predator_cap()
print(f"Predator: {str(pred)[:50]}...")
time.sleep(1.5)

print("Testing News...")
news = get_game_news()
print(f"News: {str(news)[:50]}...")
