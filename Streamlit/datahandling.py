import streamlit as st
import pandas as pd


# uploader to upload csv file
# load that
# convert that in to df
# show statistical summary

file = st.file_uploader("Upload your file",type="csv")
if file:
    df=pd.read_csv(file)
    st.subheader("Data frame")
    st.dataframe(pd.DataFrame(df))
if file:
    st.subheader("Summary Stats")
    sta_sumary=st.dataframe(df.describe())
    # st.json(sta_sumary)

if file:
    uniquvalues=df["Pulse"].unique()
    selected_value=st.selectbox("filter by values",uniquvalues)
    filterred_values= df[df["Pulse"]==selected_value] #df[condition] = filter the rows using that condition
    st.dataframe(filterred_values)
