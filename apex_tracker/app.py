from flask import Flask, render_template, request
from api_client import get_player_stats

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    stats = None
    error = None
    
    if request.method == "POST":
        player_name = request.form.get("player_name")
        platform = request.form.get("platform")
        
        if player_name:
            data = get_player_stats(player_name, platform)
            if "error" in data:
                error = data["error"]
            else:
                stats = data
        else:
            error = "Please enter a player name."
            
    return render_template("index.html", stats=stats, error=error)

@app.route("/compare", methods=["GET", "POST"])
def compare():
    stats1 = None
    stats2 = None
    error = None
    
    if request.method == "POST":
        p1_name = request.form.get("player1_name")
        p1_plat = request.form.get("player1_platform", "PC")
        
        p2_name = request.form.get("player2_name")
        p2_plat = request.form.get("player2_platform", "PC")
        
        if p1_name and p2_name:
            # Fetch both
            s1 = get_player_stats(p1_name, p1_plat)
            s2 = get_player_stats(p2_name, p2_plat)
            
            if "error" in s1:
                error = f"Player 1 Error: {s1['error']}"
            elif "error" in s2:
                error = f"Player 2 Error: {s2['error']}"
            else:
                stats1 = s1
                stats2 = s2
        else:
            error = "Please enter both player names."
            
    return render_template("compare.html", stats1=stats1, stats2=stats2, error=error)

@app.route("/live")
def live_tracker():
    return render_template("live.html")

@app.route("/api/stats")
def api_stats():
    # Helper API for the live tracker JS to call
    player = request.args.get("player")
    platform = request.args.get("platform", "PC")
    if not player:
        return {"error": "No player specified"}, 400
    return get_player_stats(player, platform)

@app.route("/dashboard")
def dashboard():
    from api_client import get_map_rotation, get_crafting_rotation, get_server_status, get_predator_cap, get_game_news
    import time
    
    # Simple in-memory cache
    if not hasattr(app, 'cache'):
        app.cache = {}
        
    current_time = time.time()
    cache_duration = 300 # 5 minutes
    
    data = {}
    endpoints = {
        'maps': get_map_rotation,
        'crafting': get_crafting_rotation,
        'predator': get_predator_cap,
        'news': get_game_news
    }
    
    for key, func in endpoints.items():
        # Check cache
        if key in app.cache and (current_time - app.cache[key]['time'] < cache_duration):
            data[key] = app.cache[key]['data']
        else:
            # Fetch new data
            try:
                result = func()
                app.cache[key] = {'data': result, 'time': current_time}
                data[key] = result
                # Sleep to prevent rate limit (1 req/sec)
                time.sleep(0.7)
            except Exception as e:
                print(f"Error fetching {key}: {e}")
                data[key] = None
    
    
    # Server status is huge, let's just assume checks are done on client or backend simple check
    # But now we want it!
    server_status = get_server_status() # Directly fetch for now to ensure freshness or cache it above
    # Actually let's use the list I made but I forgot to add it to 'endpoints' dict
    # Let me just fetch it here safely
    try:
        if 'servers' not in app.cache or (current_time - app.cache.get('servers', {}).get('time', 0) > 300):
             raw_status = get_server_status()
             
             # Flatten structure: Move selfCoreTest items to root
             if raw_status and 'selfCoreTest' in raw_status:
                 raw_status.update(raw_status['selfCoreTest'])
                 
             app.cache['servers'] = {'data': raw_status, 'time': current_time}
        server_status = app.cache['servers']['data']
    except:
        server_status = None

    return render_template("dashboard.html", 
                           maps=data.get('maps'), 
                           crafting=data.get('crafting'), 
                           predator=data.get('predator'), 
                           news=data.get('news'),
                           server_status=server_status)

@app.route("/overlay")
def overlay():
    player = request.args.get("player")
    platform = request.args.get("platform", "PC")
    if not player:
        return "Please provide player name: /overlay?player=NAME", 400
    
    stats = get_player_stats(player, platform)
    # If error, just return error text
    if "error" in stats:
        return stats["error"]
        
    return render_template("overlay.html", stats=stats)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)

