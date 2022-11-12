
from lib import parser
from lib import query

WEATHER_CSV_PATH = "data/weather.csv"
WEATHER_JSON_PATH = "data/weather.json"


def run_weather_notification():
    # rain_state = parser.parse_json_rain_state(WEATHER_JSON_PATH)
    weather_data = query.query_current_weather_data("Krems")
    print(weather_data)
    print("weather")


if __name__ == "__main__":
    run_weather_notification()
