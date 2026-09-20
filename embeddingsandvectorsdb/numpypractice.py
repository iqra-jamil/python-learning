from dotenv import load_dotenv
import numpy as np
import os
load_dotenv()
from openai import OpenAI


client=OpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key=os.getenv("GEMINI_API_KEY")
)
def embedding_create(vector_txt):
 response=client.embeddings.create(
    model="gemini-embedding-2",
    input=vector_txt
 )
 return response.data[0].embedding
def find_cosine(vec_a,vec_b):
     return np.dot(vec_a,vec_b)/(np.linalg.norm(vec_a)*np.linalg.norm(vec_b))

vec_1=embedding_create("my name is iqra")
vec_2=embedding_create("i am an IT grad")
vec_3=embedding_create("i did graduation from virtual uni")
print("similarity 1",find_cosine(vec_1,vec_2))
print("similarity 2",find_cosine(vec_2,vec_3))
print("similarity 3",find_cosine(vec_1,vec_3))