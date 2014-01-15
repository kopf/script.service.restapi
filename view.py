import json

import xbmc

import resources.lib.web as web


class View(object):
    valid_params = []
    params = {}

    def execute(self):
        self._parse_params()
        web.header('Content-Type', 'application/json')
        return xbmc.executeJSONRPC(json.dumps({
           'jsonrpc': '2.0',
           'method': self.method,
           'params': self.params,
           'id': ''
        }))
