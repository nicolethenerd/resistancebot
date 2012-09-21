# -*- coding: utf-8 -*-

"""
Message parsing

"""

import codecs
import re
import shlex

__all__ = ["parse_command", "parse_message"]


URL_REGEX_STRING = r"(?i)\b((?:[a-z][\w-]+:(?:/{1,3}|[a-z0-9%])|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?]))"
URL_REGEX = re.compile(URL_REGEX_STRING, re.U)

TAG_REGEX_STRING = r"(?:^|\s)[#]([\w-]+)"
TAG_REGEX = re.compile(TAG_REGEX_STRING, re.U)


def parse_command(content):
    # split into command and arguments
    
    try:
        byte_content = codecs.encode(content, 'utf-8')
        byte_tokens = shlex.split(byte_content, False, False)
        tokens = [codecs.decode(token, 'utf-8', 'replace') for token in byte_tokens]
    except Exception, e:
        tokens = content.split(' ')

    return (tokens[0], tokens[1:])


def parse_message(content):
    # parse message for urls and tags
    urls = [match[0] for match in URL_REGEX.findall(content)]
    
    tags = [match for match in TAG_REGEX.findall(content)]
    return (tags, urls)


