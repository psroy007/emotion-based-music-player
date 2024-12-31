# Emotion-Based Music Player 🎵🎭

A cutting-edge web application that leverages emotion recognition to analyze real-time facial expressions using a webcam. Based on the detected emotion, the system dynamically plays music from YouTube, offering a personalized auditory experience tailored to the user’s emotional state.

This project combines Deep Learning, Computer Vision, and Web Development technologies to create an interactive music player that responds to emotional cues.

## Key Features 🌟

- Real-Time Emotion Detection: Identifies emotions such as Happy, Sad, Angry, Fear, Surprise, Disgust, and Neutral from live webcam video using a pre-trained deep learning model.
- Music Recommendation: Automatically selects and plays a song from YouTube based on the detected emotion.
- Live Webcam Feed: Streams the webcam feed on a web interface for visual interaction.
- Emotion-Responsive UI: Dynamically updates the displayed emotion with color-coded feedback for an immersive user experience.

## Emotion to Music Mapping 🎶

Based on the detected emotion, the application plays an appropriate song from YouTube. Below is the mapping of emotions to music genres:

| **Detected Emotion**  | **Suggested Music Genre**            |
|-----------------------|--------------------------------------|
| **Happy**             | Upbeat, cheerful tracks             |
| **Sad**               | Soft, melancholic melodies          |
| **Angry**             | Intense, high-energy tracks         |
| **Fear**              | Mysterious, suspenseful music       |
| **Surprise**          | Exciting, energetic songs           |
| **Disgust**           | Dark, cleansing music               |
| **Neutral**           | Relaxing, instrumental music        |

## Installation & Setup ⚙️

### Prerequisites

Ensure you have the following installed:

- Python 3.7 or higher
- Virtual environment (optional, but recommended)
- A webcam for real-time emotion detection

## Steps to Install

### Clone the Repository:

            git clone https://github.com/your-username/emotion-based-music-player.git
            cd emotion-based-music-player


## Install Dependencies:

Use pip to install the required dependencies listed in the requirements.txt:

            pip install -r requirements.txt

## Prepare the Emotion Detection Model:

- Download or train the emotion detection model and save it as emotion_model.h5.
- Place the emotion_model.h5 file in the root directory of the project.

## Configure Music URLs:

Modify music_dictionary.py to include YouTube URLs for each detected emotion.

## Run the Application:

            python app.py

The application will run locally on http://127.0.0.1:5000.

## How to Use 🛠️

- Launch the Web Application: Open your browser and go to http://127.0.0.1:5000 to access the web interface.

- Allow Webcam Access: The app will prompt you to allow access to your webcam for emotion detection.

- Experience Emotion-Based Music:

- As you face the camera, the system will analyze your facial expression.

- The detected emotion will be displayed, and the appropriate song will play.


## File Structure 📁

emotion-based-music-player/
├── app.py                     # Flask application backend
├── templates/
│   └── index.html             # Frontend HTML for the user interface
├── static/                    # Optional static files (CSS, JS, etc.)
├── emotion_model.h5           # Pre-trained emotion detection model
├── music_dictionary.py        # Mapping of emotions to YouTube song URLs
├── requirements.txt           # List of required Python packages
└── README.md                  # Project documentation

## Dependencies 📦

This project requires the following libraries:

- Flask: Web framework for Python to build the web application.
- OpenCV: For capturing and processing the webcam feed.
- TensorFlow/Keras: For loading and using the emotion detection model.
- NumPy: For numerical operations.
- Webbrowser: For opening YouTube URLs to play music.

## Install all dependencies with the following command:

pip install -r requirements.txt

## How It Works 🤔

### Webcam Feed:

OpenCV captures the video feed from your webcam and processes each frame to detect faces.

### Emotion Recognition:

- The cropped face from the webcam feed is passed through a pre-trained emotion detection model.
- The model predicts the emotion by analyzing the facial expression.

### Music Playback:

- Based on the detected emotion, a corresponding song URL is fetched from music_dictionary.py.
- The song is opened in your default browser, allowing you to listen to it instantly.

## Future Enhancements 🚀

- Playlist Integration: Integrate with Spotify, YouTube Music, or other platforms for more music options.
- Multiple Face Detection: Play different songs for each detected face in the video feed.
- Emotion History: Log past emotions and songs played for better recommendations.
- Mobile Optimization: Enhance the user interface for mobile and tablet users.