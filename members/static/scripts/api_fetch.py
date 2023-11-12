import requests
import json
import constants
from pprint import pprint

class SpotifyAPI():
    """ methods relating to GET and POST calls made to the spotify API."""

    def get_access_token():
        """
        Use the client and secret ids to request an access token
        """
        CLIENT_ID = constants.CLIENT_ID
        CLIENT_SECRET = constants.CLIENT_SECRET
        AUTH_URL = 'https://accounts.spotify.com/api/token'

        auth_response = requests.post(AUTH_URL, {
            'grant_type': 'client_credentials',
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        })
        response_data = auth_response.json()
        pprint(response_data)
        access_token = response_data['access_token']
        # print(access_token)
        return access_token

    def get_headers(access_token):
        """
        Use the access token to create the headers for each API call.
        """
        headers = {'Authorization': 'Bearer {token}'.format(token=access_token)}
        # print(headers)
        return headers

    def return_tracks_by_string(headers, query):
        """
        Calls the Spotify Search API using the query string set by the user. Returns just the necessary information
        depending on the output type. (tracks, artists, albums)
        """
        query = query.replace(" ", "+")
        URL = 'https://api.spotify.com/v1/search?q=' + query + '&type=album%2Cartist%2Ctrack'
        payload = json.dumps({'name': query, 'limit': 10})
        response = requests.get(URL, headers=headers, params=payload)
        # print(response.text)
        response_data = response.json()

        tracks = {}
        for track in response_data['tracks']['items']:
            # tracks[f"THIS IS A NEW TRACK RIGHT HERE {track['name']}"] = track
            tracks[track['id']] = {
                'name': track['name'],
                'artist': track['artists'][0]['name'],
                'url': 'https://open.spotify.com/track/' + track['id'],
                'img': track['album']['images'][-1]['url']
            }
        return tracks

    def print_search_by_string(headers, query):
        """
        Calls the Spotify Search API using the query string set by the user. Returns just the necessary information
        depending on the output type. (tracks, artists, albums)
        """
        query = query.replace(" ", "+")
        URL = 'https://api.spotify.com/v1/search?q=' + query + '&type=album%2Cartist%2Ctrack'
        payload = json.dumps({'name': query, 'limit': 10})
        response = requests.get(URL, headers=headers, params=payload)
        # print(response.text)
        response_data = response.json()

        for r in response_data['tracks']['items']:
            print(f"\nName: {r['name']}")
            print(f"Type: Track")
            print("Artists:")
            for artist in r['artists']:
                print(f"    {artist['name']}")
            print(f"Spotify Link: {r['external_urls']['spotify']}")
            print("Image HREFs:")
            for image in r['album']['images']:
                print(f"    {image['url']}, ({image['width']}x{image['height']})")

        for r in response_data['artists']['items']:
            print(f"\nName: {r['name']}")
            print("Type: Artist")
            print(f"Spotify Link: {r['external_urls']['spotify']}")
            print("Image HREFs:")
            for image in r['images']:
                print(f"    {image['url']}, ({image['width']}x{image['height']})")

        for r in response_data['albums']['items']:
            print(f"\nName: {r['name']}")
            print("Type: Album")
            print("Artists:")
            for artist in r['artists']:
                print(f"    {artist['name']}")
            print(f"Spotify Link: {r['external_urls']['spotify']}")
            print("Image HREFs:")
            for image in r['images']:
                print(f"    {image['url']}, ({image['width']}x{image['height']})")

        print(f"\n\nNot finding what you're looking for? Adjust your search and try again.")


    def get_track_features(headers, track_id):
        """ 
        Returns the track features of any given track id.
        """
        url = 'https://api.spotify.com/v1/audio-features/' + track_id
        request = requests.get(url, headers=headers)
        print(request.text)
        request_data = request.json()
        return request_data