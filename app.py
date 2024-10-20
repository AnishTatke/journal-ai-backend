
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO
from datetime import datetime

from models.History import History
from bin.utils import process_audio_file
from bin.voice_agent import text_to_speech
from bin.generate_question import generate_next_question

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})
socketio = SocketIO(app, cors_allowed_origins="*")

conversation_history = History(num_questions=5)

# Routes
@app.route('/api/new_user', methods=['POST'])
def new_user():
    data = request.get_json()
    print(jsonify(data))
    return "New User Registered", 200


# SocketIO
@socketio.on('connect')
def handle_connect():
    try:
        print('Client connected')
    except Exception as e:
        print(e)
        print('Error in generating questions')


@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')


@socketio.on('give_answer')
def handle_answer(data):
    print('Received audio message:', data)
    try:
        # Convert audio to text

        # Save answer for specific question

        response = {
            'text': 'Answer received',
            'status': True
        }
        socketio.emit('answer', response)
    except Exception as e:
        print(e)
        response = {
            'text': 'Error in receiving answer',
            'status': False
        }
        socketio.emit('answer', response)


@socketio.on('request_question')
def send_question():
    print('Received request for question')
    try:
        # Generate a question
        question = generate_next_question(conversation_history)
        conversation_history.add_to_history("assistant", question)
        # Convert question to audio
        audio_base64 = text_to_speech(question)
        response = {
            "status": True,
            'id': 0,
            'text': question,
            'audioUrl': audio_base64
        }
        socketio.emit('question', response)
    except Exception as e:
        print("My Error", e)
        response = {
            'id': None,
            'text': 'Error in sending question',
            'status': False,
            'audioUrl': None
        }
        socketio.emit('question', response)

@socketio.on('send_message')
def handle_message(message):
    print('Received message:', message)
    response = {
        'text': message,
        'timestamp': datetime.now().strftime('%H:%M:%S'),
        'status': 'received',
        'type': 'text'
    }
    socketio.emit('message', response)

if __name__ == '__main__':
    socketio.run(app, port=5000)
