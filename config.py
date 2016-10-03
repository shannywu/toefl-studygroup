#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import path

BASE_DIRECTORY = path.abspath(path.dirname(__file__))
DEBUG = True
ASSETS_DEBUG = True
SECRET_KEY = 'cr4xW3b4w3S0M3>><<@.@^.^'

# SQL
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///toefl.db'

# Facebook App Info
FACEBOOK_APP_ID = '336386950040724'
FACEBOOK_APP_SECRET = '0482b187ebc9388d2bcf027513f11505'