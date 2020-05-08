from flask import Blueprint, request

from api.config import get_logger

_logger = get_logger(logger_name=__name__)

prediction_app = Blueprint('prediction_app', __name__)


@prediction_app.route('/car_prices', methods=['GET'])
def car_prices():
    if request.method == 'GET':
	_logger.info('car price status OK')
        return 'ok'
