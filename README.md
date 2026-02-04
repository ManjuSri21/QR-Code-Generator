# QR Code Generator Web Application

A simple **QR Code Generator** built using **Python Flask** that allows users to generate scannable QR codes from URLs.  
When a link is entered, a QR code is generated instantly. Scanning the QR code opens the corresponding website.


## 🚀 Features
- Generate QR codes instantly from user-provided links
- Clean and attractive user interface with gradient styling
- Simple and beginner-friendly Flask project


## 🛠️ Tech Stack
**Frontend:** HTML5 | CSS3  
**Backend:** Python | Flask  
**Libraries:** qrcode | Pillow  

## ⚙️ Backend Functionality

The backend of this application is built using **Python Flask** and performs the following tasks:

- Handles HTTP requests (GET and POST) from the frontend
- Receives the URL entered by the user through a form
- Generates a QR code using the `qrcode` library
- Saves the generated QR image in the `static/images` directory
- Sends the QR image path to the frontend for display
- Manages routing and template rendering using Flask


## 📦 Required Libraries
Install the necessary libraries using:
```bash
pip install flask qrcode pillow
