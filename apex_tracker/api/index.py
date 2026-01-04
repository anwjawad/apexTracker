import os
import sys

# Add the parent directory to sys.path so we can import app.py
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from app import app

# This is required for Vercel to find the app object
if __name__ == '__main__':
    app.run()
