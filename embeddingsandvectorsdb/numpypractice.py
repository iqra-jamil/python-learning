from dotenv import load_dotenv
import numpy as np
import os
load_dotenv()
from openai import OpenAI
import chromadb 
#ids,metadat,orignal txt,vectors/embeddings

client=chromadb.Client()
collection=client.get_or_create_collection(name="My_collection")
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
def find_cosine(vec_a,vec_b):
     return np.dot(vec_a,vec_b)/(np.linalg.norm(vec_a)*np.linalg.norm(vec_b))
query_search=embedding_create("Where did I graduate?")
vec_1=embedding_create("my name is iqra")
vec_2=embedding_create("i am an IT grad")
vec_3=embedding_create("i did graduation from virtual uni")
# print("similarity 1",find_cosine(vec_1,vec_2))
# print("similarity 2",find_cosine(vec_2,vec_3))
# print("similarity 3",find_cosine(vec_1,vec_3))
print("similarity 1",find_cosine(vec_1,query_search))
print("similarity 2",find_cosine(vec_2,query_search))
print("similarity 3",find_cosine(vec_3,query_search))
collection.add(
   ids=["id1","id2","id3"],
   embeddings=[vec_1,vec_2,vec_3],
   documents = ["my name is iqra", "i am an IT grad", "i did graduation from virtual uni"],
   metadatas=[{"author_name":"iqra","chap":3},{"author_name":"me_iqra","chap":5},{"auth_name":"iqra_3","chap":9}],
  )

result=collection.get(include=["embeddings","metadatas","documents"])
#result=collection.get(ids=["id1"])
#print(result)

query_res=collection.query(query_embeddings=[query_search],
                           n_results=2,
                           where={"author_name":"me_iqra"})
print("query results :: ",query_res)
