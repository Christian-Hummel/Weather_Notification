
"""Open a csv file containing weather data and parse the current rain state.

    Args:
        path: Path to the csv file.

    Returns:
        Rain state as a string.

    """
import csv
import json



def parse_csv_rain_state(path: str) -> str:



    with open(path, "r") as f:
        reader = csv.reader(f, delimiter=",")
        header = next(reader)
        first_line = next(reader)
        preciptype_index = header.index('preciptype')
        preciptype = first_line[preciptype_index]
        return preciptype


def parse_json_rain_state(path: str) -> str:
    """Open a json file containing weather data and parse the current rain state.

    Args:
        path: Path to the json file.

    Returns:
        Rain state as a string.

    """
    with open("data/weather.json", "r") as f:
        data = json.load(f)
        preciptype = data["days"][0]["preciptype"]
        return preciptype


