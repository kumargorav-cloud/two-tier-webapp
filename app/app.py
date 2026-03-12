from flask import Flask, render_template, request
from flask import send_from_directory
import os
import time
import mysql.connector

from werkzeug.utils import secure_filename

app = Flask(__name__)

ADMIN_PASSWORD = "admin123"

UPLOAD_FOLDER = os.path.join(os.getcwd(), "uploads")
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

while True:
    try:
        db = mysql.connector.connect(
            host="db",
            user="root",
            password="root",
            database="userdb"
        )
        print("Connected to MySQL")
        break
    except:
        print("Waiting for MySQL...")
        time.sleep(5)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():

    name=request.form["name"]
    email=request.form["email"]
    image=request.files["image"]

    filename=secure_filename(image.filename)
    filepath=os.path.join(app.config["UPLOAD_FOLDER"], filename)

    image.save(filepath)

    cursor=db.cursor()

    query="INSERT INTO users (name,email,image) VALUES (%s,%s,%s)"
    values=(name,email,filename)
    cursor.execute(query,values)
    db.commit()

    return "User uploaded successfully"

@app.route("/users")
def users():

    cursor = db.cursor()

    cursor.execute("SELECT name,email,image FROM users")

    data = cursor.fetchall()

    return render_template("users.html", users=data)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory('uploads', filename)

@app.route("/admin", methods=["GET","POST"])
def admin():

    if request.method == "POST":

        password = request.form["password"]

        if password == ADMIN_PASSWORD:
            cursor = db.cursor()
            cursor.execute("SELECT name,email,image FROM users")
            data = cursor.fetchall()

            return render_template("users.html", users=data)

        else:
            return "Invalid password"

    return render_template("admin.html")
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)
