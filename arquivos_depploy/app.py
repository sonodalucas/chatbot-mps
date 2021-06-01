from flask import Flask, render_template, request
from chatbot import answer
# create the application object
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("chat.html") # render a template

@app.route('/get')
def add_msg():

    msg = request.args.get('msg')
    return str(answer(msg))

if __name__ == '__main__':
    app.run()