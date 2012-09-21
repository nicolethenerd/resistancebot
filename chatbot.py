# -*- coding: utf-8 -*-

"""
Chatbot CLI

"""

import os
import sys

sys.path.insert(0, os.path.abspath("src/py2"))

import chatbot

def main():
    bot = chatbot.Bot()
    bot.connect_and_listen()

if __name__ == "__main__":
	main()
