#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, jsonify, request
from app.models import Vocabulary
from app import db
from os import path
import json

home = Blueprint('home', __name__,
				template_folder='templates',
				static_folder='static')

@home.route('/')
def index():
	datas = Vocabulary.query.all()
	return render_template('vocabulary.html', datas=datas)

@home.route('/vocabulary/<data_type>/<id>')
def vocabulary(data_type, id):
	data = Vocabulary.query.filter_by(id=id).first()
	json_data = {}
	with open(path.abspath(path.dirname(__file__)) + '/../static/vocabulary/' + data.file_name, 'r') as f:
		json_data = json.load(f)

	if data_type == 'a':
		json_data = [d[0] for d in json_data]
	else:
		json_data = [d[1] for d in json_data]

	return jsonify(json_data)