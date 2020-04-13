# coding=utf-8
from flask import Flask, redirect, render_template
import random
app = Flask(__name__)

list_of_quotes = ['If at first you don\'t succeed... so much for skydiving.',
                  'I tell you what always catches my eye. Short people with an umbrella.',
                  'Wouldn\'t exercise be more fun if calories screamed while you burned them?']

@app.route('/')
def index():
    random.shuffle(list_of_quotes)
    return render_template('index.html', list_of_quotes=list_of_quotes)

if __name__ == "__main__":
    app.run()
