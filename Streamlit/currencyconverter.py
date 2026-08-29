import streamlit as st
import requests
st.title("currency Converter")
amount=st.number_input("Enter amount to convert", min_value=1)

selected_cur=st.selectbox("Select country",["INR","USD","AZN","JPY"])

if st.button("Convert") :
  url="https://api.exchangerate-api.com/v4/latest/PKR"
  response=requests.get(url)
  st.write(response.status_code)
  if response.status_code == 200 :
     data = response.json()
     rate=data["rates"][selected_cur]
     st.write(rate)
     convert=amount*rate
     st.success(f"converted rate of {amount} PKR is : {round(convert)} {selected_cur}" )
  else:
     st.error("failed to fetch response")


