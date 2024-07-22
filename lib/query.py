
import requests
import yaml
from datetime import datetime, date

URL = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline"

def load_api_location():
    with open('conf/weather.yaml', 'r') as file:
        config = yaml.safe_load(file)
        location = config['location']
        return location

def load_api_token():
    with open('conf/weather.yaml', 'r') as file:
        config = yaml.safe_load(file)
        token = config['token']
        return token




def query_current_weather_data(location: str) -> dict:
    """Construct a REST call to visualcrossing and query weather data for the given location.

    Args:
        location: Query target for current weather.

    Returns:
        Weather data as python dict

    """









    parameters = {
        "location": load_api_location(),
        "datetime": date.isoformat(date.today()),
        "unitGroup": "us" ,
        "key": load_api_token(),
        "contentType": "json",

    }



    response = requests.get(f"{URL}", params=parameters)


    if not response.ok:
        response.raise_for_status()

    return response.json()