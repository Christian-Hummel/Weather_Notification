import csv
from lib import parser



with open("data/weather.csv", "r") as infile:
    reader = csv.reader(infile, delimiter=",")
    header = next(reader)
    for row in reader:
        preciptype = row[13]
        print(preciptype)


"""
def parse_current_rain_state(WEATHER_CSV_PATH) -> str
    WEATHER_CSV_PATH = "data/weather.csv"

def run_weather_notification():
    rain_state = parser.parse_current_rain_state(WEATHER_CSV_PATH)
    print(rain_state)


if __name__ == "__main__":
    run_weather_notification()
"""