from flask import Flask
from flask import jsonify, request

# EB looks for an 'application' callable by default.
application = Flask(__name__)

@application.route('/core-wallet/checkversion')
def check_version():
	version = request.args.get('version')
	current = '6.2.0.72'
	changed = (version==current)
	return jsonify(
		latest=True,
		current_version=current,
		change_log='Initial version'
	)

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = False
    application.run()
