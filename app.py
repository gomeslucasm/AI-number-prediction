from flask import Flask, render_template, request
#from functions import predict_number

app = Flask(__name__)


@app.route('/')
def Home_get():
    return render_template("home.html")


if __name__ == "__main__":
    app.run()
