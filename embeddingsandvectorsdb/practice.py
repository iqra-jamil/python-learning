# embeddings
# embedding=[0.2, -0.5, 0.8, 0.1, 0.3]
# Convert txt into numbers call Embedding APi

#from google import genai
from dotenv import load_dotenv
#import numpy as np
import os
load_dotenv()
from openai import OpenAI
from sklearn.metrics.pairwise import cosine_similarity

client=OpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key=os.getenv("GEMINI_API_KEY")
)

def find_cosine(vector):
 response=client.embeddings.create(
    model="gemini-embedding-2",
    input=vector
)

 print(response.data[0].embedding)
 return response.data[0].embedding

vec1 =find_cosine("I love dogs")
vec2 = find_cosine("Puppies are great")
vec3 = find_cosine("Stock market crashed")
print("similarity",cosine_similarity([vec1],[vec2]))
print("similarity",cosine_similarity([vec3],[vec1]))

# client=genai.Client()
# response=client.models.embed_content(
#     model="gemini-embedding-2",
#     contents="dog is an animal"
# )
# print(response)

