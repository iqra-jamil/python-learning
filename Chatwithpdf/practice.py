# # import uuid


# # my_uniqueid=uuid.uuid4()

# # print(my_uniqueid)

# # my_uniqueid=uuid.uuid6()
# # print(my_uniqueid)


# from langchain_groq import ChatGroq
# from langchain.messages import SystemMessage,HumanMessage
# model=ChatGroq(
#     model="",
#     temperature="",
#     max_tokens="",
#     #other parametrs
# )

# messages=[
#     SystemMessage(content="you are not a helpful assitant"),
#     HumanMessage(content="what is python")
# ]


# resposne=model.invoke(messages)
# messages=[
#         HumanMessage(content=user_query),
#         SystemMessage(content=f"you are a helpful ai assistant reply based on{query_res['documents'][0]}"),
#      ]

# if messages[SystemMessage] na hn :
#    with st.chat_message(HumanMessage,AImessage):
#       st.markdown(messages.content)
my_list=["3", "4", "12", "12"]  
print(my_list)
joined_list="".join(my_list)
print(joined_list)


