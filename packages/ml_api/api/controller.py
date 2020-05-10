from flask import Blueprint, request, jsonify
from regression_model.predict import make_prediction
from regression_model import __version__ as _version
import pandas as pd
from api.config import get_logger
from api.validation import validate_inputs
from api import __version__ as api_version
import json

_logger = get_logger(logger_name=__name__)

prediction_app = Blueprint('prediction_app', __name__)


@prediction_app.route('/cars', methods=['GET'])
def cars():
    if request.method == 'GET':
        _logger.info('cars status OK')
        return 'ok'

@prediction_app.route('/version', methods=['GET'])
def version():
    if request.method == 'GET':
        return jsonify({'model_version': _version,
                        'api_version': api_version})
    


@prediction_app.route('/v1/predict/car_prices', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Step 1: Extract POST data from request body as JSON
        print('abc')
        json_data = request.get_json()
        _logger.debug(f'Inputs: {json_data}')

        # Step 2: Validate the input using marshmallow schema
        # validated_data, errors = validate_inputs(input_data=json_data)
        # if validated_data:
        #     val_dict = validated_data[0]
        #     tot_dict = json.loads(json_data)[0]
        #     val_list = list(val_dict.keys())
        #     tot_list = list(tot_dict.keys())
        #     rem_flds = [x for x in tot_list if x not in val_list]
        #     for i in rem_flds:
        #         val_dict[i] = tot_dict[i]
        #     input_data = pd.DataFrame.from_dict(val_dict, orient='index')
        # else:
        #     # input_data = json.loads(json_data)
        #     input_data = pd.json_normalize(input_data)
        #     input_data = pd.DataFrame(input_data)    
       
        input_data = pd.json_normalize(json_data)
        input_data = pd.DataFrame(input_data)
        # Step 3: Model prediction
        result = make_prediction(input_data=input_data)
        _logger.debug(f'Outputs: {result}')

        # Step 4: Convert numpy ndarray to list
        predictions = result.get('predictions').tolist()
        version = result.get('version')

        # Step 5: Return the response as JSON
        return jsonify({'predictions': predictions,
                        'version': version,
                        'errors': 'errors'})
