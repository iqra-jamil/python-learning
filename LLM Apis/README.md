
# generative AI :
gen AI is an AI that can generate new content
- txt ,images,vidoes,audios,code generators
# what is LLM 
- large language model
- LLM means AI model trained on huge amount of text ,so that it can understand and generate human language
- so an LLM's main job is to understand and generate huamn language
- LLM is one type of AI model
# why we use LLM's APis 
 we use just LLM's APIs to create our own apps
# if LLM is only about text then what about video ,images etc

- LLM specifically means large language model ,so its main focus is language (text).
- imges and vidoes are not automatically LLMs
- for example GPT can process text and images too so those models are multimodel models
- model that generate images generally called image generation models (same for videos)
- So, LLM ≠ every type of generative AI. LLM specifically refers to language models.
### Modren systems are still built on large language model at the core ,but have been extended with multimodal abilities(like generatng images ,audios ,videos)
### Note :  generative AI is a broad terms , LLM is one type of gen AI focus on language (txt)

## terms (are related to LLMs only):
# 1. nxt token prediction:
- an LLM generates txt, by predicting what next token should be ,based on the tokens it alredy have seen
- the important point is that an LLM does not generate whole sentence at once ,it generates it step by step by predicting nxt token 
- the process start from the promt we enter ,an LLM use that prompt and predict the nxt token 
- for exmaple user: i am learning The model predicts a likely next token:
“Python”
- Python could be one token or split into multiple tokens, depending on the tokenizer.
- a tokenizer is the system that breaks text into tokens so the LLMs can process them
- each and evrything an LLM shows as a response ., space are tokens
# 2. tarining,
- training is the process,whre an LLM learns pattrens from the huge amount of data
- for example it see many examples like:
  “I am learning Python.”
- it learns the language pattrens from the examples and then predict the nxt tokens

# 3. tokens,
- tokens are the small pieces of txt that an LLM process (or pridicted)
- a token can be a whole word,part of a word or punctuation
### Q. whats the differnce between text and tokens?
- Text is the raw human readable string (letters,words,sentences) that we read and write
- Tokens: are the smaller chunks (words,sub-words or punctuations) that an LLM generate by splitting taht txt into interally to process and generate that language 
# 4. context window,
- context window is basically LLM's short trem memory
- context window means kitna txt aik model aik dfa mian process kar skta h ya daik skta 
- us txt ko word main nai blky tokens main measure kia jata h
- agr conversation bhot lambi chli jaati h aor aik specific limit hit ho jati h to model earlist conversation ko bhulna shuru kr dy ga 
- like normal real life conversation main hota h k humy convo ke start ke baaten yaad nai rehti aor last mint baaten hamri memory main reh jati hain
- for example agr context window = 1000 tokens and our convo reaches 1200 tokens ,oldest 200 tokens will be pushed out and model no longer sees them 
# 5. hallucination,
- ### what is it :
Hallucination is when a model generate information confidently that sounds correct ,but thats actually wrong
- ### Why:
- model ko facts ka nai pta hota 
- still wo nxt word ko un pattrens ke base par predict krta h jo us ny leran kiy hoty hain
- so agr model ko kisi cheez ka nia pta to "i dont know" kheny k bajay wo aik aisa response/answer generate krta h jo bazahir sahi lagta h lkn wo sahi hota  nai h 
- ### Simple analogy: 
It's like a student who didn't study but is confident in exams — they'll write a fluent, well-structured answer... that's completely made up.
# 6. knowledge cutoff, 
- the last date on which model was trained on a huge amount of information/data ,the model will have no knowledge about the evnets happens after that date 
- until its given internet/search acess
- Simple example: If a model's knowledge cutoff is January 2026, it won't know about news, events, or updates from February 2026 onward, unless it searches the web to check.
# 7. temprature
- ### what is it :
- setting that controls how random or how creative answers of an LLM are
    - Low temperature (like 0 or 0.2): safe,predictable or focused (good for maths ,codding or facts )
    - High temperature (like 0.8 or 1): creative ,or sometimes more suprising answers (good for brainstorming or stories)
- ### Simple example: 
Low temperature is like a careful student giving the "textbook" answer every time. High temperature is like a creative writer who might come up with something unexpected each time you ask.

## LLM vs model : An LLM is a type of AI model specifically designed to understand and generate language.
# -----------------------------------LLMs APIs---------------------------------------------------
# - • OpenAI API:
# - • Gemini API
# - • Groq API

# Question arises while studying LLM APIs
- whats OPEN AI whats Groq and Are they LLMs or companies
- how they all are different from each other and 
- why and when and in which cases i should use them how to choose which one to use in my project

## The simple picture
- point # 1: Open AI,groq,google are companies
- point # 2: Open AI create models + provide APIsto acess its own models like GPT models
- point # 3: Google create models + provide APIs to acess its own models like gemini 
- point # 4: Groq povide very fast infrastructure,provide APIs to run its own model including models created by others
- point # 5 : so evry model we are acessing through Groq's APi ,it does not means that Groq owns it
- point # 6: Groq is primarily the infrastructure/inference provider
- point # 7: infrastructure means computer and hardware system we need to run AI models
- point # 8 : inference : the process of actually running the model,to generate answers 
    - if a company craeted a model and then tarined it and then give that trained model to the groq to run it on its own infrastructure that process is inference 
    - running the trained model to make predictions , or generate outputs from inputs (new ,unseen data,prompts) is called inference 
- point # 9: so Groq provide its own hardware and computer systems to run an AI model very quikly 
- point #10 : suppose a model was craeted by another company groq provide its own infrastrcture to run that model quickly 
# - • model selection
- choosing which AI model to use (e.g., gpt-4o, gpt-4o-mini, gemini-1.5-flash)
- bigger models= high cost,slower but smarter
- smaller models= faster ,cheaper but less smarter
# - • system messages
- initial instruction given to LLM before user's inputs 
- these instructions set AI's behaviour/ role before the convo starts user never see this
- its set by the devleoper during devlopment,dev set it in the code
# - • user messages
- Actual question/ prompt from the person using the app like we give prompts to chatgpt
- this is how we send our query to the model
# - • conversation messages
conversation msgs are the different msgs inside a chat means user's prompts and LLM's responses(including system msgs)
# - • temperature
a setting that control how random or how creative answers of LLM are (discussed earlier)
# - • max tokens
- max tokens means maximum tokens an LLM is allowed to generate in its response
- it control single response not total conversation
# - • response handling
- response handling is what your app does with the LLM's response after it(app) recieve it(LLm's response)
- example:
LLM gives response--> our app rcve it --> app display LLM's response to the user(handled it by displaying it to the user)
# - • Streaming responses
- Streaming Response means LLM is sending response little by little as it generated , instead of waiting and sending entire response at once
- example : chatgpt is typing the answer gradualy is an example of streaming response
- if the resposne from an LLM is fast its not streaming response,we can call it fast inference or fast speed response
# - • basic token usage
- it means understanding how many total tokkens our API request uses.
- Total token usage = input tokens(tokens in prompts + other input msgs) + output tokens(tokens in LLM's response)
