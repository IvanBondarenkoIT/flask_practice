from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    # return "Hello World!"
    return '<iframe src="https://giphy.com/embed/3o7aCSPqXE5C6T8tBC" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/animation-retro-pixel-3o7aCSPqXE5C6T8tBC">via GIPHY</a></p>'


if __name__ == "__main__":
    app.run(debug=True)
