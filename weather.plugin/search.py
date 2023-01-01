import sys, os, json
import xbmc, xbmcgui, xbmcaddon
import requests
from api_key import API_KEY

addon = xbmcaddon.Addon()
setting_id = sys.argv[1]

API = addon.getSetting("api")
HEADERS = {'Content-Type':'application/json', 'accept': 'application/json', 'user-agent': 'xbox-weather'}
PARAMS = {
    'key': API_KEY,
    'lang': xbmc.getRegion('locale')
}

def get_locations(input):
    locations = []
    for location in input:
        locations.append("{}, {}".format(location['name'], location['country']))
    return locations

def save(location):
    try:
        file = open('special://profile/plugin_data/weather/weather.plugin/locations.json', 'r')
        json_input = file.read()
        file.close()
        locations = json.loads(json_input)
    except IOError:
        locations = {}

    locations[setting_id] = {
        'lat': location['lat'],
        'lon': location['lon'],
        'name': location['name'],
        'country': location['country']
    }
    if not os.path.exists('special://profile/plugin_data/weather/weather.plugin'):
        '''
            this is some hackery :( 
            os.makedirs() fails to recursively create 'special://profile/plugin_data'
            so we first create plugin_data with os.mkdir() and then proceed with os.makedirs()
        '''
        os.mkdir('special://profile/plugin_data')
        os.makedirs('special://profile/plugin_data/weather/weather.plugin')
    file = open('special://profile/plugin_data/weather/weather.plugin/locations.json', 'w+')
    file.write(json.dumps(locations))
    file.close()


keyboard = xbmc.Keyboard()
keyboard.doModal()

if keyboard.isConfirmed() and  keyboard.getText() != '':
    PARAMS['q'] = keyboard.getText()
    response = requests.get("{}/search.json".format(API), headers=HEADERS, params=PARAMS)
    locations = response.json()
    # locations = response = json.loads(open("{}\\locations.json".format(os.getcwd())).read())
    if locations:
        dialog = xbmcgui.Dialog()
        selected = dialog.select(addon.getLocalizedString(100), get_locations(locations))
        if selected != -1:
            location = locations[selected]
            save(location)
            addon.setSetting(setting_id, "{}, {}".format(location['name'], location['country']))
        else:
            xbmc.executebuiltin('Notification({},{},5000,DefaultIconInfo.png)'.format(addon.getLocalizedString(101), addon.getLocalizedString(102)))
    else:
        xbmc.executebuiltin('Notification({},{},5000,DefaultIconInfo.png)'.format(addon.getLocalizedString(101), addon.getLocalizedString(103)))
else:
    xbmc.executebuiltin('Notification({},{},5000,DefaultIconInfo.png)'.format(addon.getLocalizedString(101), addon.getLocalizedString(101)))
