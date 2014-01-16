import resources.lib.web as web

from view import View


class MusicView(View):
    def _parse_params(self, valid_params):
        """Parse params in the url / POST payload, generating a dict we can use
        in a JSON-RPC request to XBMC"""
        params = web.input()
        retval = {}
        if 'albumartistsonly' in valid_params:
            retval['albumartistsonly'] = params.get('albumartistsonly') == 'true'
        if 'fields' in valid_params and params.get('fields'):
            retval['properties'] = params['fields'].split(',')
        if 'start' in valid_params:
            try:
                pagination_start = int(params.get('start', 0))
            except ValueError:
                raise web.badrequest('"start" must be an integer.')
            retval['limits'] = {'start': pagination_start}
        if 'limit' in valid_params and 'limit' in params:
            try:
                retval['limits']['end'] = pagination_start + int(params['limit'])
            except ValueError:
                raise web.badrequest('"limit" must be an integer.')
        if 'sort' in valid_params and 'sort' in params:
            retval['sort'] = {
                "order": "descending" if params['sort'][0] == '-' else 'ascending',
                "method": params['sort'][1:],
                "ignorearticle": params.get('ignorearticle') == 'true'
            }
        if 'filter' in valid_params and params.get('filter'):
            # FIXME
            query = params['filter'].split(' ')
            retval['filter'] = {
                'field': query[0],
                'operator': query[1],
                'value': ' '.join(query[2:])
            }
        return retval


class Music(MusicView):
    def GET(self):
        # TODO
        return ''


class Artists(MusicView):
    def GET(self):
        method = 'AudioLibrary.GetArtists'
        valid_params = ['albumartistsonly', 'fields', 'limit', 'start', 'sort', 'filter']
        params = self._parse_params(valid_params)
        return self.execute(method, params)


class ArtistDetails(MusicView):
    def GET(self, artist_id):
        method = 'AudioLibrary.GetArtistDetails'
        valid_params = ['fields']
        params = self._parse_params(valid_params)
        try:
            params['artistid'] = int(artist_id)
        except ValueError:
            raise web.badrequest('Artist ID must be an integer.')
        return self.execute(method, params)


class Albums(MusicView):
    def GET(self):
        method = 'AudioLibrary.GetAlbums'
        valid_params = ['fields', 'limit', 'start', 'sort', 'filter']
        params = self._parse_params(valid_params)
        return self.execute(method, params)


class AlbumDetails(MusicView):
    def GET(self, album_id):
        method = 'AudioLibrary.GetAlbumDetails'
        valid_params = ['fields']
        params = self._parse_params(valid_params)
        try:
            params['albumid'] = int(album_id)
        except ValueError:
            raise web.badrequest('Album ID must be an integer.')
        return self.execute(method, params)


class Genres(MusicView):
    def GET(self):
        method = 'AudioLibrary.GetGenres'
        valid_params = ['fields', 'limit', 'start', 'sort']
        params = self._parse_params(valid_params)
        return self.execute(method, params)


class Songs(MusicView):
    def GET(self):
        method = 'AudioLibrary.GetSongs'
        valid_params = ['fields', 'limit', 'start', 'sort', 'filter']
        params = self._parse_params(valid_params)
        return self.execute(method, params)


class SongDetails(MusicView):
    def GET(self, song_id):
        method = 'AudioLibrary.GetSongDetails'
        valid_params = ['fields']
        params = self._parse_params(valid_params)
        try:
            params['songid'] = int(song_id)
        except ValueError:
            raise web.badrequest('Song ID must be an integer.')
        return self.execute(method, params)
