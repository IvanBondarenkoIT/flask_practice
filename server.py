from flask import Flask
from random import randint


target_number = randint(0, 9)
app = Flask(__name__)


@app.route("/")
def home():
    # return "Hello World!"
    return '<iframe src="https://giphy.com/embed/3o7aCSPqXE5C6T8tBC" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/animation-retro-pixel-3o7aCSPqXE5C6T8tBC">via GIPHY</a></p>'


@app.route("/<int:guess_number>")
def check_number(guess_number):

    if guess_number > target_number:
        return "The number is greater than"
    elif guess_number < target_number:
        return "The number is less than"
    else:
        return "You WIN!"


if __name__ == "__main__":
    app.run(debug=True)
