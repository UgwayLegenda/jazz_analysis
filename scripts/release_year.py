import requests
import json
import pandas as pd

with open(".venv/config.json") as f:
    config = json.load(f)
DISCOGS_TOKEN = config["discogs_token"]


def get_discogs_year(artist, title):
    url = f"https://api.discogs.com/database/search?q={artist}+{title}&type=release"
    headers = {"Authorization": f"Discogs token={DISCOGS_TOKEN}"}

    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        return data["results"][0]["year"] if data["results"] else None
    except:
        return None

lyrics = pd.read_csv("C:\\Users\yaros\Downloads\lyr_dur1_sec.csv")
lyrics["year"] = lyrics.apply(lambda row: get_discogs_year(row["artist"], row["title"]), axis=1)

final_lyrics = lyrics.to_csv('final_lyrics', index=False)