from flask import Flask
from flask import jsonify, request
from invalidUsage import InvalidUsage

import requests

# EB looks for an 'application' callable by default.
application = Flask(__name__)


@application.route('/core-wallet/checkversion')
def check_version():
    version = request.args.get('version')
    current = '6.3.0.24'
    changed = (version == current)
    return jsonify(
        latest=changed,
        current_version=current,
        change_log='Initial version',
        tag='global'
    )


@application.route('/price', methods=['GET'])
def get_price():
    symbol = 'iop'
    targetSymbol = request.args.get('symbol')

    if targetSymbol is None:
        targetSymbol = symbol

    try:
        apiResult = requests.get(
            'https://coincodex.com/api/coincodex/get_coin/' + targetSymbol)

        if apiResult.status_code == requests.codes.ok:
            dataResult = apiResult.json()
            return jsonify(
                symbol=targetSymbol,
                usdPrice=dataResult['last_price_usd']
            )
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        raise InvalidUsage('Error to get price.', 500)

    raise InvalidUsage('Error to get price.', 500)


@application.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = False
    application.run()
