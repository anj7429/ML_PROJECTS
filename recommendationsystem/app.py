import streamlit as st
import pickle
import pandas as pd

movies_dict=pickle.load(open('C:/Users/mk173/PycharmProjects/MLProjects/recommendationsystem/models/movies_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
similarity=pickle.load(open('C:/Users/mk173/PycharmProjects/MLProjects/recommendationsystem/models/similarity.pkl','rb'))

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movielist= sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies=[]
    for i in movielist:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

st.title("Movie Recommender System")
movie_option=st.selectbox(
    "Type or select a movie from the dropdown: ",
    movies['title'].values
)
if st.button('Recommend'):
    recommendations=recommend(movie_option)
    for i in recommendations:
        st.write(i)