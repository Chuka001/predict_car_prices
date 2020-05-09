import json
import math

from regression_model.config import config
from regression_model.processing.data_management import load_dataset


def test_prediction_endpoint_validation_200(flask_test_client):
    # Given
    test_data = load_dataset(file_name=config.TESTING_DATA_FILE)
    test_data = test_data[0:1]
    post_json = test_data.to_json(orient='records')

    # When
    response = flask_test_client.post('/v1/predict/car_prices',
                                      json=post_json)

    # Then
    assert response.status_code == 200
    response_json = json.loads(response.data)
    prediction = response_json['predictions']
    assert prediction[0] >= 0
