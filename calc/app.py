# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

# close but returns answer as a string... so
# @app.route('/add')
# def add():
#     a = request.args.get('a')
#     b = request.args.get('b')
#     answer = (a + b)

#     return answer


@app.route('/add')
def add():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    answer = (a + b)
    # return type cannot be an integer, so turn it back to a string
    return str(answer)


@app.route('/sub')
def sub():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    answer = (a - b)
    # return type cannot be an integer, so turn it back to a string
    return str(answer)


@app.route('/div')
def divide():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    answer = (a / b)
    # return type cannot be an integer, so turn it back to a string
    return str(answer)


@app.route('/mult')
def multiply():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    answer = (a * b)
    # return type cannot be an integer, so turn it back to a string
    return str(answer)
