import streamlit as st
st.set_page_config(layout="wide")
col1,col2=st.columns(2)
with col1:
    st.image("images/photo.png")
with col2:
    st.title("Rajasree Gorrepati")
    content="""Hi,I'm Rajasree Gorrepati.Iam a python programmer.I graduated in 2023 from R.V.R & J.C College of Engineering in the stream of computer science."""
    st.info(content)
st.write("Below you can find some of the apps I have built in Python.Feel free to contact me!")