from flask import Flask

app = Flask(__name__)

existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']


@app.route("/")
def welcome ():
    return "<h1> Welcome to Flatiron Cars </h1>"

@app.route("/<model>")
def module(model):
    if model in existing_models:
        return f"<h2>Flatiron {model} is in our fleet!</h2>"
    else:
        return f"<h2>No Model {model} exists in our catalog.</h2>"

if __name__ == '__main__':
    app.run(debug=True)
