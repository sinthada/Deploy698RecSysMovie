

import streamlit as st
import pickle
from surprise import SVD


# Streamlit app title
st.title("Movie Recommendation System")

# Load data from the pickle file
with open('66130701708_recommendation_movie_svd.pkl', 'rb') as file:
    svd_model, movie_ratings, movies = pickle.load(file)

# Display loaded data
st.write("Loaded data successfully!")

# Example: Show first few entries of movies
st.subheader("Movies Data Sample")
st.write(movies.head())

# Add further functionality for recommendations if needed
# For example: select a movie and get recommendations
st.subheader("Get Movie Recommendations")
selected_movie = st.selectbox("Select a movie:", movies['title'].values)

# Logic to get recommendations (you would need to write your recommendation logic)
if st.button("Recommend"):
    # Placeholder logic: replace with actual recommendation based on SVD model
    st.write(f"Recommendations for '{selected_movie}' will be shown here.")


