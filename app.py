from flask import Flask, render_template, request, redirect, Response, send_file, abort

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/portfolio-detail')
def blog():
    return render_template("portfolio-details.html", code=302)

if __name__ == "__main__":
    print("running py app")
    app.run(host="127.0.0.1", port=5000, debug=True)