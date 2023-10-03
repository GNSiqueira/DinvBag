from app import app
from flask import os

if __name__ == "main":
    port = int(os.getenv('PORT'), '8000')

    app.run(host='0.0.0.0', port = port)