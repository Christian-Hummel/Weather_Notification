
import requests

URL = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest"


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

    more_url_info = ""  # TODO delete this variable and complete the URL string below instead
    response = requests.get(f"{URL}/{more_url_info}", params=parameters)

    if not response.ok:
        response.raise_for_status()

    return response.json()
