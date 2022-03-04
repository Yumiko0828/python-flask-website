from flask import Flask, render_template

# Settings
app = Flask(__name__)

# Routes
@app.route("/")
def index():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

# Server listening
if __name__ == '__main__':
    app.run(debug=True, port=3000)