import requests, json
import time
import pytemperature


def get_weather_data():
    api_key = "1958cca04d95e453e5ce0c4fb7468a6e"
    base_url = "https://api.openweathermap.org/data/2.5/onecall?lat=42.36&lon=-71.06&exclude=minutely,hourly" \
               "&appid=" + api_key

    response = requests.get(base_url)
    xList = response.json()
    data = {}
    count = 1
    if xList:
        yList = xList["daily"]
        for y in yList:
            daytime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(y["dt"]))
            temp = y["temp"]
            morn = pytemperature.k2f(temp["morn"])
            eve = pytemperature.k2f(temp["eve"])
            night = pytemperature.k2f(temp["night"])
            mintemp = pytemperature.k2f(temp["min"])
            maxtemp = pytemperature.k2f(temp["max"])

            item = {"DAY/TIME": daytime, "MORNING (F)": morn, "EVENING (F)": eve, "NIGHT (F)": night, "MIN (F)": mintemp,
                    "MAX (F)": maxtemp}
            data[count] = item
            count += 1
    return data