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
#     other parametrs
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
# my_list=["3", "4", "12", "12"]  
# print(my_list)
# joined_list="".join(my_list)
# print(joined_list)



import sqlite3 as sq
if 'conv_id' not in st.session_state:
    st.session_state['conv_id']=None

connection=sq.connect('app.db')
cursor=connection.cursor()
# create conversation table 
cursor.execute('CREATE TABLE IF NOT EXISTS conversations (convo_title TEXT ,convo_id INTEGER PRIMARY KEY)')


convo_title=[uploaded_file.name]

cursor.execute('INSERT  INTO conversations UNIQUE (convo_title) VALUES (?)',convo_title)
st.session_state['conv_id']=cursor.lastrowid
connection.commit()
# create each msg table
cursor.execute('CREATE TABLE IF NOT EXISTS messages (each_msg TEXT ,role TEXT,msg_id INTEGER PRIMARY KEY ,convo_id INTEGER ,FOREIGN KEY (convo_id) references conversations(convo_id) )')


for msg in st.session_state["msg_history"].messages:
    if isinstance(msg,HumanMessage):
        role='user'
        msg=msg.content
    elif isinstance(msg,AIMessage):
        role='assistant'
        msg=msg.content
    role=role
    each_msg=msg
    convo_id=st.session_state['conv_id']
    convo_values_list=[each_msg,role,convo_id]
    cursor.execute('INSERT OR IGNORE INTO messages (each_msg,role,convo_id) VALUES(?,?,?)',convo_values_list)
    connection.commit()