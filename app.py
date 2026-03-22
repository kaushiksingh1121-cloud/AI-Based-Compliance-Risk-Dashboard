from flask import Flask, render_template, request
import pandas as pd
from database import Database
from analyzer import ComplianceAnalyzer

app = Flask(__name__)
db = Database()
analyzer = ComplianceAnalyzer()

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        file = request.files["file"]
        df = pd.read_csv(file)

        for msg in df["message"]:
            risk, score = analyzer.analyze(msg)
            db.insert_report(msg, risk, score)

        return render_template("success.html")

    return render_template("upload.html")

@app.route("/dashboard")
def dashboard():
    reports = db.fetch_reports()
    return render_template("dashboard.html", reports=reports)

if __name__ == "__main__":
    app.run(debug=True)
