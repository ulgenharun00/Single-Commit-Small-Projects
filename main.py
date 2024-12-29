import random
from email.header import make_header

from flask import Flask

app = Flask(__name__)

integer = random.randint(0,9)

@app.route("/")
def home_route():
    return ('<h1>Guess a number between 0 and 9</h1>'
            '<img src=https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif>')

@app.route("/<int:guess>")
def guess_number(guess):
    if guess < integer:
        return ('<h1>Too low</h1>'
                '<img src=https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif>')

    elif guess > integer:
        return ('<h1>Too high</h1>'
                '<img src=https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif>')

    else:
        return ('<h1>You are right!</h1>'
                '<img src=https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif>')

if __name__ == "__main__":
    app.run(debug=True)