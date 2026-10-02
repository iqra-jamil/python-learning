import streamlit as st
import chromadb 
from langchain_core.chat_history import InMemoryChatMessageHistory
from dotenv import load_dotenv
from functions import load_and_chunks
from functions import extract_my_txt
from functions import embed_and_store
from functions import retrieval_func
from functions import ask_llm
from functions import render_chat
import uuid
import os
load_dotenv()
st.title("Chat with pdf")
# Normal variables
extracted_data=[]
user_query=""
d_embed=[]
q_embed=[]


if "collection_name_id" not in st.session_state:
   st.session_state["collection_name_id"]=str(uuid.uuid4())

@st.cache_resource
def get_client():
   client = chromadb.CloudClient(
  api_key=os.getenv('CHROMA_API_KEY'),
  tenant=os.getenv('CHROMA_TENANT'),
  database=os.getenv('CHROMA_DATABASE')
)
   return client
client=get_client()
collection=client.get_or_create_collection(name=st.session_state["collection_name_id"])


# State variables
if "chat_started" not in st.session_state:
    st.session_state.chat_started = False
if "msg_history" not in st.session_state:
   st.session_state["msg_history"]=InMemoryChatMessageHistory()
if 'processes_file'  not in st.session_state:
    st.session_state['processes_file']=None
if 'retrived_data' not in st.session_state:
   st.session_state['retrived_data']=[]
if 'my_pagelabels' not in st.session_state:
   st.session_state['my_pagelabels']=[]
if 'Retrieved_Chunks' not in st.session_state:
   st.session_state['Retrieved_Chunks']=''
# Sidebar
with st.sidebar:
  uploaded_file=st.file_uploader("Uplaod Your File",type="pdf")
  if uploaded_file:
    st.write("Source : ",uploaded_file.name)
user_query=st.chat_input("Ask something....")


#Load the document and extract data 
if uploaded_file:
  if st.session_state['processes_file'] != uploaded_file.name:
    st.session_state["msg_history"].clear() 
    client.delete_collection(name=st.session_state["collection_name_id"])
    collection=client.get_or_create_collection(name=st.session_state["collection_name_id"])
    #function calls
    get_my_chunks=load_and_chunks(uploaded_file.getvalue())
    my_metadata,extracted_txt,my_unique_ids=extract_my_txt(get_my_chunks)
    chk_embedding=embed_and_store(collection,my_metadata,extracted_txt,my_unique_ids)
    if chk_embedding:
     st.session_state['processes_file'] = uploaded_file.name
    else : #embedding failed
       st.stop()
# handling user's query   
if user_query:
          st.session_state.chat_started = True
          if not uploaded_file:
              st.warning("Upload a PDF first")
              st.stop()
          query_result=retrieval_func(collection,user_query)
          if not query_result:
             st.stop()
          st.session_state['Retrieved_Chunks'] = ''
          st.session_state['my_pagelabels'] = []

          for doc in query_result["documents"][0]:
            st.session_state['Retrieved_Chunks']+=doc + "\n\n"
       
          for metadata in query_result["metadatas"][0]:
              st.session_state['my_pagelabels'].append(metadata["page_label"])
          with st.sidebar:
             with st.expander(label="Retrieved Context"):
              st.write("Page numbers : ",",".join(st.session_state['my_pagelabels']))
              with st.expander(label="Retrieved Chunks"):
               st.write('Retrieved Txt',st.session_state['Retrieved_Chunks'])

          ask_llm(query_result["documents"][0],user_query)
#rendring chat
if not st.session_state.chat_started:
   st.write("How Can I Help You Today?")
render_chat()
