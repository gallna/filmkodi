# -*- coding: utf-8 -*-

'''
    FanFilm Add-on
    Copyright (C) 2016 mrknow

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''


import re,json,urllib
from resources.lib.libraries import client


def resolve(url):
    try:
        result = client.source(url)
        vid = url.split('public')[-1]
        token = re.compile('"tokens":{"download":"([^"]+)"}').findall(result)[0]
        weblink = re.compile('"weblink_get":\[{"count":\d+,"url":"([^"]+)"}\]').findall(result)[0]
        if len(token) > 0 and len(weblink) > 0:
            url = weblink + vid + '?key=' + token
        return url
    except:
        return

