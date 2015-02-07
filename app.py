

from flask import Flask, jsonify, make_response, render_template, redirect, request
from crossdomain import crossdomain

app = Flask(__name__)


@app.route('/')
@crossdomain(origin='*')
def index():
    '''
    This page is displayed when index page is requested.
    '''
    return render_template('main.html')
	


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)