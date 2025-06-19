from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'michellezhu'

# Welcome/Home page route
@app.route('/')
def index():
    return render_template('welcome.html')

# Birthday card route
@app.route('/birthday_card', methods=['GET', 'POST'])
def birthday_card():
    return render_template('card.html')

# Photo album route
@app.route('/photo_album')
def photo_album():
    return render_template('photo_album.html')

if __name__ == '__main__':
    app.run(debug=True)