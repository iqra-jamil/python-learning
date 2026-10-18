from dotenv import load_dotenv
from langchain_core.messages import AIMessage,HumanMessage,SystemMessage,ToolMessage
from functions import call_llm
from functions import get_weather
from functions import read_json_file
from functions import get_date_time
import os
load_dotenv()

api_key=os.getenv('API_KEY')
conversattion_list=[
    SystemMessage(content="You are a helpful assitant answer always in details"),
     HumanMessage(content="What’s the date and time right now")
]


response=call_llm(conversattion_list)
# print(response.tool_calls)
conversattion_list.append(response)
if response.tool_calls:
  for tool_call in response.tool_calls:
     if tool_call["name"]=='get_date_time':
        tool_call_id=tool_call["id"]
        datetime_result=get_date_time()
        str_datetime_res=str(datetime_result)
        datetime_tool_result=ToolMessage(
               content=str_datetime_res,
               tool_call_id=tool_call_id
        )
        conversattion_list.append(datetime_tool_result)
     elif tool_call["name"]=='get_weather':
        cityname_arg=tool_call["args"]["city_name"]
        tool_call_id=tool_call["id"]
        execution_res=get_weather(api_key,cityname_arg)
        tool_result=ToolMessage(
                content=execution_res,
                tool_call_id=tool_call_id
            )
        conversattion_list.append(tool_result)
     final_response=call_llm(conversattion_list)
     print(final_response.content)
else:
    print(response.content)
