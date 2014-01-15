# -*- coding: utf-8 -*-
import json

import resources.lib.web as web
import xbmc

from music import (Music, Artists, ArtistDetails, Albums, AlbumDetails, Genres,
                   Songs, SongDetails)


class WebApplication(web.application):
    """Allows us to specify what port we run on"""
    def run(self, port=8080, *middleware):
        func = self.wsgifunc(*middleware)
        return web.httpserver.runsimple(func, ('0.0.0.0', port))


URLS = (
    '/', 'RootHandler',
    '/music', 'Music',
    '/music/artists', 'Artists',
    '/music/artists/(.*)', 'ArtistDetails',
    '/music/albums', 'Albums',
    '/music/albums/(.*)', 'AlbumDetails',
    '/music/genres', 'Genres',
    '/music/songs', 'Songs',
    '/music/songs/(.*)', 'SongDetails'
)


class RootHandler(object):
    # TODO
    def GET(self):
        web.header('Content-Type', 'application/json')
        return json.dumps(URLS)


APP = WebApplication(URLS, globals())


if __name__ == "__main__":
    APP.run(port=31313)
