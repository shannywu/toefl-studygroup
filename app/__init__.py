#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

# app config

app = Flask(__name__)

# extension

db = SQLAlchemy(app)

# blueprints

from views.home import home

app.register_blueprint(home)