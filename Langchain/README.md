# what is langchain
- Langchain is a framework that makes it easy for us to devlop LLMs (AI-powered apps.)
- when we delop our own chatbots we write alot of repetetive code liek for sending msgs ,geting response, and saving conversation history
- langchain gives us readymad building blocks to make it easy for us
- we were manulay building lists of dicts with role and content wvery time we were sending request to API (system prompt,,user prompt, assistant resposne) 
- langchain has prompt templates that handles this automatically 
- we just pass our variable (will see it in details later)
- LangChain lets our AI talk to the outside world our documents, our database, our tools instead of being stuck with only what it was trained on.

# why we should use it
- without langchain we will have to write code for evewrything
- we will have to write code for :
     - connecting services provider like Open AI ,claude,groq
     - to format user's prompt
     - to parse (converting raw response in to structured resposne) AI's response
     - to search through documnt
- with lanchain all of this is alredy builtin for us we just need to plug the pieces together

### Real example:
Say you want to build a chatbot that reads your PDF and answers questions from it. Without LangChain  weeks of work. With LangChain a few lines of code, because it already has tools for loading PDFs, searching them, and chatting with a model.


# what is RAG
- RAG-Retrieval Augmented Generation
- LLMs have knowledge about the data only till they were tarined they never know on what they were never trained on
- like if we ask quetion about a documnt RAG fetch that info from doc and send that infor along with our quetion to LLM for response
# how is langchain connected to RAG and
- RAG has multiple steps to do like 
- like loading a doc , fetching specific info from a doc, sending taht info to LLM ,
- langchain provide us ready made tools for all of these steps 
- RAG is just one technique to connect LLMs with outside data (specifically documents).
- LangChain is the toolkit that makes RAG and many other connections possible it's bigger than just RAG.
- RAG is specifically for dicumnts

# what problems Langchain solve??
## Problem 1 — Switching AI providers is painful
- as i developed a chatbot using openAI library ,and calls groq's API but if open AI libary supports gemini and GRoq it doesnt mean it will support evry other provider's API will be supported by openAI , as i saw gemini,groq claude evry provider had its own library and  they all had diffrnt own functions names, msgs formats,response strctures  
- this is whre langchain help us : it provide us Same function names, same message format, same response structure  regardless of provider.
- if in case we have to switch provider we can easily switch between the providers by replacing only model name 
- in other case we may have to write entire code again
## Problem 2 — Building step by step is messy
- A real AI App needs many steps like taking input, formatting promt, geting resposne from model,parse that repsponse
- without langchain we will have to connect each and evrystep 
- with lanchaing we can do it all in 1 line of code

## Problem 3 — AI doesn't know your data
the AI know only the data it was trained on ,it nevr saw our course books,company docs etc langchain have tools to load documnts and feed them to AI
## Problem 4 — AI forgets previous messages
- By default the AI has no memory  every message is fresh. LangChain has ready-made memory tools to maintain chat history. like streamlit had sesion state lanchain also have its own way to store data
- by default ChatMessageHistory also stores temporarily like session state 
- but it also gives us option to store data permanently

## Problem 5 — Parsing AI responses is annoying
Sometimes you want the AI to return JSON or a list, not just plain text. LangChain has output parsers that handle this automatically.

# what we use to store chats permanently in general?
database,Redis ,SQLite

# models
- When we say models in LangChain, we mean the AI brain our app talks to.
- jis k pass request jati h
- LangChain supports 3 types:
## Type 1 — Chat Models (most common)
- chat models are like chatgpt clude 
- we send messages it replies with a message.
## Type 2 — LLMs (old style)
- we send a palin txt and LLM complete that txt (sentence)
## Type 3 — Embedding Models (for RAG)
- They work behind the scenes in Chatmodel we interact with chatmodels as users and embedding vectors work in the background
-  when we send txt embeding models convert and returns that txt into numbers we call those numbers vectors
- this model never raed our question ,our documnt  it convert evrything into numbers and then search pages by similiarity and after finding similar data embedding models hands taht data to the chat modles
# Basic Flow of LAngchain:
The basic flow in LangChain is 3 steps:
## 1. prompt tempalte
- its a raedy made msg structure where we just fillin the blanks 
- like we craeted a pdf summarizer whre we set systm promt and user prompt as extracted txt 
sytm prompt will alwys stay as it is user's input will alwys be filled in extarcted txt 
- for example:
- "Tell me a joke about {topic}"
- topics can be a cat,pythn anything user enter
## 2. Model
we send that user's filled prompt to LLM and model think and the return a resposne
## 3. Output Parser
- we take LLM's resposne and conevrt into a format we want by suing langchain's parsing tools
## How they connect:

LangChain uses the | pipe symbol to connect steps — just like a water pipe, output of one flows into the next.
prompt | model | parser
this is called chain

# what prompt templates do, why they are useful, and how they turn variables into a final prompt.  
- A reusable prompt structure with variables.
- It turns input variables into a final prompt by replacing the placeholders in the template with actual values.
- Useful for creating consistent prompts without rewriting them each time.
- It only creates the prompt. It does not call the LLM.

# Chains in LangChain (symbol |)
- in LAngchain Chains are linked pipelines connect multiple componets together
- components Like prompt,LLMs,Output parsers 
- Each component do its own job and pass results to the nxt component 
- the chain just connect all the components so we dont have to write each step (component) manually
# Document Loaders in langchain
- They laod the data from different sources to Langchain so LLM can read it
- Examples:
       - Pdf file :pdf loader
       - website :web loader
       - word file: Docx loader
       - Database:db loader

- Loaded data then become a documnt object with which langchain can wrk further 
- like splitting,embedding,searching
#  text splitters in langchain
- After loading a document, the text is usually too long to send to an LLM at once so you split it into smaller chunks.
### Simple flow:
Big Document → Text Splitter → [Chunk1, Chunk2, Chunk3...]
### Why split?
- LLMs have a token limit (can't read everything at once)
- Smaller chunks = better, focused answers
### Common Splitters:
- CharacterTextSplitter — splits by characters
- RecursiveCharacterTextSplitter — smartly splits by paragraphs → sentences → words (most popular)
- It tries splitting by **paragraphs first** → if chunk is still too big, splits by **sentences** → still too big, splits by **words** → still too big, splits by **characters**. It goes from largest to smallest until the chunk fits within `chunk_size`.
- TokenTextSplitter — splits by token count
- splitting by tokens ensures each chunk never exceeds the LLM's limit
### Key settings:
- chunk_size — how big each chunk is
- chunk_overlap — how much chunks share with each other (so context isn't lost at the edges)
- For example if a sentence starts at the end of chunk 1, it will also appear at the beginning of chunk 2 — so the LLM doesn't miss it.
- if we set it to 50  means 50 characters will be shared between two neighboring chunks.

# output parsers in langchain: 
- By default, LLM returns a raw text response  output parsers help you format that response into what you actually need.
- Without parser:
  LLM response → "The name is John and age is 25"  (just a string)
- With parser:
  LLM response → {"name": "John", "age": 25}  (clean JSON)
- Common Parsers:
     - **Parser**	                               **Use**
      - StrOutputParser	                 ---plain text string
      - JsonOutputParser	                 ---converts to JSON
      - PydanticOutputParser              ---converts to Python object
      - CommaSeparatedListOutputParser	  ---converts to a list
- output parsers save you from manually cleaning the LLM's response yourself.

# Message Histry :
- It stores 3 types of messages:
- **Message**	                   
HumanMessage
AIMessage
SystemMessage

# retrivers in Langchain
A retriever fetches the most relevant chunks of data based on the user's query.
## Simple flow:
User Query → Retriever → Finds relevant chunks → LLM → Answer
## Why needed?
You can't send an entire document to LLM  so retriever picks only the relevant parts.
## Example:
Document = 1000 pages book
Query = "What is photosynthesis?"
Retriever = finds only the 3-4 chunks about photosynthesis
LLM = answers using only those chunks 
How it works internally:
1. Document is split into chunks
2. Chunks are converted to vectors (embeddings)
3. Query is also converted to vector
4. Retriever finds chunks closest to query vector

## Common Retriever:
VectorStoreRetriever (most popular — searches by similarity)

# langchain_core.prompts :
is simply the module inside LangChain that contains all prompt-related classes.