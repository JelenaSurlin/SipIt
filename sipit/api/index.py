import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app import app

def handler(environ, start_response):
    return app(environ, start_response)