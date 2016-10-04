#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, jsonify, request, url_for, session, redirect
from app.models import User
from app import db, facebook
from os import path
import json

login = Blueprint('login', __name__, template_folder='templates', static_folder='static')

@facebook.tokengetter
def get_facebook_token():
    return session.get('facebook_token')

@login.route('/login')
def fb_login():
    return facebook.authorize(callback=url_for('login.facebook_authorized', next=request.args.get('next'), _external=True))

@login.route("/facebook_authorized")
@facebook.authorized_handler
def facebook_authorized(resp):
    next_url = request.args.get('next') or url_for('home.index')
    if resp is None or 'access_token' not in resp:
        return redirect(next_url)

    session['logged_in'] = True
    session['facebook_token'] = (resp['access_token'], '')

    data = facebook.get('/me').data
    if 'id' in data and 'name' in data:
        user_id = data['id']
        user_name = data['name']
        session['name'] = user_name

        user = User.query.filter_by(fb_id=user_id).first()
        if not user:
            user = User(user_name, user_id)
            db.session.add(user)
            db.session.commit()

    return redirect(next_url)
