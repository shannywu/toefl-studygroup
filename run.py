#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app import app, db

if __name__ == '__main__':
	app.config.from_object('config')
	db.create_all()
	app.run(host='0.0.0.0', port=5000)
