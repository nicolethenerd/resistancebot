# -*- coding: utf-8 -*-

"""
Startgame handler

"""

import chatbot.dispatch


@chatbot.dispatch.handler("startgame")
def startgame_handler(params, *args, **kwargs):
    """
    get the current weather
    """
    print 'a'
    return "Starting game"

