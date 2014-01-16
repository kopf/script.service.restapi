import json

import xbmc

import resources.lib.web as web


class View(object):

    def execute(self, method, params):
        web.header('Content-Type', 'application/json')
        print 'RESTAPI PASSING PARAMS', params
        return xbmc.executeJSONRPC(json.dumps({
           'jsonrpc': '2.0',
           'method': method,
           'params': params,
           'id': ''
        }))
