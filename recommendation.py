import pickle

import numpy as np

model = pickle.load(open('artifacts/model.pkl', 'rb'))
movie_names = pickle.load(open('artifacts/movie_name.pkl', 'rb'))
final_data = pickle.load(open('artifacts/Final_Data.pkl', 'rb'))
data_pivot = pickle.load(open('artifacts/data_pivot.pkl', 'rb'))


def fetch_poster(suggestion):
    movie_name = []
    ids_index = []
    poster_url = []

    for movie_id in suggestion:
        movie_name.append(data_pivot.index[movie_id])

    for name in movie_name[0]:
        ids = np.where(final_data['Movie_name'] == name)[0][0]
        ids_index.append(ids)

    for idx in ids_index:
        url = final_data.iloc[idx]['Image_ID']
        poster_url.append(url)

    return poster_url


def recommend_movie(movie_name):
    error = ''
    movie_list = []
    filters = np.where(data_pivot.index == movie_name)[0]
    if len(filters) == 0:
        error = 'No movie found for recommendation'
        return [], [], error
    movie_id = filters[0]
    distance, suggestion = model.kneighbors(
        data_pivot.iloc[movie_id, :].values.reshape(1, -1), n_neighbors=6)

    poster_url = fetch_poster(suggestion)

    for i in range(len(suggestion)):
        books = data_pivot.index[suggestion[i]]
        for j in books:
            movie_list.append(j)
    return movie_list[1:], poster_url[1:], error
