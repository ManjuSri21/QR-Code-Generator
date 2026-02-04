# QR Code Generator Web Application

## 📄 Description

- Flask-based QR Code Generator web application  
- Generates QR codes from user-provided URLs  
- Displays QR code instantly on the webpage  
- Scanning the QR opens the corresponding website  
- Simple and responsive UI using HTML and CSS  


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

Install the required libraries using pip:

- **Flask** – Web framework for backend development  
- **qrcode** – Library for generating QR codes  
- **Pillow** – Image processing library used by qrcode
  
```bash
pip install flask qrcode pillow

