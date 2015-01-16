from flask import (
							Flask,
							render_template,
							request
						)
app = Flask(__name__)

@app.route('/')
def hello_world():
	return render_template('index.html')

@app.route('/generate')
def generate_link():
	field = request.args.get('Field')
	return render_template('rel_info.html', data = field)

@app.route('/user_id/<int:identity>')
def print_id_int(identity):
	return 'Hello robot %d' %identity

@app.route('/hello')
@app.route('/goodbye')
def annoy():
	return 'what what'

if __name__ == '__main__':
	app.run(debug = True)
