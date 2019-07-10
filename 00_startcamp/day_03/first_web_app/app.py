from flask import Flask, render_template
import random

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/pick_lotto')
def pick_lotto():
    numbers = range(1, 46)
    lucky = random.sample(numbers, 6)
    return str(lucky)


# @app.route('/get_lotto/<int:num>')
# def get_lotto_


@app.route('/hello/<name>')  # var routing
def hello(name):
    return f'hi,{name}'


@app.route('/pick_lunch/<int:count>')
def pick_lunch(count):
    menus = [
        '짜장면',
        '짬뽕',
        '마라탕',
        '마라샹궈',
        '탕수육',
        '양장피'
    ]
    picks = random.sample(menus, count)
    return str(picks)


@app.route('/cube/<int:number>')
def cube(number):
    return str(number ** 3)


if __name__ == '__main__':
    app.run(debug=True)
