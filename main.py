import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Marian Dobrea")
    content = """
      Hello, I am Marian !
      Being an Experienced Quality Assurance Engineer and Python Developer with a proven track record of delivering exceptional results through both freelance projects with high-profile companies and an extensive internship at GOIT Romania 
      I am an adept of designing, executing and writing comprehensive code, test plans, identifying critical issues, and collaborating effectively with development teams. 
      Leveraging diverse experiences to drive product excellence and user satisfaction through meticulous and innovative testing strategies and coding.
      Looking for my next challenge and opportunity in the Development World ! 
      """
    st.info(content)

content2 = """Below you can find some of the apps I have built in Python. 
Feel free to contact me!"""
st.write(content2)

col3,emptycol, col4 = st.columns([1.5, 0.5, 1.5])


df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")