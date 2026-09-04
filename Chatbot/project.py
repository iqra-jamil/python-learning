from openai import OpenAI
import streamlit as st
import openai
from dotenv import load_dotenv
import os

load_dotenv()
# side_title=''

client=OpenAI(
    api_key=os.getenv('GROQ_API_KEY'),
    base_url="https://api.groq.com/openai/v1"
)


if "messages_list" not in st.session_state:
    st.session_state.messages_list=[
      {"role":"system","content":"you are a helpful AI assistant"}
    ]
if "all_chats" not in st.session_state:
     st.session_state.all_chats=[]
st.title("Iqra Ai")
user_prompt=st.chat_input("Ask anything")
# try Except
try:
 if user_prompt:
   st.session_state.messages_list.append({"role":"user","content":user_prompt})
   if(len(st.session_state.messages_list)==2):
     st.session_state.all_chats.append(st.session_state.messages_list)

   response=client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=st.session_state.messages_list
   )

   model_response=response.choices[0].message.content
   st.session_state.messages_list.append({"role":"assistant","content":model_response})


except openai.BadRequestError as e:
  print(f"BadRequestError  : {e}")
except openai.APIConnectionError as e:
  print(f"APIConnectionErrorr  : {e}")

# Side bar
with st.sidebar:
   st.header("LLM Chatbot")
   st.write("You AI Assistant")
   if st.button("New Chat",icon="💬" ,width="stretch" ):
      
        st.session_state.messages_list=[
             {"role":"system","content":"you are a helpful AI assistant"}
           ]
      
   if st.button("clear conversation",icon="🗑️" ,width="stretch" ):
       st.session_state.messages_list=[
            {"role":"system","content":"you are a helpful AI assistant"}
          ]
   assitant_modes={
       "General Assistant": "you are a helpful, friendly assistant.",
           "Coding Assistant": "you are an expert programming assistant.",
           "Study Tutor": "you are a patient and clear tutor.",
           "Creative Writer": "you are a creative writing expert.",
   }

   selected_mode=st.selectbox("Choose The Assistant Mode",assitant_modes.keys())
   if st.button("Apply mode",width="stretch"):
        st.session_state.messages_list=[
            {"role":"system","content":assitant_modes[selected_mode]}
        ]

# chat histry
   st.write("Recents")
   for index,chat in enumerate(st.session_state.all_chats):
     chat_index=index
     for c in chat:
       
       if c["role"]=='user':
        splited_txt=side_title=c['content'].split()
        joined_txt=' '.join(splited_txt[:3])
        if st.button(joined_txt+"....",width="stretch"):
            selected_chat=st.session_state.messages_list=st.session_state.all_chats[index]
        break
# rendring chat on UI
for msg_list in  st.session_state.messages_list:
      if msg_list["role"]!="system":
       with st.chat_message(msg_list["role"]) :
           st.markdown(msg_list["content"])

 