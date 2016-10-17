#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_oauth import OAuth
import config

# app config

app = Flask(__name__)

# extension

db = SQLAlchemy(app)

# Facebook Oauth
oauth = OAuth()
facebook = oauth.remote_app(
    'facebook',
    base_url='https://graph.facebook.com/',
    request_token_url=None,
    access_token_url='/oauth/access_token',
    authorize_url='https://www.facebook.com/dialog/oauth',
    consumer_key=config.FACEBOOK_APP_ID,
    consumer_secret=config.FACEBOOK_APP_SECRET,
    request_token_params={'scope': ('email, ')}
)

# blueprints
from views.home import home
from views.login import login

app.register_blueprint(home)
app.register_blueprint(login)
