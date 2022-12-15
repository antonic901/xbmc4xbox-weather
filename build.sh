#! /bin/bash
echo "Packaging Weather for release..."
mkdir release
mkdir release/out
cp -r weather.plugin modules "Confluence Lite" readme.txt release
zip -r release/out/plugin.weather.zip modules weather.plugin "Confluence Lite" readme.txt
echo "Finished!"
