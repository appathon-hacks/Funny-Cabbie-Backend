

from flask import Flask, jsonify, make_response, render_template, redirect, request
from crossdomain import crossdomain
import requests
import duckduckgo as ddg
import pyjokes
import json

app = Flask(__name__)

commands = [
	'joke',
	'food',
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
	if command_name == 'train':
		result['train'] = get_train_status_url(request.args['args'])
	return  make_response(jsonify(result),200)	
	

@app.route('/freetext/<free_text>/')
@crossdomain(origin='*')
def freetext(free_text):
	'''
	This page is displayed when index page is requested.
	'''
	result = {}
	if free_text == 'joke':
		result['joke'] = get_joke()
	if free_text == 'trivia':
		result['trivia'] = get_trivia()
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
	
def get_trivia():
	return 'Random Trivia'
	
def get_train_status_url(train_no):
	try:
		return goo_shorten_url('http://www.trainrunningstatus.org/0%s'%train_no)
	except:
		return 'http://www.trainrunningstatus.org/0%s'%train_no

	
def goo_shorten_url(url):
	post_url = 'https://www.googleapis.com/urlshortener/v1/url'
	payload = {'longUrl': url}
	headers = {'content-type': 'application/json'}
	r = requests.post(post_url, data=json.dumps(payload), headers=headers)
	print r.text.strip()
	return r.text

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)