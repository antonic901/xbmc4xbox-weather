# Weather plugin for XBMC4Xbox
Finally we are close to fixing Weather in XBMC4Xbox! This is beta release and because of that expect bugs, errors and so on. Inside this document you will find instructions on how to install this plugin and how to use it. So lets begin!
![Weather](https://github.com/antonic901/xbmc4xbox-weather/blob/master/images/2.png?raw=true)
## Support
<a href="https://www.buymeacoffee.com/antonic901" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>
## Requirements
1. **[OPTIONAL]** Latest release of XBMC4Xbox. Version 3.5.3 should work, but 3.7 is recommended
2. You need to have **script.module.requests** inside **Q:\scripts\.modules**
3. If you don't have it you can find it inside **modules** folder of **plugin.weather.zip** you downloaded. Copy from **modules** script.module.requests to **Q:\scripts\.modules**
4. Restart your Xbox

## How to install
1. Extract archive **plugin.weather.zip**
2. Inside that archive you should find **XBMC** folder
3. Copy all files from **XBMC** folder to **Q:\** (XBMC4Xbox's root) and replace all files that it's telling you
4. Restart your Xbox. Turn it off completely and then turn it on again

## How to configure this plugin
1. Go to System -> Settings -> Weather
2. Select Weather plugin to be weather.plugin
3. Click Plugin settings
4. Click on Location 1, enter search query and select location. Do the same for for second and third location
5. ATTENTION!! After you selected all three locations click CANCEL. If you clik OK it won't remember anything. Don't ask me why :)
6. Open again Plugin settings and check are locations remembered.
7. Go to weather settings and after couple of seconds you should see weather data


## Info
If you don't know how to edit guisettings.xml then don't use Use locations from XMBC option. Before you can use this option you first need manually to edit Q:\UserData\guisettings.xml. How to do that:
1. First open guisettings.xml in your favorite text editor
2. Find <weather> section inside of which well be areacode1, areacode2, areacode3
3. Edit each arecode following this format: "lat;lon - location, country" (**ex. "40.25;20.29 - Novi Sad, Serbia"**)
4. Enable Use locations from XBMC in plugin settings

## Bugs
1. For some reason when using Confluence Lite skin weather won't automatically fetch. This problem is only presented in this skin. To fix it, open manually weather window

## Images
![Weather](https://github.com/antonic901/xbmc4xbox-weather/blob/master/images/3.png?raw=true)
![Weather](https://github.com/antonic901/xbmc4xbox-weather/blob/master/images/4.png?raw=true)
![Weather](https://github.com/antonic901/xbmc4xbox-weather/blob/master/images/1.png?raw=true)
![Weather](https://github.com/antonic901/xbmc4xbox-weather/blob/master/images/2.png?raw=true)
![Weather](https://github.com/antonic901/xbmc4xbox-weather/blob/master/images/5.png?raw=true)
![Weather](https://github.com/antonic901/xbmc4xbox-weather/blob/master/images/6.png?raw=true)
![Weather](https://github.com/antonic901/xbmc4xbox-weather/blob/master/images/7.png?raw=true)
![Weather](https://github.com/antonic901/xbmc4xbox-weather/blob/master/images/8.png?raw=true)
