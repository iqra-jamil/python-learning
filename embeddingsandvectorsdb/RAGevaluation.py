from dotenv import load_dotenv
import numpy as np
import os
load_dotenv()
from openai import OpenAI
import chromadb 

# doc_1 = "Python is a high level programming language known for its simple and readable syntax. It is commonly used for web development, automation, data analysis, artificial intelligence, and machine learning. Python is popular because it is easy to learn and has a large ecosystem of libraries."

# doc_2 = "JavaScript is a programming language mainly used to make web pages interactive. It runs in web browsers and can also be used on servers with environments such as Node.js. It is widely used for frontend and backend web development."

# doc_3 = "React is a JavaScript library used to build user interfaces. It allows developers to create reusable components and update parts of a web page efficiently when application data changes. React is commonly used for single page applications."

# doc_4 = "A database is used to store and organize data so applications can access and manage it efficiently. Common database systems include MySQL, PostgreSQL, MongoDB, and SQLite. Databases help applications store user and business information securely."

# doc_5 = "Machine learning is a field of artificial intelligence where models learn patterns from data. These models can use learned patterns to make predictions or decisions on new data. It is used in recommendation systems, fraud detection, and image recognition."


doc_1="Python is a high level programming language known for its simple and readable syntax."

doc_2="Python is commonly used for web development, automation, data analysis, artificial intelligence, and machine learning."

doc_3="JavaScript is a programming language mainly used to make web pages interactive."

doc_4="It runs in web browsers and can also be used on servers with environments such as Node.js."

doc_5="React is a JavaScript library used to build user interfaces."

doc_6="It allows developers to create reusable components and update parts of a web page efficiently when application data changes."

doc_7="A database is used to store and organize data so applications can access and manage it efficiently."

doc_8="Common database systems include MySQL, PostgreSQL, MongoDB, and SQLite."

doc_9="Machine learning is a field of artificial intelligence where models learn patterns from data."

doc_10="These models can use learned patterns to make predictions or decisions on new data."


query_1="What is Python commonly used for?"
query_2="What is JavaScript mainly used for?"
query_3="What is React used to build?"
query_4="What is the purpose of a database?"
query_5="What is machine learning?"
unrelated_query1="What is the capital of France?"
unrelated_query2="Who invented the telephone?"
one_more_query= "What is Mongodb?"
client=chromadb.Client()
collection=client.get_or_create_collection(name="my_collection")

client=OpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key=os.getenv("GEMINI_API_KEY")
)

def embedding_create(vector_txt):
 response=client.embeddings.create(
    model="gemini-embedding-2",
    input=vector_txt
 )
 #print(response.data[0].embedding)
 return response.data[0].embedding
def search_cosine(veca,vecb):
 return np.dot(veca,vecb)/(np.linalg.norm(veca)*np.linalg.norm(vecb))
query_search1=embedding_create(query_1)
query_search2=embedding_create(query_2)
query_search3=embedding_create(query_3)
query_search4=embedding_create(query_4)
query_search5=embedding_create(query_5)
query_search6=embedding_create(unrelated_query1)
query_search7=embedding_create(unrelated_query2)
one_more_queryy=embedding_create(one_more_query)
txt_1=embedding_create(doc_1)
txt_2=embedding_create(doc_2)
txt_3=embedding_create(doc_3)
txt_4=embedding_create(doc_4)
txt_5=embedding_create(doc_5)
txt_6=embedding_create(doc_6)
txt_7=embedding_create(doc_7)
txt_8=embedding_create(doc_8)
txt_9=embedding_create(doc_9)
txt_10=embedding_create(doc_10)

print("similarity 1",search_cosine(query_search6,txt_1))
print("similarity 2",search_cosine(query_search6,txt_2))
print("similarity 3",search_cosine(query_search6,txt_3))
print("similarity 4",search_cosine(query_search6,txt_4))

collection.add(
ids=["id1","id2","id3","id4","id5","id6","id7","id8","id9","id10"],

documents=[doc_1,doc_2,doc_3,doc_4,doc_5,doc_6,doc_7,doc_8,doc_9,doc_10],

metadatas=[
    {"author_name":"iqra","words":93},
    {"author_name":"iqraj","words":103},
    {"author_name":"iqra3","words":109},
    {"author_name":"iqra4","words":106},
    {"author_name":"iqra5","words":99},
    {"author_name":"iqra6","words":95},
    {"author_name":"iqra7","words":101},
    {"author_name":"iqra8","words":97},
    {"author_name":"iqra9","words":104},
    {"author_name":"iqra10","words":100}
],

embeddings=[txt_1,txt_2,txt_3,txt_4,txt_5,txt_6,txt_7,txt_8,txt_9,txt_10]

)

result=collection.get()
# print(result)
# query_res=collection.query(query_embeddings=query_search3)

# query_res=collection.query(query_embeddings=query_search6)

query_res=collection.query(query_embeddings=[query_search7],
                           n_results=1)
print("top-k=1",query_res)
query_res=collection.query(query_embeddings=[query_search7],
                           n_results=3)
print("top-k=3",query_res)

query_res=collection.query(query_embeddings=[query_search7],
                           n_results=5)
print("top-k=5",query_res)


