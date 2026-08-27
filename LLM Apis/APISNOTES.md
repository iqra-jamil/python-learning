# Completion API vs Chat completion API
completion api takes raw text just a plain txt and continue that txt 
chat completion api takes a list of roles role-labeled messages to the model and it generate the nxt assistant reply based on that whole conversation histry
both apis are stateless ,but in chat completion api our application store the chat history not api itself
## Completion API
# what is completion api :
- an API where we send a text(prompt) to the model 
- it continues/predict what comes next
- when we are using compeltion api the model will be a stateless text generator
   - stateless means the model cant remeber or save anything between the requests
   - it will traet each prompt like a new one (like it never saw the prompt before even though hum ny same prompt same chat main phly b bhja ho tab b )

- we will give a prompt to the model and it will continue/complete the text from our prompt 
- it will have no memory of previous prompt or evn its own response till we dont resnd that as a new prompt to it 
- No built-in memory of conversation
- has no roles (roles means labels like system,user or assistant tell the model who said what ,what was its own previous reposne)
## Chat Completion API
# what is chat completion api :

- an API where we send messages (not just plain text) to the model, each message lebeled with a role
- roles = system, user, assistant → tells the model who said what
   - system = instructions/rules for the model's behavior
   - user = what the person is asking
   - assistant = the model's own previous replies

- unlike completion api,  (within one session)
   - it can "remember" the conversation because YOU send the full message history every time
       - This line means: the model itself doesn't actually remember anything — you (or the app/code) are the one resending the entire past conversation (all previous messages) along with your new message, every single time you make a request.

        -  So it looks like the model remembers you, but really it's just seeing the whole history fresh each time because you keep including it in your request.
   - so it's not real memory — the API/app keeps track and resends old messages + new one together each call

- built for multi-turn conversations (back and forth chat)
   - example: user: "tell me a story" → assistant: "..." → user: "make it scarier"
   - the model sees all previous messages + roles, so it stays in context

- structure looks like a list of messages:
[
{"role": "system", "content": "You are a helpful assistant"},
{"role": "user", "content": "I am Iqra"},
{"role": "assistant", "content": "Nice to meet you, Iqra!"},
{"role": "user", "content": "What's my name?"}
]

### NOTE 1  : completion api and chat completion api concepts exist in any api like gemini and groq just use different methods/ functions names

# Responses apis

- Respones api is the newest api end point by the open ai to replace both completion and chat completion api
- it takes model and input (replacing completion api)
- we can set role and content list inside input (replacing chat completion api )


# ROLES: 
- system or devloper
- user
- assistant

# why we create Client object??
- we create Client object because it holds api key and conection setting like base URL
- so because of this on evry api call (client.chat.completions.create(), etc.) it uses same 
authenticated connection instead of we passing our api key manualy evry single time 

# client.chat.completions.create()
 client.chat.completions.create() is exactly what triggers the actual API call (an HTTP request) to the /chat/completions endpoint over the internet.

# NOTE 2 : we can acess other LLM's APIs using openai python library but gemini and groq have their own libraries (other LLM's may also have)