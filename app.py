from flask import Flask, render_template, request, jsonify, session
from flask_socketio import SocketIO, emit, join_room, leave_room
from flask_cors import CORS
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'michellezhu'
CORS(app, resources={r"/*": {"origins": "*"}})
socketio = SocketIO(app, 
                   cors_allowed_origins="*",
                   ping_timeout=60,
                   ping_interval=25,
                   logger=True,
                   engineio_logger=True)

# Welcome/Home page route
@app.route('/')
def index():
    return render_template('welcome.html', active_page='home')

# Birthday card route
@app.route('/birthday_card', methods=['GET', 'POST'])
def birthday_card():
    return render_template('card.html', active_page='card')

# Photo album route
@app.route('/photo_album')
def photo_album():
    return render_template('photo_album.html', active_page='相簿')

# Chat route
@app.route('/chat')
def chat():
    return render_template('chat.html', active_page='chat')

# SocketIO event handlers
@socketio.on('connect')
def handle_connect():
    emit('status', {'msg': 'Connected'}, broadcast=True)

@socketio.on('message')
def handle_message(data):
    print('Received message:', data)  # Debug log
    emit('message', data, broadcast=True, include_self=False)

@socketio.on('join')
def handle_join(data):
    print('User joined:', data)  # Debug log
    emit('user_joined', data, broadcast=True)

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')  # Debug log
    emit('status', {'msg': 'Disconnected'}, broadcast=True)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    socketio.run(app, host='0.0.0.0', port=port, debug=True)