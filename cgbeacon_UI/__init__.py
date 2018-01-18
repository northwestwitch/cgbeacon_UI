from flask import Flask, render_template

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')

import cgbeacon_UI.views
