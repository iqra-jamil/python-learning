# Embeddings + Vector Databases

## what are embeddings and vectors
- Embedding is the process of converting information like words,sentences,paragraphs in to lists of numbers so that computer can understand their meaning
- vectors are the lists of numbers we get after converting info like wrds, parahraphs ,sentences ,images in to numbers, those numbers are called vectors

## text to vectors
- A vector is jsut a list of numbers
- we dont pick numbers randomly a trained model pick numbers for a wrd or something automatically,
- if two wrds have almost same meaning they may have almost same numbers 

## semantic similarity
Semantic : meaning 
similiarity : how close or how realted the things are
sematic similiarity mean do these two pieces of txt have same meaning
for example "dog" & "puppy"	✅ Very similar
"car" & "banana"	❌ Not similar
## vector space
- A vector space is a mathemaical environment whre all the vectors stay together
- when we embed 1000 of documnts ,evry single doc will become a vector they all will saty together inside one shared place ,so that we can compare later 
- so when user will send a query the querie's vectors will get compare tothe vectors we have inside vector space

## What we Actually Do With Vector Space in Real Projects
Task	                     What happens in vector space
Semantic search	             Find vectors closest to your query vector
Recommendation	             Find vectors closest to what user liked
Clustering	                 Group nearby vectors into topics
RAG (AI + your docs)	     Store doc vectors, fetch closest ones to answer questions
## cosine similarity
- Cosine similiarity is just a way to measure how similiar two vectors are
- and we measure similiarity by chking the angke between them
- small angke means similar meaning and large angle means differnt menaing 
- 0 degree angle means identical meaning, 180 degree means total opposite meaning, 90 means unrelated meaning,45 similar
- we can find the angle betweenthe vectors buy using the foloowing formula
 cosine similarity = A.B/|A|X|B|
 -  A.B= multiply each matching number and add them all up
 - |A| × |B| = multiply the lengths of both vectors
 - after finding angle from vectors we apply cos functions like cos(90),cos(180) to get cosine score 
 - smaller angle (0) means higher cosine score
 - higher coisne score menas vectrs are idntical
 - score stays between Between -1 and 1.
# whats the difference between sematic similarity and cosine similary?
**Semantic similarity** — the *concept* of how similar two texts are in meaning.

**Cosine similarity** — the *math formula* used to measure that semantic similarity.
## embedding models
- its a pre trained AI- model that take txt as input and convert that txt into vectors
- vectors _ A list of numbers that represent meaning of that txt 
- we don't build them we just call them via API and get vectors back
- We as developers do it we write code to send text to an embedding model and get vectors back, it does not happen automatically.
- When we need a computer to understand and compare meaning  search, recommendations, chatbots, finding similar documents.
- We store them in a vector database and later search/compare them using cosine similarity (score) to find similar meanings.
## creating embeddings
creating embedding means :
- pick an embedding model
- call it via API
- get vectors back
- store those vectrs in db
## Differ between Vector space and Vector database?

- Vector space is just a mathemetics calculation we use to find similrity between vectors or we use to compare diffrent vectrs 
- vector database is actula software we use to stoir vectors tand run vector space calculations for us


# What is a Vector Database?
- a normal db store txt,numeric values dates etc (like WHERE name = 'iqra' or WHERE age = 24 )
- a vector db store vectors
- and we search by meanings in vector dbs not by exact match
- we frst convert user's query txt into vectors then we comapre its vectors with vectore we have stored in vector db
- we find similarity between both by using cosine similarity


# FAISS(pronounce as faise (like dice))
- Facebook AI similarity search
- its an open source library developed by meta we can use for fast similarity serach
- and used for clustring high dimensional dense vectors
- clustring - grouping similar vectors together based on theri meanimg
- High dimension - vectors with thousands of numbers (like 1536 dimension) 
- dimension here means length /size of vectors (how many numbers are stored inside a vector) not array dimension
- dense - every number in the vector has a value not zero
- we cant store meta data in it 
- its a large scale ,fast libaray
- FAISS can only search vectors efficiently  for storing and managing you have to handle that yourself with Python code or another tool.
- we cant store vectors & metadata too
- its developed by meta 
# ChromaDB
- its an opn source database designed to store,manage , and search vector embeddings for AI applications
- developed by chroma , its beginer friendly , we can use it for Learning, small projects
- we can store meta data in it 
- it act as a memory layer of LLMs
- we can use it for RAG systems
# storing vectors
we store vector embedding in dbs so that we can search vectors later
# storing metadata
- meta data is extra info of a vector
- like orignal txt,date, author name 
- along wioth vectors we also store metadata
# similarity search
- we give query ,it is coverted in to vectors
- now we have quey vectors and vectors stored inside a db
- query vectors will be compared with stored vectrs and vectrs with highest cosine similarty will be returned
# top-k results
- Instead of returning all results, return only top 3 or top 5 most similar ones.
- n_results=3  # return top 3 most similar
# metadata filtering
- Narrow results by metadata before searching by vectors
- where={"author": "iqra"}
- now we can search by vectors only the documnts with author name iqra

# Chromadb
the basic flow is to:
- create a client wihc connect our app to chroma db
- create collection: create a container or acess  a conatiner to store data
we can acess or fetch it from somewhre
- collection.add() store metadats,ids,docs,embeddings inside it
- collection.get() to retrive data from db
- query() → perform similarity search and get relevant records, usually top-k results.
- chroma db dont retrn cosine similarty it return distance 
less distance= more similarty
high cosine similarty= less similarty
 - so in query we can give query txt or qury embeding vectrs
 - if we alredy calls embedung model to convert qury txt in to vectrs we will use 
 query_embeddings parameter if we didnt then we will use query_txt parameter 
 - we use "where" parameter for filter by metadata
 - query_embeddings expects a list of vectors
