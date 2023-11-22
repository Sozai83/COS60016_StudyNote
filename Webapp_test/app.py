from flask import Flask, redirect, url_for, render_template, request
import requests

# flask --app app.py --debug run

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', content='True')


@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template("login.html")
    

@app.route("/user/<string:usr>")
def user(usr:str):
    if len(usr) > 0:
        return render_template("user.html", usr=usr)
    else:
        redirect(url_for("login"))


if __name__ == '__main__':
    app.run()


