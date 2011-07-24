from flask import Flask
from app.db import session_remove
from app.controller.project import project

app = Flask(__name__)
app.config.from_pyfile('settings.py')
app.register_module(project)

@app.after_request
def shutdown_session(response):
    session_remove()
    return response

