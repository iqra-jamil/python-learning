
import streamlit as st
import pandas as pd
df={"First column" :[1,2,4],
    "second column" :[8,7,0]}
st.title("Favorite Programming Language Selector")
st.header("Favorite Programming Language ❤️")
st.text("Choose your favorite programming language:")
st.write("“Select one language from the options below.”")
lang=st.selectbox("Your fav lang",["python","javascript","C++","C","PHP"])
st.success(f"your favourite language is {lang}")
st.badge("Selected")
st.dataframe(pd.DataFrame(df))