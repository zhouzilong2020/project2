import os

from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, send

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

message =[]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login/")
def login():
    return render_template("login.html")

# send() is used for unnamed event
@socketio.on('sent message')
def sent_message(data):
    message.append(data)
    emit("sent message", message, broadcast = True)
    # emit支持callback function 以返回是否收到某一个信息
    # emit('my response', json, callback=function)
