# -*- coding: utf-8 -*-

"""
Startgame handler

"""

import pywapi

import chatbot.dispatch


@chatbot.dispatch.handler("startgame")
def startgame_handler(params, *args, **kwargs):
    """
    get the current weather
    """
    loc = "30342"
    if params:
        loc = " ".join(params)
    
    city = "Atlanta, GA"
    weather = pywapi.get_weather_from_google(loc)
    if weather and "current_conditions" in weather:
        current = weather["current_conditions"]
        
        if "forecast_information" in weather:
            forecast = weather["forecast_information"]
            city = forecast["city"]
        
        return u"{0} {1}\u00B0 F in {2}".format(current["condition"], current["temp_f"], city)

