import streamlit as st
import openai

 

# Title
st.title("🎬 Movie Rating Predictor")
st.write("Enter a movie summary and get a predicted IMDb rating.")

# Text input from user
movie_summary = st.text_area("Movie Summary", height=200)

if movie_summary:
    response = openai.chat.completions.create(
        model="gpt-4o-mini", 
        messages=[
            {"role": "system", "content": "Predict the IMDb ratings based on plot synopsis of a movie. The rating is from 1 to 10."},
            {"role": "user", "content": f"Here is the plot synopsis: {movie_summary}\nRating:"}
        ],
        temperature=0.5,
        max_tokens=100
    )
    predicted_rating = response.choices[0].message.content
    st.success(f"Predicted IMDb Rating: ⭐ {predicted_rating}")
