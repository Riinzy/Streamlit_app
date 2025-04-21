import streamlit as st

st.title("My First App")

name = st.text_input ("WHat's your name")
if name:
  st.write(f"Hello, {name}!")
