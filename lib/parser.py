
"""Open a csv file containing weather data and parse the current rain state.

    Args:
        path: Path to the csv file.

    Returns:
        Rain state as a string.

    """
import csv
def parse_current_rain_state(WEATHER_CSV_PATH: str) -> str:
    path = WEATHER_CSV_PATH


    with open(path, "r") as f:
        reader = csv.reader(f, delimiter=",")
        header = next(reader)
        for row in reader:
            preciptype = row[13]
            return preciptype
