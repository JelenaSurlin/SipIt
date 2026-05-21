from app import app

def handler(environ, start_response):
    start_response("200 OK", [("Content-Type", "text/plain")])
    return [b"SipIT OK"]