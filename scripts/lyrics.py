import json
import lyricsgenius
import pandas as pd
from lyricsgenius import Genius
import re
import time


def clean_genius_lyrics(text):
    # Удаляем все технические блоки перед текстом песни
    text = re.sub(
        r'^(\d+\s*Contributors|.*?Lyrics\b).*?\n',
        '',
        text,
        flags=re.IGNORECASE | re.DOTALL | re.MULTILINE
    )

    # Удаляем Read More и всё до него
    text = re.split(r'Read More\s*\n', text, flags=re.IGNORECASE)[-1]

    # Дополнительные паттерны
    patterns = [
        r'Genius Annotation.*',
        r'You might also like.*',
        r'Embed\s*\d+',
        r'\xa0',
        r'^[\W\d_]+$'  # Удаляем строки из спецсимволов/чисел
    ]

    for pattern in patterns:
        text = re.sub(pattern, '', text, flags=re.IGNORECASE | re.DOTALL)

    # Финальная очистка
    text = "\n".join([line.strip() for line in text.split("\n") if line.strip()])
    return text.strip()
with open(".venv/config.json") as f:
    config = json.load(f)

genius = lyricsgenius.Genius(config["genius_token"])
genius.remove_section_headers = True
artists = ['Frank Sinatra', 'Dean Martin', 'Nat "King" Cole', 'Louis Armstrong']

all_songs = []

for artist in artists:
    try:
        if artist != 'Nat "King" Cole':
            artist_obj = genius.search_artist(artist, max_songs = 50, sort='popularity')
            for song in artist_obj.songs:
                all_songs.append({
                    'artist': song.artist,
                    'title': song.title,
                    'lyrics': clean_genius_lyrics(song.lyrics)
            })
        else:
            artist_obj = genius.search_artist(artist, max_songs=16, sort='popularity')
            for song in artist_obj.songs:
                all_songs.append({
                    'artist': song.artist,
                    'title': song.title,
                    'lyrics': clean_genius_lyrics(song.lyrics)
                })
    except:
        print(f'Ошибка для {artist}')

lyrics = pd.DataFrame(all_songs)
lyrics = lyrics.drop_duplicates(subset=['artist', 'title', 'lyrics'])
lyrics_csv = lyrics.to_csv('lyrics_all.csv',sep=',', index= False )
