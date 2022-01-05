import os
from flask import Flask
import db
import auth
import environment
import status
import rgb
import timer
import holiday
import stock
import temperature

test_config = None

app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(SECRET_KEY='dev', )

if test_config is None:
    app.config.from_pyfile('config.py', silent=True)
else:
    app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


@app.route('/')
def hello_world():
    return 'Hello User, not World!'


db.init_app(app)
app.register_blueprint(auth.bp)
app.register_blueprint(environment.bp)
app.register_blueprint(status.bp)
app.register_blueprint(rgb.bp)
app.register_blueprint(timer.bp)
app.register_blueprint(holiday.bp)
app.register_blueprint(stock.bp)
app.register_blueprint(temperature.bp)
