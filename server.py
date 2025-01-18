import ssl
import cv2
import base64
import numpy as np
import os
from flask import Flask, render_template
from flask_socketio import SocketIO

# Initialize Flask and Flask-SocketIO
app = Flask(__name__)
socketio = SocketIO(app, async_mode="threading")

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('video_frame')
def handle_video_frame(data):
    # Decode base64 image
    img_data = base64.b64decode(data.split(',')[1])
    np_img = np.frombuffer(img_data, dtype=np.uint8)
    frame = cv2.imdecode(np_img, cv2.IMREAD_COLOR)

    # Save the received image to a file
    filename = "received_frame.jpg"
    cv2.imwrite(filename, frame)
    print(f"Saved frame as {filename}")

if __name__ == '__main__':
    # Define paths to your SSL certificate and key
    cert_file = 'certificates/certificate.crt'
    key_file = 'certificates/private.key'

    # Create an SSL context
    ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    ssl_context.load_cert_chain(certfile=cert_file, keyfile=key_file)

    # Use Werkzeug server with SSL
    socketio.run(app, host='0.0.0.0', port=5000, ssl_context=ssl_context)
