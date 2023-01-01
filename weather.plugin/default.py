"""
    Quick overview of how weather plugins should be implemented:
        1. When XBMC calls weather plugins it will pass three sys arguments
        2. You can acces these arguments with sys.argv[i]:
            a) sys.argv[0] -> returns weather plugin id (id from addon.xml)
            b) sys.argv[1] -> returns areacode from XBMC in "lat;lon" format (ex. 40.50;-70.04)
            c) sys.argv[2] -> returns areacode index (1, 2 or 3). You can use this info to make plugin locations independant from XBMC locations
        3. Extract latitude and longitude from areacode and use that info to get weather data from some Weather API
        4. Get Weather window by calling "xbmcgui.Window(12600)" and then use setProperty("name", value) method to set properties of window with data you get from API

    INFO: Weather Window properties are dependent on Skin you are using. If skin is written wrong maybe some infos won't show.
          All official skins (PM3.HD, Project Mayhem, Confluence and Confluence Lite) should work without any problem.
"""
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
defaultLocation = None
if len(sys.argv) == 3:
    defaultLocation = "Location{}".format(sys.argv[2])
else:
    # fallback to default location from settings (used on XBMC4Xbox 3.5.3)
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
        # fallback to XBMC locations
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
for day in weather['forecast']['forecastday'][1:]:
    WEATHER_WINDOW.setProperty("Day{}.Title".format(i), getLocalizedDay(datetime.fromtimestamp(day['date_epoch']).strftime('%A')))
    WEATHER_WINDOW.setProperty("Day{}.OutlookIcon".format(i), "http:{}".format(day['day']['condition']['icon']))
    WEATHER_WINDOW.setProperty("Day{}.HighTemp".format(i), int(day['day']['maxtemp_{}'.format(getLocalizedTempUnit(xbmc.getRegion('tempunit')))]))
    WEATHER_WINDOW.setProperty("Day{}.LowTemp".format(i), int(day['day']['mintemp_{}'.format(getLocalizedTempUnit(xbmc.getRegion('tempunit')))]))
    WEATHER_WINDOW.setProperty("Day{}.Outlook".format(i), day['day']['condition']['text'])
    i = i + 1