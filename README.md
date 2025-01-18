WebSocket Secure (WSS) Camera Stream Application
This project provides a secure, real-time camera streaming application using Flask and WebSockets over HTTPS (WSS).

Steps to Set Up the Application
Clone the repository:

git clone https://github.com/MohamedEshmawy/StreamCamServer
cd StreamCamServer
Install the required dependencies:

pip install -r requirements.txt
Install OpenSSL on Windows (if applicable):

Install via Precompiled Binaries:

Download OpenSSL for Windows from Shining Light Productions.
Add OpenSSL to your system's PATH environment variable.
Verify Installation:

Open a terminal and run:
openssl version
You should see the installed OpenSSL version.
Generate SSL certificates:

Open a terminal in the project directory.
Run the following command to create the certificates in the certificates/ folder:
mkdir certificates
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
    -keyout certificates/private.key \
    -out certificates/certificate.crt
You will be prompted to provide details such as country, organization name, etc. leave them blank for development purposes.
The private key will be saved as certificates/private.key.
The certificate will be saved as certificates/certificate.crt.
Start the Flask application with HTTPS and WebSocket Secure (WSS):

python app.py
Open the application in your browser:

Navigate to:
https://<your-domain-or-ip>:5000
The application should load, and the camera stream will be displayed.
