from flask import Flask, request, jsonify, Response
from flask import render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/Home')
def Home():
    return render_template('home.html', title='Home')
@app.route('/Generate', methods=['GET', 'POST'])
def Generate():
    return render_template('generate.html', title='Generate')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

