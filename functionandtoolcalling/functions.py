from langchain_groq import ChatGroq
from datetime import datetime
import requests
import json
def read_json_file():
    with open(r"C:\Users\decent\OneDrive\Desktop\python-learning\functionandtoolcalling\tools.json",'r') as file:
        tools=json.load(file)
        return tools["tools_list"]

    
def call_llm(conversattion_list):
  llm_model=ChatGroq(
    model="openai/gpt-oss-20b"
  )
  binding_tools=llm_model.bind_tools(read_json_file())
  model_response= binding_tools.invoke(conversattion_list)
  conversattion_list.append(model_response)
  return model_response

#tools
def get_weather(api_key,city_name):
    API_URL=f"https://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city_name}&units=metric"
    data=requests.get(API_URL)
    api_data=data.json()
    return api_data

def get_date_time():
    current_date_time=datetime.now()
    time=current_date_time.time()
    date=current_date_time.date()
    return time,date
    
    
