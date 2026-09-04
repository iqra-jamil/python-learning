import streamlit as st
x=0


# def counter():
#    global x
#    x=x+1
   
# st.button("Click me",on_click=counter)
# st.write(x)
# # counter()
# # print(x)
# # counter()
# # print(x)
# # counter()
# # print(x)


# if "x"  not in st.session_state :
#     st.session_state.x=0
    
# if st.button("click me") :
#     st.session_state.x +=1
# st.write(st.session_state.x)
# st.write(st.session_state["x"])

if "count" not in st.session_state:
    st.session_state["count"]=0
if st.button("Increment"):
    st.session_state["count"]+=1
if st.button("decrement"):
    st.session_state["count"]-=1
if st.button("Reset"):
    st.session_state["count"]=0
st.write(st.session_state["count"])

#frst initilize it and then update