#! /bin/bash
echo "Packaging Weather for release..."
output="release"
mkdir -p $output/XBMC/plugins/weather
cp -r modules readme.txt $output
cp -r skin $output/XBMC
cp -r weather.plugin $output/XBMC/plugins/weather
zip -r $output/plugin.weather.zip $output/modules $output/XBMC $output/readme.txt
rm -r $output/modules $output/XBMC $output/readme.txt
echo "Finished!"
