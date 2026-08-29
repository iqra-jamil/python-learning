import streamlit as st
import time
print("LAYOUTS  & CONTAINERS")
col1,col2,col3=st.columns(3,border=True)
with col1:
    st.header("Students names")
    st.image("https://images.unsplash.com/photo-1787140031683-70098c9f3f97?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxmZWF0dXJlZC1waG90b3MtZmVlZHw3fHx8ZW58MHx8fHx8",width=200)
with col2:
     st.header("Students id")
     st.image("https://images.unsplash.com/photo-1773332585815-f106a5d6ed6c?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDF8MHxmZWF0dXJlZC1waG90b3MtZmVlZHw4fHx8ZW58MHx8fHx8",width=200)
with col3:
     st.header("Students samester")
     st.image("https://images.unsplash.com/photo-1773332585771-5c9c5fa642d1?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDF8MHxmZWF0dXJlZC1waG90b3MtZmVlZHwyMnx8fGVufDB8fHx8fA%3D%3D",width=200)



c= st.container(border=True)
with c:
  st.write("inside container")
  st.write("inside container")
  st.write("inside container")

st.write("outside")

# st.markdown("**This is bold**")

# st.write("**This is bold**")

# st.markdown("# heading 1")
# st.write("# heading 1")

# st.markdown('<p style="color: red;">This is red text</p>',unsafe_allow_html=True)
# st.write('<p style="color: red;">This is red text</p>',unsafe_allow_html=True)

@ st.dialog("Sign up")
def email_verf():
    name = st.text_input("enter your name")
    Email=st.text_input("Email",type="email")
    button= st.button("Sign up" ,use_container_width=True)

st.button("Click me",on_click=email_verf)

c=st.empty()

c.write("Loading data...")
time.sleep(2)
c.text("Done!")

c=st.expander("click to expend")

with c:
    st.write("I AM EXpender")
    st.write("I AM one")
    st.write("I AM two")


# s=st.sidebar("i am side bar")
# with s :
st.sidebar.text_input("name")
st.sidebar.write("i am side bar")


#### tabs
tab1,tab2=st.tabs(["Tab1","Tab2"]) #it dont use int like col 
with tab1:
    st.write("main h Tab1")
with tab2:
    st.write("main hn Tab2")



st.space(size="small")

st.write("ayyeudahu")