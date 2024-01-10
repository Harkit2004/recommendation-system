import pandas as pd
import streamlit as st
import pickle 

def recommend(title):
    index = games[games['Title'] == title].index[0]
    print(index)
    distance = similarity[index]
    print(distance)
    movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x:x[1])[1:6]
    print(movies_list)
    for i in movies_list:
        st.write(games.iloc[i[0]].Title)

game_dict = pickle.load(open('games.pkl', 'rb'))
games = pd.DataFrame(game_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Video Game Recommender')

selected_game = st.selectbox('Hi', games['Title'].values)

if st.button('Recommend'):
    recommend(selected_game)