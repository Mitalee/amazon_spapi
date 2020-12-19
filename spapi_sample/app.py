from flask import Flask
from spapi_sample.blueprints.user import user

def create_app(debug=True, main=True):
    app = Flask(__name__)#, instance_relative_config=True)#, static_folder='static-v1.0.1')

    app.url_map.strict_slashes = False

    app.config.from_object('config.settings')


    app.register_blueprint(user)

    return app