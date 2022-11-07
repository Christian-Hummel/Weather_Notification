import csv
from lib import parser


WEATHER_CSV_PATH = "data/weather.csv"
WEATHER_JSON_PATH = "data/weather.json"


def run_weather_notification():
    rain_state = parser.parse_json_rain_state(WEATHER_JSON_PATH)
    print(rain_state)

    notification_doc = open("data/TODO.txt", "w")
    notification_doc.write(rain_state)
    notification_doc.close()


if __name__ == "__main__":
    run_weather_notification()
