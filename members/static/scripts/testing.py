from api_fetch import SpotifyAPI
import cgi


form = cgi.FieldStorage()
searchterm = form.getvalue('searchbar')
headers = SpotifyAPI.get_headers(SpotifyAPI.get_access_token())


response = SpotifyAPI.return_tracks_by_string(headers, searchterm)
print(response)
