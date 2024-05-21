# main.py

from flask import Flask, render_template
from flask_socketio import SocketIO, send

# Initialize Flask app
app = Flask(__name__)

# Initialize Flask-SocketIO
socketio = SocketIO(app, cors_allowed_origins="*")


# Define a handler for the 'message' event
@socketio.on('message')
def handle_message(message):
    # Broadcast the received message to all clients
    send(message, broadcast=True)


# Define a route for the home page
@app.route('/')
def index():
    # Render the index.html template
    return render_template('index.html')


# Define a route for the chat page
@app.route('/chat')
def chat():
    # Render the chat.html template
    return render_template('chat.html')


# Run the Flask app with Flask-SocketIO
if __name__ == '__main__':
    socketio.run(app, host="localhost", port=5000, debug=True)
