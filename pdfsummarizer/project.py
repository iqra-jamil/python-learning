import streamlit as st
import pdfplumber as pb
from openai import OpenAI
from dotenv import load_dotenv
import time 
import os
import openai
load_dotenv()
extracted_txt=''
final_summary=''
joined_txt=''
uploaded_file=st.file_uploader("Upload PDF File",type="pdf")
client=OpenAI(
    api_key=os.getenv('GROQ_API_KEY'),
    base_url='https://api.groq.com/openai/v1' )
try:
 if uploaded_file is not None:
    st.write("The file name is",uploaded_file.name)
    with pb.open(uploaded_file) as pdf:
        page_numbers=pdf.pages
        for page in page_numbers:
           
               extracted_txt+=page.extract_text()
            # handling large document
        start=0
        while start<len(extracted_txt.split()):
                 end=start+1000
                 splitted_txt=extracted_txt.split()[start:end]
                 start=end
                 joined_txt=" ".join(splitted_txt)

                
                 response=client.chat.completions.create(
                        model="openai/gpt-oss-20b",
                        messages=[
                        {'role':'system','content':'Summarize this text only, do not ask for follow up questions.'},
                        {'role' : 'user','content':joined_txt}
                        ]
                    )
                 # to reset groq limit wait for 15 secnd before the nxt request
                 #time.sleep(100)
                 final_summary+=response.choices[0].message.content
except openai.RateLimitError as e:
     st.error(e)
st.write(final_summary)


 