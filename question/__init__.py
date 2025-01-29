from flask import Flask

def create_app():
    app = Flask(__name__)

    # Register routes (in routes.py)
    from .routes import home
    app.add_url_rule('/', 'home', home)

    return app
