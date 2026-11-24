# from flask import Flask
# app = Flask(__name__)

# @app.route("/")
# def hallo():
#     return  "Hello, World!"

# @app.route("/")
# def home():
#     return "Home page"

# @app.route("/about")
# def about():
#     return "About us"

# @app.route("/user/<name>")
# def profile(name):
#     return f"Hello, {name}!"

# @app.route("/post/<int:post_id>")
# def post(post_id):
#     return f"Post #{post_id}"

# @app.route("/")
# def index():
#     return "Welcome!"

# @app.route("/hi/<name>")
# def hi(name):
#     return f"Hi, {name}!"

# @app.route("/double/<int:n>")
# def double(n):
#     return f"{n * 2}"

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/greet", methods=["POST"])
def greet():
    varNama = request.form.get("parName")
    if not varNama:
        varNama = "Anonim"
    return f"<h2>Halo, {varNama}! Selamat datang di Flask First App </h2>"

if __name__ == "__main__":
    app.run(debug=True)