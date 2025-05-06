import pandas as pd
import json
from youtube_search import YoutubeSearch



lyrics = pd.read_csv('/content/lyrics_all.csv')
def get_youtube_duration(artist, title):
    try:
        results = YoutubeSearch(f"{artist} {title}", max_results=1).to_dict()
        return results[0]["duration"]
    except:
        return None

lyrics["duration"] = lyrics.apply(lambda row: get_youtube_duration(row["artist"], row["title"]), axis=1)

def convert_duration(duration_str):
    if pd.isna(duration_str) or not isinstance(duration_str, str):
        return None
    try:
        # Разделяем строку на минуты и секунды
        parts = duration_str.split(':')
        if len(parts) == 1:
            return int(parts[0]) * 60  # Если только минуты
        elif len(parts) == 2:
            return int(parts[0]) * 60 + int(parts[1])
        else:
            return None
    except:
        return None

# Применяем функцию к колонке duration
lyrics["duration"] = lyrics["duration"].apply(convert_duration)

# Сохраняем результат в новый файл
lyrics.to_csv("lyr_dur1_sec.csv", index=False)

# Сохраняем результат в новый файл
lyrics.to_csv("lyr_dur1_sec.csv", index=False)
