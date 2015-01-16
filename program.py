from flask import (
							Flask,
							render_template,
							request
						)

#import dbase

app = Flask(__name__)

@app.route('/')
def hello_world():
	return render_template('index.html')

'''@app.route('/generate')
def generate_link():
	field = request.args.get('Field')
	sql = "SELECT * FROM LINK WHERE FIELD = (?) ORDER BY RANDOM() LIMIT 1"
	link = db.read(sql,field)
	return render_template('rel_info.html', data = link, data = field)'''

@app.route('/user_id/<int:identity>')
def print_id_int(identity):
	return 'Hello robot %d' %identity

@app.route('/hello')
@app.route('/goodbye')
def annoy():
	return 'what what'

@app.errorhandler(404)
def raiseerror(error):
	return "lol ganvaar."

if __name__ == '__main__':
	#dbase.init()
	app.run(debug = True)
