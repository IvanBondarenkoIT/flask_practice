from flask import Flask

app = Flask(__name__)


def add_tag(function, tag: str):
    return f"<{tag}>{function}</{tag}>"


def make_bold(function):
    def wrapper():
        return add_tag(function(), tag="b")

    return wrapper


def make_emphasis(function):
    def wrapper():
        return add_tag(function(), tag="en")

    return wrapper


def make_underlined(function):
    def wrapper():
        return add_tag(function(), tag="u")

    return wrapper


@app.route("/")
@make_bold
@make_emphasis
@make_underlined
def hello_world():
    return "Hello"
    # return (
    #     "<p>Hello, World!</p>"
    #     "<h1> Hello, World!</h1>"
    #     '<iframe src="https://giphy.com/embed/auxDaJxhVa2By" width="480" height="374" frameBorder="0" class="giphy-embed" allowFullScreen></iframe> '
    # )


@app.route("/username/<username>")
def greet(username):
    return f"<p>Hello, {username} </p>"


if __name__ == "__main__":
    app.run(debug=True)
