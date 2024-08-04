
from lib import parser
from lib import query
from lib import messageparse

WEATHER_CSV_PATH = "data/weather.csv"
WEATHER_JSON_PATH = "data/weather.json"




def run_weather_notification():
    # rain_state = parser.parse_json_rain_state(WEATHER_JSON_PATH)
    weather_data = query.query_current_weather_data('location')
    notification = parser.get_current_day_notification(weather_data)
    print(notification)
    print(weather_data)
    message = messageparse.fetch_message()
    print(message)
    #messageparse.save_to_file(message)



if __name__ == "__main__":
    run_weather_notification()
