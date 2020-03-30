from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit, join_room, leave_room
from flask_login import current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


# 可以直接通过这个启动app 也包括flask的一套启动
# 可以使用系统中除了Werkzeug之外的东西
# socketio.run(app)

# socketio.on_event('my event', my_function_handler, namespace='/test')
@socketio.on('message', namespace='/test')
def handle_message(message):
    print('received message:' + message)
    # send使用未命名的事件
    send(message)
    # emit使用已经命名了的事件
    emit(message, broadcast=True)
    return 'success'

@socketio.on('join')
def on_join(data):
    username = data['username']
    room = data['room']
    join_room(room)
    send(username+ ' has entered the room.', room = room)
@socketio.on('leave')
def on_leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    send(username+ ' has left the room.', room = room)
    