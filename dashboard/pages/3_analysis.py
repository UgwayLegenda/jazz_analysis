import streamlit as st
import pandas as pd
from spacy.lang.en.stop_words import STOP_WORDS
from sklearn.feature_extraction.text import TfidfVectorizer
import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
import plotly.graph_objects as go
import numpy as np

st.set_page_config(page_title="Analysis", page_icon="📉")

df = pd.read_csv('dashboard/data/lyrics_for_analysis1.csv')
st.title('Анализ текста песен')
st.markdown('Наш обработанный датафрейм(проведена первоначальная очистка и лемматизация):')
st.dataframe(df)


st.markdown('## Облако слов')


def generate_wordcloud(artist_name=None, df=None,
                       background_color='white',
                       colormap='viridis',  # Фиксированная цветовая схема
                       max_words=100,
                       figsize=(12, 8)):
    """
    Генерирует облако слов с фиксированной цветовой схемой
    """
    # Фильтрация данных
    if artist_name:
        data = df[df['artist'] == artist_name]['lemmatized_text']
        if data.empty:
            st.error(f"Исполнитель '{artist_name}' не найден в данных.")
            return None
    else:
        data = df['lemmatized_text']

    # Объединение текстов в одну строку
    all_text = ' '.join(data.astype(str))

    # Подсчет частоты слов
    word_freq = Counter(all_text.split())

    # Генерация облака
    wordcloud = WordCloud(
        width=figsize[0] * 100,
        height=figsize[1] * 100,
        background_color=background_color,
        colormap=colormap,
        max_words=max_words
    ).generate_from_frequencies(word_freq)

    # Создание фигуры
    fig = plt.figure(figsize=figsize)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')

    if artist_name:
        plt.title(f'Облако слов для {artist_name}', fontsize=14, pad=20)
    else:
        plt.title('Облако слов для всех исполнителей', fontsize=14, pad=20)

    return fig


# Получаем список всех исполнителей
artists = ['По всем исполнителям'] + sorted(df['artist'].unique().tolist())

# Интерфейс Streamlit
st.title('Интерактивное облако слов')

cloud_choice = st.selectbox(
    'Выберите для кого показать облако слов:',
    artists
)

# Выбор параметров
max_words = st.slider(
    'Максимальное количество слов:',
    min_value=50,
    max_value=200,
    value=100
)

# Генерация облака
if cloud_choice == 'По всем исполнителям':
    fig = generate_wordcloud(df=df, max_words=max_words)
else:
    fig = generate_wordcloud(artist_name=cloud_choice, df=df, max_words=max_words)

# Отображение результатов
if fig:
    st.pyplot(fig)
else:
    st.warning('Не удалось сгенерировать облако слов')






st.markdown('## Встречаемость по частям речи')

pos_df = pd.read_csv('dashboard/data/pos_analysis1.csv')
pos_categories = ['noun', 'verb', 'adj', 'adv']
pos_choice = st.selectbox(
    'Выберете часть речи:',
    pos_categories
)
n_words = st.slider(
    'Количество отображаемых слов:',
    min_value=5,
    max_value=20,
    value=20
)
# Фильтрация данных по выбранной части речи
filtered_df = pos_df[pos_df['part_of_speech'] == pos_choice].head(n_words)

# Создание интерактивного графика
fig1 = px.bar(
    filtered_df,
    x='frequency',
    y='word',
    orientation='h',
    title=f'Топ {n_words} самых частых {pos_choice}',
    labels={'frequency': 'Частота', 'word': 'Слово'},
    color='frequency',
    color_continuous_scale='Blues'
)

# Настройка внешнего вида
fig1.update_layout(
    yaxis={'categoryorder': 'total ascending'},  # Сортировка по частоте
    height=600,
    showlegend=False,
    margin=dict(l=50, r=50, t=50, b=50)
)

# Отображение графика в Streamlit
st.plotly_chart(fig1, use_container_width=True)



st.markdown('## Характерные слова')

# Группировка по исполнителям и объединение в одну строку
grouped = df.groupby('artist')['lemmatized_text'].agg(' '.join).reset_index()


custom_stop_words = [
    "gobble", "bidee", "ve", "ll", "oh", "ya", "ain", "don", "didn", "te", "fasule", "tay", "ce",
    "la", "em", "di", "il", "er", "de", "to", "ba", "da", "doo", "zee", "boo", "mmm", "ho", "ti", "to"]

# Расширим стоп-слова
STOP_WORDS.update(custom_stop_words)
# Создание TF-IDF матрицы
vectorizer = TfidfVectorizer(max_features=1000, stop_words = list(STOP_WORDS))   # Не забываем про расширенный набор стоп-слов
tfidf_matrix = vectorizer.fit_transform(grouped['lemmatized_text'])

# Датафрейм с весами TF-IDF
tfidf_df = pd.DataFrame(
    tfidf_matrix.toarray(),
    columns=vectorizer.get_feature_names_out(),
    index=grouped['artist']
)

# Элементы интерфейса
artists = grouped['artist'].unique()
selected_artist = st.selectbox('Выберите исполнителя', artists)
n_words = st.slider('Количество отображаемых слов', 5, 20, 10)

# Палитры и настройки цвета
artist_palettes = {
    'Nat “King” Cole': px.colors.sequential.YlOrBr,
    'Frank Sinatra': px.colors.diverging.RdYlGn,
    'Dean Martin': px.colors.sequential.PuBu,
    'Louis Armstrong': px.colors.sequential.Cividis
}


def create_interactive_plot(artist, n=10):
    # Получаем топ-слов и сортируем для правильного отображения
    top_words = tfidf_df.loc[artist].nlargest(n)
    top_words = top_words.sort_values(ascending=False)

    # Создаем DataFrame для Plotly
    plot_df = pd.DataFrame({
        'Слово': top_words.index,
        'Вес TF-IDF': top_words.values
    })

    # Выбираем палитру
    colors = artist_palettes.get(artist, px.colors.qualitative.Pastel)

    # Создаем интерактивный график
    fig = px.bar(
        plot_df,
        x='Вес TF-IDF',
        y='Слово',
        orientation='h',
        color='Слово',
        color_discrete_sequence=colors,
        text='Вес TF-IDF',
        height=600
    )

    # Настраиваем оформление
    fig.update_layout(
        title={
            'text': f"Топ-{n} характерных слов для {artist}",
            'y': 0.95,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        xaxis_title="Вес TF-IDF",
        yaxis_title="Слово",
        showlegend=False,
        hovermode='closest',                  # подсказка
        margin=dict(l=100, r=50, t=80, b=50), # отступы
        font=dict(size=12)
    )

    # Форматируем подписи
    fig.update_traces(
        texttemplate='%{text:.3f}',
        textposition='outside'
    )

    return fig


# Отображение графика
if selected_artist in tfidf_df.index:
    plot = create_interactive_plot(selected_artist, n_words)
    st.plotly_chart(plot, use_container_width=True)
else:
    st.error("Выбранный исполнитель не найден в данных")