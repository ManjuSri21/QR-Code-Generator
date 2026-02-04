from flask import Flask, render_template, request
import qrcode
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    qr_image = None

    if request.method == "POST":
        data = request.form.get("data")
        if data:
            # Make images folder inside static if not exist
            images_path = "static/images"
            if not os.path.exists(images_path):
                os.makedirs(images_path)

            # Save QR code
            img_path = os.path.join(images_path, "qr.png")
            img = qrcode.make(data)
            img.save(img_path)

            qr_image = "images/qr.png"  # Path relative to static folder

    return render_template("index.html", qr_image=qr_image)

if __name__ == "__main__":
    app.run(debug=True)
