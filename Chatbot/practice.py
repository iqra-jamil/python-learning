import streamlit as st
from openai import OpenAI
import openai
import time
from dotenv import load_dotenv
import os
load_dotenv()
# Css needed to adjust buttons we have in side bar
st.markdown("""
    <style>
    div[data-testid="stSidebarContent"] .stButton > button {
        display: flex;
        justify-content: flex-start !important;
        align-items: center;
        gap: 10px;
        padding-left: 15px;
    }
    div[data-testid="stSidebarContent"] .stButton > button > div {
        display: flex;
        justify-content: flex-start !important;
        align-items: center;
        gap: 10px;
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)


st.title("ThinkBot")
# initializing state variable to store roles
if "user_messages" not in st.session_state:
    st.session_state.user_messages=[
        {'role' : 'system','content':'you are helpful assitant'}
    ]


# getting user prompt
user_prompt=st.chat_input("Ask something...")

try:
 if user_prompt:
   st.session_state.user_messages.append({'role' : 'user','content':user_prompt})
   
    # API CALL configration    
   client=OpenAI(
    base_url='https://api.groq.com/openai/v1',
    api_key=os.getenv('GROQ_API_KEY')
   )
   # API CALL with messages and model
   respose=client.chat.completions.create(
      model='openai/gpt-oss-20b',
      messages=st.session_state.user_messages,
     
    )
  
   assistant_resposne=respose.choices[0].message.content
   st.session_state.user_messages.append({'role' : 'assistant','content':assistant_resposne})
   
 # rendring chat on every rerurn
 for user_msg in st.session_state.user_messages:
       if user_msg["role"]!="system":
        with st.chat_message(user_msg["role"]):
           st.markdown(user_msg["content"])

# exception handling
except openai.APIError as e :
    print(f"An unexpected OpenAI library error occurred:{e}")
except openai.APITimeoutError:
    time.sleep(60) #wait and retry
# Sidebar
with st.sidebar:
  st.title("LLM Chatbot")
  st.write("Your AI Assistant")

# buttons and assitant's mode dropdowns

  if st.button("New Chat",icon="💬" ,width="stretch" ) :
    #    st.session_state.messages_list.append(st.session_state.user_messages)
       st.session_state.user_messages = [
        {'role': 'system', 'content': 'you are a helpful assistant'}
    ]

      
      
    
  if st.button("Clear conversation",icon="🗑️" ,width="stretch" ) :
     st.session_state.user_messages=[
         {'role' : 'system','content':'you are helpful assitant'}
     ]
 
system_options = {
    "General Assistant": "you are a helpful, friendly assistant.",
    "Coding Assistant": "you are an expert programming assistant.",
    "Study Tutor": "you are a patient and clear tutor.",
    "Creative Writer": "you are a creative writing expert.",
}

with st.sidebar:

           selected_role=st.selectbox("Choose Assistant Mode",list(system_options.keys()))

with st.sidebar:
   if st.button("Apply Mode"):
      st.session_state.user_messages=[
                 {'role' : 'system','content':system_options[selected_role]}
        ]



# chat interface bnaia tha  chat _input sy
# api call ke thi 
#chat completion  api call krty hoy hum user prompt backend sy set krhy thy actual m humy wo chatbox main lana tha
# user prompt jo chat box main enter krha tha us ko variable main store krwa k user role ko as content wo variable dy dia 
# response hum extract kr chuky thy after calling api 
#  us response ko b stor kia in a varible or us variable ko assistant role k content main dy dia  
# bcz ab na to user prompt aik ho ga na to resposne aik ho ga so we will ahve to use those varaibles 
# ab jesy he prompt jata h api call hoti h resposne b aarha h 
# but na to user ka prompt persist horha h na to model ka resposne
# so for that we will create a sesseion state varaible than append each respone and user promt into that variable
# ab wo yaad to krha h but jesy promt k bad response phir prompt phir response show hoty hain wo nai horhy so that is why we use chat_message

# ab q k role and content us state variable main appned ho chuky hain so we will loop on that state variable to extract role and content from that to show role and content on UI using chat_message

# we had three roles system,user and assitant - we initilize state variable with system role 
# Because the system role sets the AI's behavior/personality from the start, and it must be included in every API call as part of the conversation history.
# as user write prompt and press enter the user's prompt will be appeded in to state variable
# as the response will be come from a model it will be appended into statevariable exct after response will come 
# then as we had a list of msgs with roles and content we will just assign that state variable in wihc we appended all the three roles to that messages varible instead of having  alist now 
# we had to move roles at the moment exactly when they become available
# then we will go on side bar 


# ..............................
 #  for chat in st.session_state.all_chats:
  #    for c in chat:
  #      if c["role"]=='user':
  #       splited_txt=side_title=c['content'].split()
  #       joined_txt=' '.join(splited_txt[:5])
  #       st.button(joined_txt,width="stretch")
  #       break
# st.write(st.session_state.all_chats)
    #  for index in range(len(st.session_state.all_chats)):
    #    chat_index=index
    #    selected_chat=st.session_state.messages_list=st.session_state.all_chats[index]
    #    st.write(selected_chat)

