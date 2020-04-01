from flask import Flask, render_template, request, flash, redirect, url_for, jsonify, session, make_response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from datetime import timedelta
from models import *
import requests
from flask_socketio import SocketIO, emit
app = Flask(__name__)


app.config.setdefault('BOOTSTRAP_SERVE_LOCAL', True)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:20001003@localhost:5432/test"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 关闭对模型修改的监控
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"   #filesystem允许用户对数据进行更改、插入、删除等操作
app.config['SECRET_KEY'] = 'dev'  # 等同于 app.secret_key = 'dev'

app._static_folder = "./static"

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds = 1)
#escape() 函数对 name 变量进行转义处理，比如把 < 转换成 &lt;
socketio = SocketIO(app)

@socketio.on("new message")
def message(data):
    new_message = data["new_message"]
    emit("announce message", data, broadcast=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = User(request.form.get('user_id'), request.form.get('password'))
        remember_me = request.form.get('remember_me')
        user.login()
        if user.isAuthorized():
            if remember_me == True:
                make_response.set_cookie(f"{user.user_id}", f"{user.password}", max_age=3600)
            return redirect(url_for('homepage', user_id = user.user_id))



    return render_template('login.html')


@app.route('/register/', methods=['POST', 'GET'])
def register():
    return render_template('register.html')

@app.route('/test/')
def test():
    return render_template('test.html')


# * `200 OK`
# * `201 Created`
# * `400 Bad Request`
# * `403 Forbidden`
# * `404 Not Found`
# * `405 Method Not Allowed`
# * `422 Unprocessable Entity`
