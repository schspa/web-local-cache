#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#   app.py --- Flask entry point
#
#   Copyright (C) 2022, Schspa Shi, all rights reserved.
#
#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 2 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
import os
import toml
from flask import Flask, render_template, request
from flask import send_from_directory, redirect

app = Flask(__name__)
if os.path.exists("/etc/local-url-cache/config.toml"):
    app.config.from_file("/etc/local-url-cache/config.toml", load=toml.load)
else:
    app.config.from_file("config.toml", load=toml.load)

@app.route('/<path:path>')
def send_report(path):
    if os.path.exists(os.path.join(app.config['LOCAL_PATH'], path)):
        response =  send_from_directory(app.config["LOCAL_PATH"], path)
        response.headers["Content-Type"] = 'text/plain; charset=utf-8'
        return response
    else:
        return redirect('{:s}/{:s}'.format(app.config["REMOTE_HOST"], path))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
