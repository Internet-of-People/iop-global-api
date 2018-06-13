from flask import Flask
from flask import jsonify, request

# EB looks for an 'application' callable by default.
application = Flask(__name__)

@application.route('/core-wallet/checkversion')
def check_version():
	version = request.args.get('version')
	changed = (version=='1.0.0')
	return jsonify(
		latest=changed,
		current_version='1.0.0',
		change_log='Initial version'
	)

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = False
    application.run()
