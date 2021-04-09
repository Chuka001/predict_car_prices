This is an automated service that constantly updates the prediction model with happenings in the marketplace (fresh data is fetched from kaggle -- check shell script), so that at every point in time, users can get semi accurate prediction of the prices of proposed cars.

#API DOCUMENTATION

URL
https://car-price-prediction-service.herokuapp.com

Endpoints

GET '/version'
POST 'v1/predict/car_prices'

GET '/version'
- Fetches a dictionary of current model and API versions
- Methods: ['GET']
- sample response: {"api_version":"0.1.0","model_version":"2.0.0"}

POST 'v1/predict/car_prices'
- requests a json object with 25 keys
- sample request data: {
    "id": 7088811595,
    "url": "https:\\/\\/yakima.craigslist.org\\/cto\\/d\\/yakima-subaru-2003-wrx\\/7088811595.html",
    "region": "yakima",
    "region_url": "https:\\/\\/yakima.craigslist.org",
    "year": 2003,
    "manufacturer": "subaru",
    "model": "impreza sedan wrx",
    "condition": "good",
    "cylinders": "4 cylinders",
    "fuel": "gas",
    "odometer": 158000,
    "title_status": "clean",
    "transmission": "manual",
    "vin": null,
    "drive": "4wd",
    "size": "compact",
    "type": "sedan",
    "paint_color": "black",
    "image_url": "https:\\/\\/images.craigslist.org\\/01515_6AMGuH37NCT_600x450.jpg",
    "description": "Selling my wrx asking 5,100  158k miles  New lights and fog lights  Fresh oil change  Tranny and diff just serviced New battery  New tires  New radiator  New Brakes  Noting wrong with it serious inquires only  Vehicle was crashed! Got it inspected and they sent me a clean title! \\ufffc\\ufffc",
    "county": null,
    "state": "wa",
    "lat": 46.5934,
    "long": -120.531,
    "ori_cost_prc": 138671
}

- returns predictions as dictionaries
