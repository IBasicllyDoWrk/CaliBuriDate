from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/details')
def details():
    # This page will host the date picker and store selector
    return render_template('details.html')

if __name__ == '__main__':
    app.run(debug=True)