import csv
from lib import parser


WEATHER_CSV_PATH = "data/weather.csv"




def run_weather_notification():
    rain_state = parser.parse_current_rain_state(WEATHER_CSV_PATH)
    print(rain_state)

    notification_doc = open("data/TODO.txt", "w")
    notification_doc.write(rain_state)
    notification_doc.close()



if __name__ == "__main__":
    run_weather_notification()
