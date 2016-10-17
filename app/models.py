# /usr/bin/env python
# -*- coding: utf-8 -*-

from app import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    user = db.Column(db.String(255))
    fb_id = db.Column(db.Integer())

    def __init__(self, user, fb_id):
        self.user = user
        self.fb_id = fb_id


class Vocabulary(db.Model):
    __tablename__ = 'vocabulary'
    id = db.Column(db.Integer(), primary_key=True)
    file_name = db.Column(db.String(255))

    def __init__(self, file_name):
        self.file_name = file_name
