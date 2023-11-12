from api_fetch import SpotifyAPI

def getTrack(user_query):
        headers = SpotifyAPI.get_headers(SpotifyAPI.get_access_token())

        # SpotifyAPI.search_by_string(headers, "multilove")
        response = SpotifyAPI.return_tracks_by_string(headers, user_query)
        return response
    # pprint(searchTrack("Houdini"))
