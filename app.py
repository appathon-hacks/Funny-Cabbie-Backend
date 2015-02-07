

from flask import Flask, jsonify, make_response, render_template, redirect, request
from crossdomain import crossdomain

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
	print command_name
	print request.args['args']
	return  make_response(jsonify({ 'error': '500' }))	
	

	
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
	


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)