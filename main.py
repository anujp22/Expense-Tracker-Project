from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route('/result')
def result():
    return render_template("result.html")

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")

if __name__ == "__main__":
    app.run(debug=True)