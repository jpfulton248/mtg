import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import create_app
from dotenv import load_dotenv
from __init__ import create_app

load_dotenv()

app = create_app()

if __name__ == '__main__':
	app.run()