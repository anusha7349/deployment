from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return "this is my first deployment"
if __name__ == "main.py":
    app.run(host="0.0.0.0",port=5000)
    