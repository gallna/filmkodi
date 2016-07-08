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


import re,urlparse
from resources.lib.libraries import client
from resources.lib.libraries import control



def resolve(url):
    try:

        result = client.request(url, mobile=True)
        control.log('### VIDSPOT AAA' % result)
        url = re.compile('"file" *: *"(http.+?)"').findall(result)[-1]

        query = urlparse.urlparse(url).query
        url = url[:url.find('?')]
        url = '%s?%s&direct=false' % (url, query)
        return url
    except:
        return

def check(url):
    try:
        result = client.request(url)
        if result == None: return False

        result = client.parseDOM(result, 'b', attrs = {'class': 'err'})
        if any('Removed' in x for x in result): raise Exception()

        return True
    except:
        return False