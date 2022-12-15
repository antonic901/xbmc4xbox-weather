Finally we are close to fixing Weather in XBMC4Xbox! This is beta release and because of that expect bugs, errors and so on. Inside this document you will find instructions on how to install this plugin and how to use it. So lets begin!

## How to install
1. Extract archive weather-beta.zip
2. Inside that archive you should find two folder, Confluence Lite and weather.plugin
3. Copy Confluence Lite to Q:\skin and replace all files that it's telling you
4. Copy weather.plugin to Q:\plugins\weather\. If weather folder doesn't exist create one
5. Restart your Xbox. Turn it off completely and the turn it on again

## How to configure this plugin
1. Go to System -> Settings -> Weather
2. Select Weather plugin to be weather.plugin
3. Click Plugin settings
4. Click on Location 1, enter search query and select location. Do the same for for second and third location
5. ATTENTION!! After you selected all three locations click CANCEL. If you clik OK it won't remeber anything. Don't ask me why :)
6. Open again Plugin settings and check are locations remembered.
7. Select default location and now click OK.
8. Go to weather settings and after couple of seconds you should see weather data


## Info
If you don't know how to edit guisettings.xml then don't use Use locations from XMBC option. Before you can use this option you first need manually to edit Q:\UserData\guisettings.xml. How to do that:
1. First open guisettings.xml in your favorite text editor
2. Find <weather> section inside of which well be areacode1, areacode2, areacode3
3. Edit each arecode following this format: "lat;lon - location, country" (ex. "40.25;20.29 - Novi Sad, Serbia")
4. Enable Use locations from XBMC in plugin settings
