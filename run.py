import dbase

from flask import Flask

app = Flask(__name__)

# Blueprints make your app modular
from views import (
    frontend,
    api
)

app.register_blueprint(frontend)
app.register_blueprint(api, url_prefix='/api/1')

# Error handling is always great!
from errors import init_errors
init_errors(app)


if __name__ == '__main__':

    dbase.init()

    app.run(
        host='127.0.0.1',
        port=9999,
        debug=True
    )
