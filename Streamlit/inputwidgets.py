import streamlit as st
import datetime
click_button=st.button("Click me")
if click_button:
    st.success("Clicked")
menu=st.menu_button("Export",options=["CSV","JSON","PDF"])
if menu=="CSV":
    st.write(f" Exporting as {menu}...")
if menu=="JSON":
    st.write(f"Exporting as {menu}...")
if menu=="PDF":
     st.write(f"Exporting as {menu}...")

st.checkbox("I agree")
# st.feedback("stars")
# st.feedback("faces")


sentiment_list=["one", "two", "three", "four", "five"]
print(sentiment_list[2])
selected=st.feedback("stars") # will return index of the star 
if selected is not None:
   st.write(f"you selcetd {sentiment_list[selected]} star(s)")
sentiment_mapping = [":material/thumb_down:", ":material/thumb_up:"]
selected=st.feedback("thumbs") # will return index 
if selected is not None:
    st.write(f" You selcted {sentiment_mapping[selected]}")


color=st.color_picker("Pick A Color")
if color:
 st.write(f"you selected : {color}")

#st.multiselect("text",[arry of options],[array of default])

st.multiselect("What are your favorite colors?",["Green", "Yellow", "Red", "Blue"],default=["Yellow", "Red"])
on=st.toggle("Activate feature")
if on:
    st.write("feature activated")
else:
    st.write("Activate feature")

st.camera_input("Take a picture")

email= st.text_input("enter email",type="email")
if email:
 st.write(f"we will contact on {email}")

dob=st.date_input("Select you DOB")
st.write("You selected",dob)
selected_year=dob.year
st.write(f"Your age is : {2026-selected_year}" )