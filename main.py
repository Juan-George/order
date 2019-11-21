# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
from geventwebsocket.handler import WebSocketHandler
from gevent.pywsgi import WSGIServer


app = Flask(__name__)  # 创建一个服务对象，赋值给APP


@app.route('/websocket')
def index():
    return render_template('websocket.html')


@app.route('/')
def love():
    return render_template('Love.html')


http_server = WSGIServer(('0.0.0.0', 9090), app, handler_class=WebSocketHandler)
http_server.serve_forever()