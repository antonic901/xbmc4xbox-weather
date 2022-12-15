import os,sys,json
import xbmc, xbmcgui,xbmcaddon
import requests
from tools import get_dew_point_c, getUVIndex, getLocalizedDay, getLocalizedTempUnit, getLocalizedSpeedUnit, getLocalizedDistanceUnit
from api_key import API_KEY
from datetime import datetime

addon = xbmcaddon.Addon()

"""
This whole crap will be removed when I implement searching from XBMC Settings
"""
defaultLocation = "Location{}".format(addon.getSetting('default'))
locations = None
lat = lon = None
if addon.getSetting('use-from-xbmc') == 'false':
    try:
        file = open('special://profile/plugin_data/weather/weather.plugin/locations.json', 'r')
        json_input = file.read()
        file.close()
        locations = json.loads(json_input)
    except IOError:
        locations = {}

    try:
        lat = locations[defaultLocation]['lat']
        lon = locations[defaultLocation]['lon']
    except KeyError:
        lat, lon = sys.argv[1].split(';', 1)
else:
    lat, lon = sys.argv[1].split(';', 1)

API = addon.getSetting("api")
HEADERS = {'Content-Type':'application/json', 'accept': 'application/json', 'user-agent': 'xbox-weather'}
PARAMS = {
    'key': API_KEY,
    'q': "{},{}".format(lat,lon),
    'lang': xbmc.getRegion('locale'),
    'days': '7'
}

response = requests.get("{}/forecast.json".format(API), headers=HEADERS, params=PARAMS)
weather = response.json()
# weather = json.loads(open("{}\\test.json".format(os.getcwd())).read())

date = datetime.fromtimestamp(weather['current']['last_updated_epoch'])

WEATHER_WINDOW = xbmcgui.Window(12600)
WEATHER_WINDOW.setProperty("Location", "{}, {}".format(weather['location']['name'], weather['location']['country']))
WEATHER_WINDOW.setProperty("FromXBMC", addon.getSetting('use-from-xbmc').lower())

WEATHER_WINDOW.setProperty("Updated","{} {}".format(date.strftime(xbmc.getRegion('dateshort')), date.strftime(xbmc.getRegion('time'))))
WEATHER_WINDOW.setProperty("Updated", weather['current']['last_updated'])
WEATHER_WINDOW.setProperty("Current.Temperature", int(weather['current']['temp_{}'.format(getLocalizedTempUnit(xbmc.getRegion('tempunit')))]))
WEATHER_WINDOW.setProperty("Current.ConditionIcon", "http:{}".format(weather['current']['condition']['icon']))
WEATHER_WINDOW.setProperty("Current.Condition", weather['current']['condition']['text'])
WEATHER_WINDOW.setProperty("Current.FeelsLike", int(weather['current']['feelslike_{}'.format(getLocalizedTempUnit(xbmc.getRegion('tempunit')))]))
WEATHER_WINDOW.setProperty("Current.DewPoint", int(get_dew_point_c(weather['current']['feelslike_{}'.format(getLocalizedTempUnit(xbmc.getRegion('tempunit')))], weather['current']['humidity'])))
WEATHER_WINDOW.setProperty("Current.Humidity", "{}%".format(weather['current']['humidity']))
WEATHER_WINDOW.setProperty("Current.UVIndex", "{} ({})".format(getUVIndex(weather['current']['uv']), int(weather['current']['uv'])))
WEATHER_WINDOW.setProperty("Current.Wind", "{} {} {} {} {}".format(
    xbmc.getLocalizedString(407).title(), 
    weather['current']['wind_dir'],
    xbmc.getLocalizedString(408),
    int(weather['current']['wind_{}'.format(getLocalizedSpeedUnit(xbmc.getRegion('speedunit')))]),
    xbmc.getRegion('speedunit')
))

i = 0
for day in weather['forecast']['forecastday']:
    WEATHER_WINDOW.setProperty("Day{}.Title".format(i), getLocalizedDay(datetime.fromtimestamp(day['date_epoch']).strftime('%A')))
    WEATHER_WINDOW.setProperty("Day{}.OutlookIcon".format(i), "http:{}".format(day['day']['condition']['icon']))
    WEATHER_WINDOW.setProperty("Day{}.HighTemp".format(i), int(day['day']['maxtemp_{}'.format(getLocalizedTempUnit(xbmc.getRegion('tempunit')))]))
    WEATHER_WINDOW.setProperty("Day{}.LowTemp".format(i), int(day['day']['mintemp_{}'.format(getLocalizedTempUnit(xbmc.getRegion('tempunit')))]))
    WEATHER_WINDOW.setProperty("Day{}.Outlook".format(i), day['day']['condition']['text'])
    i = i + 1