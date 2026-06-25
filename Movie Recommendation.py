# data --> data preprocessing --> feature extraction --> user input --> Cosine Similarity --> list of movies


# importing dependencies

import numpy as np
import pandas as pd
import difflib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity



# loading the data from the csv file to pandas dataframe

movies_data = pd.read_csv(r'C:\Users\allen\OneDrive\Desktop\understanding\data\movies.csv')


pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)



# selecting the relevant features for recommendation

selected_features = [
    'genres',
    'keywords',
    'tagline',
    'cast',
    'director'
]



# replacing the null values with null string

for feature in selected_features:
    movies_data[feature] = movies_data[feature].fillna('')



# combining all the selected features

combined_features = (
    movies_data['genres'] + ' ' +
    movies_data['keywords'] + ' ' +
    movies_data['tagline'] + ' ' +
    movies_data['cast'] + ' ' +
    movies_data['director']
)



# converting text data into feature vectors

vectorizer = TfidfVectorizer()

feature_vectors = vectorizer.fit_transform(combined_features)



# getting similarity scores using cosine similarity

similarity = cosine_similarity(feature_vectors)



# getting movie name from user

movie_name = input('Enter your favourite movie name : ')



# creating list of all movie names

list_of_all_titles = movies_data['title'].tolist()



# finding close match for movie name

find_close_match = difflib.get_close_matches(
    movie_name,
    list_of_all_titles
)



if len(find_close_match) == 0:

    print("Movie not found")


else:

    close_match = find_close_match[0]



    # finding index of the movie

    index_of_the_movie = movies_data[
        movies_data.title == close_match
    ]['index'].values[0]



    # getting similarity score

    similarity_score = list(
        enumerate(similarity[index_of_the_movie])
    )



    # sorting movies based on similarity score

    sorted_similar_movies = sorted(
        similarity_score,
        key=lambda x:x[1],
        reverse=True
    )



    # printing recommended movies

    print("\nMovies suggested for you : \n")


    i = 1


    for movie in sorted_similar_movies:

        index = movie[0]


        title_from_index = movies_data[
            movies_data.index == index
        ]['title'].values[0]


        if i < 30:

            print(i, '.', title_from_index)

            i += 1