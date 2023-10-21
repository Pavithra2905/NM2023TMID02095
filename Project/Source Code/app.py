from flask import Flask, render_template

app = Flask(__name__)

@app.route('/',methods=["GET", "POST"])
def index():
    return render_template('index.html')

@app.route('/Dashboard',methods=["GET", "POST"])
def dashboard():
    return render_template('dashboard.html')

@app.route('/Report',methods=["GET", "POST"])
def report():
    return render_template('report.html')

@app.route('/Story',methods=["GET", "POST"])
def story():
    return render_template('story.html')


if __name__ == "__main__":
    app.run(debug=True)
