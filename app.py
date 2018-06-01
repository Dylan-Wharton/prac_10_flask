from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello World :)</h1>'


if __name__ == '__main__':
    app.run()


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return "Hello {}".format(name)


@app.route('/f')
@app.route('/f/temp')
def f(temp):
    fahrenheit = temp * 9.0 / 5 + 32
    return fahrenheit
