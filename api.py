from flask import Flask

#initialize the app
app = Flask(__name__)

#define what happens when you visit the main page (/)

@app.route("/")
def home():
    return "<h1> this is my first flask app.</h1><p> its working </p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
