import streamlit as st
import pandas as pd

st.set_page_config(page_title="EDA", page_icon="👨‍💻")

st.title('EDA')
df = pd.read_csv('dashboard/data/final_lyrics.csv')

df['len_lyr'] = df['lyrics'].apply(lambda x: len(x))

songs_len = df.groupby('artist')["len_lyr"].agg('mean')

x = st.selectbox('Среднюю длину песен какого исполнителя хотите посмотреть?', ['Frank Sinatra', 'Dean Martin', 'Nat “King” Cole', 'Louis Armstrong'])
st.write(f'Средняя длина песен(кол-во слов) {x} = `{songs_len[x]}`')

st.markdown('## Статистический датафрейм по продолжительности треков по исполнителям')


# Сделаем сводную таблицу с посчитанной средней, медианной, минимальной и максимальной продолжительностью
dur_df = df.groupby('artist')['duration'].agg(
    mean_duration='mean',
    median_duration='median',
    min_duration='min',
    max_duration='max'
).reset_index()


st.dataframe(dur_df)
st.markdown('---')
st.markdown('### Самый долгий и короткий трек исполнителя')

selected_artist = st.selectbox(
    'Выберите исполнителя',
    ['Frank Sinatra', 'Dean Martin', 'Nat “King” Cole', 'Louis Armstrong']
)

# Фильтруем данные по выбранному исполнителю
artist_df = df[df['artist'] == selected_artist]

if not artist_df.empty:
    # Находим самый длинный и короткий треки
    longest_idx = artist_df['duration'].idxmax()
    shortest_idx = artist_df['duration'].idxmin()

    # Получаем данные о треках
    longest_track = artist_df.loc[longest_idx, ['title', 'duration']]
    shortest_track = artist_df.loc[shortest_idx, ['title', 'duration']]

    # Форматируем вывод
    st.subheader(f"Результаты для {selected_artist}:")

st.metric(
    label="Самый длинный трек",
    value=longest_track['title'],
    help=f"Продолжительность: {longest_track['duration']} секунд"
)


st.metric(
    label="Самый короткий трек",
    value=shortest_track['title'],
    help=f"Продолжительность: {shortest_track['duration']} секунд"
)

st.markdown('---')