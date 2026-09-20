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

