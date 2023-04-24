import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

URL = "https://www.billboard.com/charts/hot-100/"
CLIENT_ID = "20d97be65b17430a84782ffdfc8605a6"
CLIENT_SECRET = "733f72884b9646b5a519cb0b0bf84090"


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_date = input("Please enter the date that you wish to travel back to in the format YYYY-MM-DD: ")


response = requests.get(URL+user_date)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

song_names_html = soup.find_all(name="h3", id="title-of-a-story", class_="c-title")

song_names = []

for ana in soup.findAll(name="h3", id="title-of-a-story", class_="c-title"):
  if ana.parent.name == 'li' :
    song_names.append(ana.text.strip())

user_id = sp.current_user()["id"]
print(user_id)





song_uris = []
year = user_date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{user_date} Billboard 100", public=False)
print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
