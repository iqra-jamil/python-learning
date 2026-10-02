from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_groq import ChatGroq
from langchain.messages import HumanMessage,SystemMessage,AIMessage
import tempfile
import uuid
import streamlit as st

#Functions
#load and extract txt from documnt
def load_and_chunks(file_byte):
      with tempfile.NamedTemporaryFile(delete=False,suffix='.pdf') as temp_file:
        temp_file.write(file_byte)
        file_path=temp_file.name
      loader=PyPDFLoader(file_path)
      extracted_data=loader.load()
       # Chunks of data
      txt_splitter=RecursiveCharacterTextSplitter(
             chunk_size=10000,
             chunk_overlap=100
      )
      my_chunks=txt_splitter.split_documents(extracted_data)
      return my_chunks
#get txt ,metadata,id from the chunks
def extract_my_txt(my_chunks):
    my_metadata=[]
    extracted_txt=[]
    my_unique_ids=[]
    for chunk in my_chunks:
      my_metadata.append(chunk.metadata)
      extracted_txt.append(chunk.page_content)
      each_id=uuid.uuid4()
      my_unique_ids.append(str(each_id))
    return my_metadata,extracted_txt,my_unique_ids
#Calling embeding model to convert document's txt into vectors
def embed_and_store(my_collection,metadat_a,da_ta, id_s,):
   try:
    document_embeddings=GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2-preview",
    task_type="RETRIEVAL_DOCUMENT"
    )

#embed_document get list not txt
    d_embed=document_embeddings.embed_documents(da_ta)
    if d_embed:
         my_collection.add(
        ids=id_s,
        documents=da_ta,
        metadatas=metadat_a,
        embeddings=d_embed
   )

    st.session_state['retrived_data']=my_collection.get(include=["embeddings","documents","metadatas"])
    return True
   except Exception as e:
      st.error(e)
      return False
def  retrieval_func(my_collection,query):
 try:
    query_embedding=GoogleGenerativeAIEmbeddings(
     model="gemini-embedding-2-preview",
     task_type="RETRIEVAL_QUERY"
    )
    q_embed=query_embedding.embed_query(query)
    query_res=my_collection.query(query_embeddings=q_embed,
                               n_results=4,
                                include=['metadatas','documents','embeddings'])
    return query_res
 except Exception as e:
    st.error(e)
    return False

# sending user's query and retrived chunks to an LLM for response
def ask_llm(query_res,user_query):
 try:
    model=ChatGroq(
      model="openai/gpt-oss-20b",
       temperature=1.0,
      max_tokens=None
    )
    system_msg=SystemMessage(content=f"You are a helpful AI assistant. Answer the user's query based only on the provided information: {query_res}. If the requested information is not available, respond with 'Information not provided.' Do not provide any information beyond the provided context.")
    #msg history
    st.session_state["msg_history"].add_message(
       HumanMessage(content=user_query)
    )
    response=model.invoke([system_msg]+st.session_state["msg_history"].messages)
    st.session_state["msg_history"].add_message(response)
 except Exception as e:
    st.error(e)
#rendring chat
def render_chat():
 for msg in st.session_state["msg_history"].messages:
       if isinstance(msg,HumanMessage):
          with st.chat_message("user"):
             st.write(msg.content)
       elif isinstance(msg,AIMessage):
          with st.chat_message("assistant"):
             st.write(msg.content)