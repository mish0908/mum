from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
import json
from database import init_db, get_messages, save_message
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'  # Change this to a secure key
socketio = SocketIO(app)

# Welcome page route
@app.route('/')
def welcome():
    return render_template('welcome.html')

# Slideshow route
@app.route('/slideshow')
def slideshow():
    return render_template('slideshow.html')

# Birthday card route
@app.route('/card', methods=['GET', 'POST'])
def card():
    if request.method == 'POST':
        name = request.form.get('name')
        message = request.form.get('message')
        save_message(name, message)
        return jsonify({'status': 'success'})
    messages = get_messages()
    return render_template('card.html', messages=messages)

# Chat route
@app.route('/chat')
def chat():
    return render_template('chat.html')

# Socket.IO events
@socketio.on('message')
def handle_message(data):
    emit('message', {
        'user': data['user'],
        'message': data['message'],
        'timestamp': datetime.now().strftime('%H:%M')
    }, broadcast=True)

if __name__ == '__main__':
    init_db()
    socketio.run(app, debug=True) 