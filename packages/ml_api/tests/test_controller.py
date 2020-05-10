from regression_model.config import config as model_config
from regression_model.processing.data_management import load_dataset
from regression_model import __version__ as _version
from api import __version__ as api_version
import json

def test_car_prices_endpoint_returns_200(flask_test_client):
    # When
    response = flask_test_client.get('/cars')

    # Then
    assert response.status_code == 200

def test_version_endpoint_returns_version(flask_test_client):
    # When
    response = flask_test_client.get('/version')

    # Then
    assert response.status_code == 200
    response_json = json.loads(response.data)
    assert response_json['model_version'] == _version
    assert response_json['api_version'] == api_version
    
def test_prediction_endpoint_returns_prediction(flask_test_client):
    # Given
    # test_data = load_dataset(file_name=model_config.TESTING_DATA_FILE)
    # post_json = test_data[0:1].to_json(orient='records')
    post_json = '{"id":7088811595,"url":"https:\\/\\/yakima.craigslist.org\\/cto\\/d\\/yakima-subaru-2003-wrx\\/7088811595.html","region":"yakima","region_url":"https:\\/\\/yakima.craigslist.org","year":2003,"manufacturer":"subaru","model":"impreza sedan wrx","condition":"good","cylinders":"4 cylinders","fuel":"gas","odometer":158000.0,"title_status":"clean","transmission":"manual","vin":null,"drive":"4wd","size":"compact","type":"sedan","paint_color":"black","image_url":"https:\\/\\/images.craigslist.org\\/01515_6AMGuH37NCT_600x450.jpg","description":"Selling my wrx asking 5,100  158k miles  New lights and fog lights  Fresh oil change  Tranny and diff just serviced New battery  New tires  New radiator  New Brakes  Noting wrong with it serious inquires only  Vehicle was crashed! Got it inspected and they sent me a clean title! \\ufffc\\ufffc","county":null,"state":"wa","lat":46.5934,"long":-120.531,"ori_cost_prc":138671}'

    # When
    response = flask_test_client.post('/v1/predict/car_prices',
                                      json=post_json)

    # Then
    assert response.status_code == 200
    response_json = json.loads(response.data)
    prediction = response_json['predictions']
    response_version = response_json['version']
    assert response_version == _version
