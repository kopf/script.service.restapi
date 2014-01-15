import resources.lib.web as web

from view import View


class MusicView(View):
    def _parse_params(self):
        """Parse params in the url / POST payload, generating a dict we can use
        in a JSON-RPC request to XBMC"""
        params = web.input()
        if 'albumartistsonly' in self.valid_params:
            self.params['albumartistsonly'] = params.get('albumartistsonly') == 'true'
        if 'properties' in self.valid_params and params.get('properties'):
            self.params['properties'] = params['properties'].split(',')
        if 'start' in self.valid_params:
            try:
                pagination_start = int(params.get('start', 0))
            except ValueError:
                raise web.badrequest('"start" must be an integer.')
            self.params['limits'] = {'start': pagination_start}
        if 'limit' in self.valid_params and 'limit' in params:
            try:
                self.params['limits']['end'] = pagination_start + int(params['limit'])
            except ValueError:
                raise web.badrequest('"limit" must be an integer.')
        if 'sort' in self.valid_params and 'sort' in params:
            self.params['sort'] = {
                "order": "descending" if params['sort'][0] == '-' else 'ascending',
                "method": params['sort'][1:],
                "ignorearticle": params.get('ignorearticle') == 'true'
            }
        if 'filter' in self.valid_params and params.get('filter'):
            # FIXME
            query = params['filter'].split(' ')
            self.params['filter'] = {
                'field': query[0],
                'operator': query[1],
                'value': ' '.join(query[2:])
            }


class Music(MusicView):
    def GET(self):
        # TODO
        return ''


class Artists(MusicView):
    valid_params = ['albumartistsonly', 'properties', 'limit', 'start', 'sort', 'filter']

    def GET(self):
        self.method = 'AudioLibrary.GetArtists'
        return self.execute()


class ArtistDetails(MusicView):
    pass


class Albums(MusicView):
    pass


class AlbumDetails(MusicView):
    pass


class Genres(MusicView):
    pass


class Songs(MusicView):
    pass


class SongDetails(MusicView):
    pass
