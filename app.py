import random
import webbrowser
import cv2
import numpy as np
import time
from flask import Flask, render_template, Response
from keras.models import load_model
from music_dictionary import emotion_urls
from tensorflow.keras.preprocessing.image import img_to_array

app = Flask(__name__)

# Load the trained emotion detection model
model = load_model('emotion_model.h5')

emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']
last_emotion = None  # Store the last detected emotion
last_song_time = time.time()  # Store time of the last played song

def play_song(emotion):
    global last_emotion, last_song_time
    current_time = time.time()
    if emotion != last_emotion and current_time - last_song_time > 20:
        if emotion in emotion_urls:
            song_urls = emotion_urls[emotion]
            if song_urls:
                song_url = random.choice(song_urls)
                webbrowser.open(song_url)
                last_song_time = current_time
        last_emotion = emotion

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/current_emotion')
def current_emotion():
    return last_emotion or "Neutral"

def gen_frames():
    global last_emotion
    cap = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        detected_emotion = "Neutral"

        for (x, y, w, h) in faces:
            face = gray[y:y+h, x:x+w]
            face = cv2.resize(face, (48, 48))
            face = img_to_array(face).reshape(1, 48, 48, 1) / 255.0
            emotion_probabilities = model.predict(face)
            detected_emotion = emotion_labels[np.argmax(emotion_probabilities[0])]

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, detected_emotion, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        play_song(detected_emotion)
        last_emotion = detected_emotion

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    cap.release()

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
