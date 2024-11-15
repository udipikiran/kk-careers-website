from flask import Flask, render_template

app = Flask(__name__, template_folder="templates", static_folder='static', static_url_path="/")

@app.route("/")
def index():
    return render_template("home.html")

print(__name__)
if __name__ == "__main__":
    app.run(host="localhost", debug=True)