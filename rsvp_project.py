from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    attending = request.form['attending']

    with open('responses.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([name, attending])

    return render_template('thankyou.html', name=name, attending=attending)

@app.route('/responses')
def show_responses():
    data = []
    try:
        with open('responses.csv', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            data = list(reader)
    except FileNotFoundError:
        pass

    return render_template('responses.html', data=data)

import os


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
