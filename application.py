from flask import Flask
from flask import jsonify, request

# EB looks for an 'application' callable by default.
application = Flask(__name__)

@application.route('/core-wallet/checkversion')
def check_version():
	version = request.args.get('version')
	current = '6.2.2.14'
	changed = (version==current)
	return jsonify(
		latest=changed,
		current_version=current,
		change_log='Initial version',
		tag = 'v6.2.2'
	)

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = False
    application.run()
