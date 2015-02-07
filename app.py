

from flask import Flask, jsonify, make_response, render_template, redirect, request
from crossdomain import crossdomain

import pyjokes

app = Flask(__name__)

commands = [
	'joke'
];


@app.route('/')
@crossdomain(origin='*')
def index():
    '''
    This page is displayed when index page is requested.
    '''
    return  make_response(jsonify({ 'error': '503 something wrong' }))
	
@app.route('/command/<command_name>/')
@crossdomain(origin='*')
def command(command_name):
	'''
	This page is displayed when index page is requested.
	'''
	result = {}
	if command_name == 'joke':
		result['joke'] = get_joke()
	return  make_response(jsonify(result),200)	
	

	
@app.errorhandler(404)
def not_found(error):
    '''
    Returns a jsonified 404 error message instead of a HTTP 404 error.
    '''
    return make_response(jsonify({ 'error': '404 not found' }), 404)


@app.errorhandler(503)
def not_found(error):
    '''
    Returns a jsonified 503 error message instead of a HTTP 404 error.
    '''
    return make_response(jsonify({ 'error': '503 something wrong' }), 503)
	
@app.errorhandler(500)
def not_found(error):
	'''
	Returns a jsonified 500 error message instead of a HTTP 404 error.
	'''
	print error
	return make_response(jsonify({ 'error': '500 something wrong' }), 500)	
	
	
# helpers

def get_joke():
	return pyjokes.get_joke()

	


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)