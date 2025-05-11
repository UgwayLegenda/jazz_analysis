import streamlit as st
import pandas as pd
import plotly
import plotly.express as px


st.set_page_config(page_title="Data", page_icon="📊")
st.title('Data')
df = pd.read_csv('dashboard/data/final_lyrics.csv')

st.write('**Наш датафрейм:**')
st.dataframe(df)

st.write(f' Количество записей: {len(df)}')
st.write(f' Количество пропусков года: {len(df[df.year.isna()])}')

# Подсчет песен по исполнителям
artist_counts = df["artist"].value_counts().reset_index()
artist_counts.columns = ["artist", "songs"]


# Создание интерактивного pie-chart
fig = px.pie(
    artist_counts,
    values="songs",
    names="artist",
    hole=0.3,
    color_discrete_sequence=px.colors.qualitative.Pastel,
    title="Доля песен каждого исполнителя"
)

# Настройка отображения значений
fig.update_traces(
    textposition="inside",       # Текст внутри
    textinfo="percent+label",    # Исполнитель + его доля
    hovertemplate="<b>%{label}</b><br>Песен: %{value}"    # подсказка(при наведении)
)

# Отображение в Streamlit
st.plotly_chart(fig, use_container_width=True)

# Распределение продолжительности
st.write('**Распределение продолжительности треков по исполнителям**')
fig2 = px.histogram(
    df,
    x='duration',
    color='artist',
    nbins=20,
    opacity=0.7,
    barmode='group',
    title='Распределение продолжительности',
    labels={'duration': 'Длительность (секунды)', 'count': 'Количество треков'}
)

fig2.update_layout(
    plot_bgcolor='black',
    hoverlabel=dict(bgcolor='grey'), # сделаем заливку фона подсказок белой
    legend_title='Исполнитель',
    title_x=0.5,
    xaxis=dict(showgrid=True),
    yaxis=dict(showgrid=True)
)

fig2.update_traces(
    hovertemplate='Длительность: %{x:.1f} секунд<br>Треков: %{y}' # <br> - элемент переноса строки в html, чтобы при наведении подсказка отображалась приятнее
)

st.plotly_chart(fig2, use_container_width=True)
