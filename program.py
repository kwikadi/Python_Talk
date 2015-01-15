from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello World part 2!'

@app.route('/username/<identity>')
def print_id(identity):
	return 'Hello %s' % identity

@app.route('/user_id/<int:identity>')
def print_id_int(identity):
	return 'Hello robot %d' %identity

@app.route('/hello')
@app.route('/goodbye')
def annoy():
	return 'what what'

if __name__ == '__main__':
	app.run(debug = True)
