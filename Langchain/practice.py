print("Langchain")

from langchain_core.prompts import PromptTemplate
# from langchain_openai import ChatOpenAI 
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv
import os
load_dotenv()


template="tell me a {adjective} joke about {topic}"
promt_temp=PromptTemplate.from_template(template)
# final_res=promt_temp.format(adjective="dark",topic="programming")
# print(final_res)
parser= StrOutputParser()
model=ChatGroq(model="openai/gpt-oss-20b",api_key=os.getenv("GROQ_API_KEY"))
chain=promt_temp|model|parser
resposne=chain.invoke({"adjective":"dark","topic":"programming"})
print(resposne)

#chat history for chatbots
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain.messages import HumanMessage,AIMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
load_dotenv()

history=InMemoryChatMessageHistory()

history.add_message(HumanMessage(content="hy i am iqra"))

model=ChatGroq(model="openai/gpt-oss-20b",api_key=os.getenv("GROQ_API_KEY"))
response=model.invoke(history.messages)
history.add_message(AIMessage(content=response.content))
print(response.content)
history.add_message(HumanMessage(content="what is my name"))
response=model.invoke(history.messages)
history.add_message(AIMessage(content=response.content))
print(response.content)

# Document Loader

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
loader=PyPDFLoader("document.pdf")
doc=loader.load()
print(doc)

#splitter

spliter=RecursiveCharacterTextSplitter(size=500,chunk_overlap=50)
chunk=spliter.split_documents(doc)
print(chunk)


# Retriever
#will see them after embedding and vectors

