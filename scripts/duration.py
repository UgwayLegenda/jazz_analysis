import pandas as pd
import json
from youtube_search import YoutubeSearch


with open(".venv/config.json") as f:
    config = json.load(f)

lyrics = pd.read_csv('data/lyrics_all.csv')
# Получим продолжительность треков
def get_youtube_duration(artist, title):
    try:
        results = YoutubeSearch(f"{artist} {title}", max_results=1).to_dict()
        return results[0]["duration"]
    except:
        return None

lyrics["duration"] = lyrics.apply(lambda row: get_youtube_duration(row["artist"], row["title"]), axis=1)
def convert_duration(duration):
    minutes = int(duration)
    seconds = round((duration - minutes) * 100)  # Извлекаем две цифры после точки
    return (minutes * 60)  + seconds

# Применяем функцию к колонке duration
lyrics["duration"] = lyrics["duration"].apply(convert_duration)

# Сохраняем результат в новый файл
lyrics.to_csv("lyr_dur1_sec.csv", index=False)
