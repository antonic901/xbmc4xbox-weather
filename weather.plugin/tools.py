# -*- coding: utf-8 -*-

import math
import xbmc

def get_dew_point_c(t_air_c, rel_humidity):
    A = 17.27
    B = 237.7
    alpha = ((A * t_air_c) / (B + t_air_c)) + math.log(rel_humidity/100.0)
    return (B * alpha) / (A - alpha)

def getUVIndex(value):
    if value >= 1 and value <= 2: return xbmc.getLocalizedString(391).title()
    if value >= 3 and value <= 5: return xbmc.getLocalizedString(392).title()
    if value >= 6 and value <= 7: return xbmc.getLocalizedString(393).title()
    if value >= 8 and value <= 10: return xbmc.getLocalizedString(393).title()
    if value >= 11: return xbmc.getLocalizedString(603).title()
    return 'Invalid'

def getLocalizedDay(value):
    days = {
        'Monday': xbmc.getLocalizedString(11),
        'Tuesday': xbmc.getLocalizedString(12),
        'Wednesday': xbmc.getLocalizedString(13),
        'Thursday': xbmc.getLocalizedString(14),
        'Friday': xbmc.getLocalizedString(15),
        'Saturday': xbmc.getLocalizedString(16),
        'Sunday': xbmc.getLocalizedString(17)
    }
    return days[value]

def getLocalizedTempUnit(value):
    temp = {
        '°C': 'c',
        '°F': 'f'
    }
    return temp[value]

def getLocalizedSpeedUnit(value):
    speedUnit = {
        'km/h': 'kph',
        'mph': 'mph'
    }
    return speedUnit[value]

def getLocalizedDistanceUnit(value):
    speedUnit = {
        'km/h': 'km',
        'mph': 'miles'
    }
    return speedUnit[value]