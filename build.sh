#! /bin/bash
echo "Packaging Weather for release..."
output="release"
mkdir -p $output/XBMC_3.5.3/plugins/weather $output/XBMC_3.5.3/skin $output/XBMC_3.7+/plugins/weather $output/XBMC_3.7+/skin
cp -r modules readme.txt $output
cp -r skin/3.5.3/* $output/XBMC_3.5.3/skin
cp -r skin/3.7+/* $output/XBMC_3.7+/skin
cp -r weather.plugin $output/XBMC_3.5.3/plugins/weather
cp -r weather.plugin $output/XBMC_3.7+/plugins/weather
zip -r $output/plugin.weather.zip $output/modules $output/XBMC_3.5.3 $output/XBMC_3.7+ $output/readme.txt
rm -r $output/modules $output/XBMC_3.5.3 $output/XBMC_3.7+ $output/readme.txt
echo "Finished!"
