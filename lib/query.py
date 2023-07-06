
import requests
import yaml

URL = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline"
def load_api_token():
    with open('weather.yaml', 'r') as file:
        config = yaml.safe_load(file)
        api_token = config['token']
        return api_token


def query_current_weather_data(location: str) -> dict:
    """Construct a REST call to visualcrossing and query weather data for the given location.

    Args:
        location: Query target for current weather.

    Returns:
        Weather data as python dict

    """

    parameters = {
        "datetime": "2023-03-14",
        "unitGroup": "us" ,
        "key": "PHNQBUCUXL9FLM4WBG3329EDB",
        "contentType": "json",

    }

    response = requests.get(f"{load_api_token()}/{location}", params=parameters)


    if not response.ok:
        response.raise_for_status()

    return response.json()




