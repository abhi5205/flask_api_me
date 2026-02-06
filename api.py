from flask import Flask

#initialize the app
app = Flask(__name__)

#define what happens when you visit the main page (/)

@app.route('/')
def home():
    return "<h1> this is my first flask app.</h1><p> its working </p>"

#defining a second page(/hello)
@app.route('/hello')
def say_hello():
    return "you are now on the hello page"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
