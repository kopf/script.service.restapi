# XBMC REST API

## Valid GET parameters

A list of valid GET parameters, and their usage.

* `albumartistsonly`: When set to `true`, exclude artists who only appear on compilations. Defaults to `false`.
* `properties`: A comma-separated list of extra fields to return, e.g. `born,died,genre`.
* `limit`: Limit the number of results returned by the API.
* `start`: Used for pagination. Skips a certain number of results, e.g. `300` means "beginning at the 300th result". Defaults to `0`.
* `sort`: Specify sorting order and field to sort by. The value `-artist` will sort by `artist`, in descending order, whereas the value `artist` will sort by `artist` in ascending order.
* `sort_ignorearticle`: When set to `true`, ignore grammatical articles ('the', 'a') at the beginning of strings by which we're sorting. Defaults to `false`.
* `filter`: Filter results returned by the api using an expression, e.g. `playcount is 0`

### GET /music

### GET /music/artists

_AudioLibrary.GetArtists_

Returns a list of artists. 
