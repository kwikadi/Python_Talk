from flask import (
    Blueprint,
    jsonify,
    render_template
)

""" Frontend """

frontend = Blueprint('frontend', __name__)


@frontend.route('/')
def hello_frontend():
    return render_template('index.html')

# @frontend.route('/generate')
# def generate_link():
#     field = request.args.get('Field')
#     sql = "SELECT * FROM LINK WHERE FIELD = (?) ORDER BY RANDOM() LIMIT 1"
#     link = db.read(sql, field)
#     return render_template('rel_info.html', data = link, data = field)


@frontend.route('/user/<int:identity>')
def print_id_int(identity):
    return 'Hello robot %d' % identity


""" API """

api = Blueprint('api', __name__)


@api.route('/')
def hello_api():
    return jsonify(status=200, message="Awesome API goes here.")
