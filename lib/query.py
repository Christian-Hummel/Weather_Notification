
import requests

URL = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Krems?unitGroup=us&key=PHNQBUCUXL9FLM4WBG3329EDB&contentType=json"
API_KEY = "PHNQBUCUXL9FLM4WBG3329EDB"

def query_current_weather_data(location: str) -> dict:
    """Construct a REST call to visualcrossing and query weather data for the given location.

    Args:
        location: Query target for current weather.

    Returns:
        Weather data as python dict

    """

    # TODO input all the necessary parameters for the REST query
    parameters = {
        "unitGroup": "metric",
        "": ""
    }

    response = requests.get(f"{URL}", params=parameters)
    print(response)
    if not response.ok:
        response.raise_for_status()

    return response.json()
