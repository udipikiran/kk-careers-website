from flask import Flask, render_template, jsonify

app = Flask(__name__, template_folder="templates", static_folder='static', static_url_path="/")

JOBS = [
    {
        'id':1,
        'title':'Data Analayst',
        'location':'Bangalore',
        'salary':'10L INR'
    },
    {
        'id':2,
        'title':'Data Scientist',
        'location':'Bangalore',
        'salary':'20L INR'
    },
    {
        'id':3,
        'title':'DBA',
        'location':'Bangalore',
        'salary':'15L INR'
    },
    {
        'id':4,
        'title':'Middleware',
        'location':'Bangalore',
        'salary':'18L INR'
    }
]

@app.route("/")
def index():
    return render_template("home.html", jobs = JOBS)

@app.route("/jobs")
def listjobs():
    return jsonify(JOBS)

print(__name__)
if __name__ == "__main__":
    app.run(host="localhost", debug=True)