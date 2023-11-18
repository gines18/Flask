from flask import Flask, render_template, request, redirect, url_for, session
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(minutes=5)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/test")
def test():
    return render_template("new.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"].strip()
        if user:
            session.permanent = True
            session["user"] = user
            return redirect(url_for("user"))
        else:
            return render_template("login.html", error="Please enter a valid username")
    else:
        if "user" in session:
            return redirect(url_for("user"))
        return render_template("login.html")

@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return render_template("user.html", usr=user)
    else:
        return redirect(url_for("login"))

@app.route("/hp")
def hp():
        user = session["user"]
        return render_template("hp.html", usr=user)

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
