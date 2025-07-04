import streamlit as st
import pandas as pd

st.set_page_config(page_title="Conclusion", page_icon="🪄")
st.title('Выводы & рекомендации')


freq = st.markdown(""" ## Выводы по анализу частоты слов:
Чаще всего именно **существительные** являются центральными словами в песнях, поскольку именно существительные выступают темой и главным лейтмотивом тех или иных песен. Как ни странно и предсказуемо, именно "love" (любовь) лидирует в топ-20 слов среди существительных. Будучи одной из главных тем песен любой эпохи, в эпоху джаза любовь остается самым распространенным словом - свыше 200 упоминаний среди существительных. Это также самое распространенное слово в джазовых песнях в целом.

***Однако!*** Не стоит забывать про то, что "love" - также и глагол. Пускай это и не отменяет остальных наблюдений, даже так "love" имеет вдвое больше упоминаний, чем "way", как второй глагол. Вместе с существительным вариантом, "love" является САМЫМ распространенным словом среди всех четырех топов.

Из прилагательных - стоит отметить, что почти все они, кроме двух (low, cold) имеют так или иначе положительный окрас. Наличие этих двоих слов в топе, учитывая их относительно небольшое количество (около 15 у каждого) может либо значить использование подобных слов в качестве контраста в песнях, либо то, что они встречаются лишь в небольшом количестве песен. В остальном, положительный окрас большинства прилагательных можно связать с двумя вещами: либо то, что как жанр, сам по себе джаз в основном поднимает темы с положительным окрасом, вроде любви, счастья, верности, и сами песни поэтому имеют положительный окрас. Либо это можно связать с социокультурным явлением послевоенной "золотой эпохи" и экономическим процветанием США. Закат эры свинга как музыкального жанра пришелся на первую половину сороковых, в то время как джаз захватил популярность и стал главным музыкальным жанром США как раз к второй половине сороковых и оставался таким вплоть до шестидесятых.

В анализе глаголов стоит отметить глагол "let" - в то время, как сами поставленные нами условия это не нарушает, одной из двух пересекающихся песен, помимо "Blue Moon", является "Let it Snow" с 25 упоминаниями глагола "let". Учитывая известность обоих вариантов этих песен, как и в случае с "Blue Moon", для общего проекта это не является особо большой проблемой. В остальном глаголы и наречания не представляют особого интереса, и особо ничего не сообщают.
"""
)
tfidf = st.markdown(""" ## Анализ характерных слов:
Данные столбчатые диаграммы демонстрируют частоту упоминания слов по песням каждого из отдельно взятых исполнителей на основе TF-IDF. Самым интересным фактом, пожалуй, следует отметить, что для трех из четырех исполнителей самым характерным и часто используемым остается слово "love", любовь. Не важно, используется оно в роли существительного или глагола, однако встречается оно значительно чаще других.

И только Луи Армстронг предпочитает любви вкусные чизкейки - вес этого слова у него выше 0.40, что, по меркам IDF, весьма много. Единственный, у кого главное слово имеет схожий вес - Нэт Кинг Коул. В частности, можно заметить, что вес у "love" в его случае также заметно выше 0.40 и ближе к 0.50, однако тут следует учитывать саму формулу TF-IDF, а также то, что в его случае выборка в почти три раза меньше, чем у остальных музыкантов, и анализ не может считаться полностью правдоподобным и корректным.

Отдельно также выделяется Дин Мартин - в топе его характерных слов встречаются не только напевы "bon" и "boom", но и иностранное "si", присутсвовавшее в двух песнях, "C'est si bon", и "Mambo Italliano".
"""
)
tfidf = st.markdown(""" ## Самые длинные и короткие треки, средняя продолжительность треков:
Самым длинным треком отмечена стерео-рендиция трека "I've Got A Crush On You" Фрэнка Синатры, однако относительно анализа это неверная информация: длина этой песни в обычном исполнении составляет всего 2 минуты, поэтому самым длинным треком из анализа по-праву достойна называться Let's Do It от Луи Армстронга, длиной в 524 секунды. В среднем разные записи этой песни идут около 8 с половиной минут, но длина может отличаться на пару секунд в зависимости от трека.

Луи Армстронгу также принадлежит один из двух самых коротких треков в подборке, с продолжительностью всего в 106 секунд: Bill Bailey, Won’t You Please Come Home. Он делит это место с Нэтом "Кингом" Коулом и его треком Daisy Bell (Bicycle Built for Two).

Среднее по продолжительности треков для всех четырех исполнителей находится на отметке около трех минут. Приблизительный результат равен 3 минутам 6 секундам (186 сек).
"""
)

recommendations = st.markdown(""" ## Обсуждение: 
**Что мы хотели сделать в рамках нашего исследования и что сделать удалось**

Изначально нашим планом было проанализировать лишь три исполнителя, однако в процессе мы решили добавить четвертого (Луи Армстронга) для более широкой выборки. Это также позволило нам компенсировать тот факт, что у Нэта "Кинга" Коула лишь шестнадцать песен вместо пятидесяти, как у всех остальных. Можно считать, что самую основную часть работы (выяснение продолжительности песен, анализ наиболее часто встречаемых слов) мы выполнили на "отлично".
 
**Что не удалось сделать и почему**

Одной из главных визуализаций данных, которую мы планировали вставить, изначально был анализ наиболее значимых для этих музыкантов лет через подсчет песен по датам их выпуска и создания на этой основе графика. Проблема возникла с музыкальной базой данных(discogs) и её api - из 166 треков 96 оказалось без дат. Следовательно, анализ данных получился бы по меньшей мере практически полностью недостоверным. В один момент мы также рассматривали идею убрать дубликаты песен из подборки, однако в конечном счете решили, что это не имеет смысла относительно того, что именно мы анализируем. 

**Как наше исследование можно было бы улучшить**

Определенно - решить возникшие у нас проблемы. Избавиться от дубликатов песен, вероятно, пофиксить базовые ошибки, по типу пропусков значений лет и неверной продолжительности некоторой песни.

Возможно, расширить выборку ещё на несколько знаменитых джазовых исполнителей: возможно, Пегги Ли, Бинга Кросби, Джона Колтрэйна, Билли Холидея, Сэмми Дэвиса. Если бы мы расширили выборку, из нишевого проекта это стало бы более значимой работой. Кроме того, вместо 50 наиболее знаменитых песен каждого музыканта мы могли взять всю их дискографию. Однако в таком случае также пришлось бы чистить подборку от возможных дубликатов некоторых песен, вроде Blue Moon. Из более экспериментальных идей - попробовать пошарить по американским сайтам в поисках данных о продажах копий джазовых альбомов Фрэнка Синатры, как одного из самых известных исполнителей джазовых песен (даже если и не джазмена в классическом понимании термина) и сопоставить с продажами рок-н-ролльных альбомов и синглов Элвиса Пресли, как самого известного исполнителя в жанре рок-н-ролла, дабы отследить момент, где джаз уступил рок-н-роллу в популярности среди простых обывателей.

**Fun Fact:**
В нашем готовом датасете (пусть и сделанном на основе скрипта) песня "Blue Moon" встречается два раза. Изначально не написанная ни Синатрой, ни Дином Мартином, она была создана в тридцатых и исполнялась огромным количеством певцов и групп в самые разные времена. Её исполнял даже Элвис Пресли в самой начале своей карьеры, причем его звучание песни сильно отличается не только от более торжественных версий, но и от его более поздних работ.

**Кому наше исследование может быть полезно (или что можно сделать дополнительно, чтобы оно было полезным)**

Если провести изменения, которые мы описали в прошлом блоке по поводу улучшения нашего проекта, чисто теоретически, оно бы могло использоваться в полноценной научной работе по поводу джаза. Провести подобное с рок-н-роллом в тех же годах, а также с ещё парой доминирующих жанров, вроде диско и более классического рока/рэпа, и подобную таблицу можно было бы использовать в научной работе по поводу различных музыкальных эпох в США, и как одни жанры выходили из моды и заменялись другими с развитием культуры. В зависимости от типа исследования также может иметь смысл удаление дубликатов Blue Moon и Let it Snow.

В общем и целом, это исследование так и останется весьма специфичным и нишевым исследованием, однако базовая логика может быть улучшена и адаптирована и для более серьезных работ.
"""
)
