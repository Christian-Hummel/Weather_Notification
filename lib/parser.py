import csv
import json
NOTIFICATION_STRING = "today there will be "
NONE_STRING = "the weather will be alright today"


def parse_csv_rain_state(path: str) -> str:
    """Open a csv file containing weather data and parse the current rain state.

        Args:
            path: Path to the csv file.

        Returns:
            Rain state as a string.

        """
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
    with open(path, "r") as f:
        data = json.load(f)
        preciptype = data["days"][0]["preciptype"]
        return str(preciptype)

def parse_current_day_rain_state(weather_data: dict) -> str:
    preciptype = weather_data["preciptype"]
    return preciptype


def get_current_day_notification(weather_data: dict) -> str:
    preciptype = parse_current_day_rain_state(weather_data)
    if preciptype is None:
        return NONE_STRING

    return NOTIFICATION_STRING + " and ".join(preciptype)