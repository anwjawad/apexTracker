import webview
import threading
import time
import sys
from app import app

# Function to run Flask in a separate thread
def start_server():
    # We use a different port or the same one. 
    # Important: threaded=True to ensure it doesn't block if we were running it differently, 
    # but app.run blocks, so we put it in a thread.
    app.run(port=5000, host="127.0.0.1", use_reloader=False)

if __name__ == '__main__':
    # Start Flask in a daemon thread
    t = threading.Thread(target=start_server)
    t.daemon = True
    t.start()

    # Wait a bit for server to spin up
    time.sleep(1)

    # Create the native window
    # width/height based on typical 1080p usage or smaller
    webview.create_window('Apex Legends Tracker', 'http://127.0.0.1:5000', width=1280, height=800, background_color='#121212')
    
    # Start the GUI loop
    webview.start()
