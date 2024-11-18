
import streamlit as st
import pickle
from surprise import SVD

# Load the data and the SVD model
with open('66130701708_recommendation_movie_svd.pkl', 'rb') as file:
    svd_model, movie_ratings, movies = pickle.load(file)

# Streamlit UI
st.title("Movie Recommendation System")

# Ask for user input
user_id = st.number_input("Enter User ID", min_value=1, value=6, step=1)

# Get rated movies for the selected user
rated_user_movies = movie_ratings[movie_ratings['userId'] == user_id]['movieId'].values

# Get unrated movies
unrated_movies = movies[~movies['movieId'].isin(rated_user_movies)]['movieId']

# Predict ratings for unrated movies
pred_rating = [svd_model.predict(user_id, movie_id) for movie_id in unrated_movies]

# Sort predictions by estimated rating in descending order
sorted_predictions = sorted(pred_rating, key=lambda x: x.est, reverse=True)

# Get top 5 movie recommendations
top_recommendations = sorted_predictions[:5]

# Display top recommendations
st.subheader(f"Top 5 movie recommendations for User {user_id}:")

for recommendation in top_recommendations:
    movie_title = movies[movies['movieId'] == recommendation.iid]['title'].values[0]
    st.write(f"{movie_title} (Estimated Rating: {recommendation.est:.2f})")

