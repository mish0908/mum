from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
from flask_cors import CORS
import os
import eventlet
eventlet.monkey_patch()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'michellezhu'
CORS(app, resources={r"/*": {"origins": "*"}})
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='eventlet')

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
@socketio.on('message')
def handle_message(data):
    emit('message', data, broadcast=True)

@socketio.on('join')
def handle_join(data):
    emit('user_joined', data, broadcast=True)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    socketio.run(app, host='0.0.0.0', port=port, debug=True)