def test_car_prices_endpoint_returns_200(flask_test_client):
    # When
    response = flask_test_client.get('/car_prices')

    # Then
    assert response.status_code == 200
