from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "hello"
# @app.route("/")
# def home():
#     return "First page"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/test")
def test():
    return render_template("new.html")

@app.route("/login", methods= ["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        session["user"] = user
        return redirect(url_for("user"))
    else:
        return render_template("login.html")

@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return f"<h1>{user}</h1>"
    else:
        return redirect(url_for("login"))
    
if __name__ == "__main__":
    app.run(debug=True)
