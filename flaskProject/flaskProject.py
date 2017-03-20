from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def index():


    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
    # THis is for LINUX ONLY     app.run(debug=True, host='83.212.82.80', port=8000)
