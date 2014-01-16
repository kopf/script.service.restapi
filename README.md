# XBMC REST API

## Valid GET parameters

A list of valid GET parameters, and their usage.

* `albumartistsonly`: When set to `true`, exclude artists who only appear on compilations. Defaults to `false`.
* `fields`: A comma-separated list of extra fields to return, e.g. `born,died,genre`.
* `limit`: Limit the number of results returned by the API.
* `start`: Used for pagination. Skips a certain number of results, e.g. `300` means "beginning at the 300th result". Defaults to `0`.
* `sort`: Specify sorting order and field to sort by. The value `-artist` will sort by `artist`, in descending order, whereas the value `artist` will sort by `artist` in ascending order.
* `sort_ignorearticle`: When set to `true`, ignore grammatical articles ('the', 'a') at the beginning of strings by which we're sorting. Defaults to `false`.
* `filter`: Filter results returned by the api using an expression, e.g. `playcount is 0`

### GET /music

### GET /music/artists

_AudioLibrary.GetArtists_

Returns a list of artists. 

### GET /music/artists/`id`

_AudioLibrary.GetArtistDetails_

Returns details for a specific artist. 

### GET /music/albums

_AudioLibrary.GetAlbums_

Returns a list of albums.

### GET /music/albums/`id`

_AudioLibrary.GetAlbumDetails_

Returns details for a specific album.

### GET /music/genres

_AudioLibrary.GetGenres_

Returns a list of genres.

### GET /music/songs

_AudioLibrary.GetSongs_

Returns a list of songs.

### GET /music/songs/`id`

_AudioLibrary.GetSongDetails_

Returns details for a specific song.

