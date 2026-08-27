# Techniques we use to atlk to an AI

- # how we talk to AI 
# system prompts
- they are hidden instructions we use to define AI mode's behaviour
- we set them even when we didn't even start talking to the the AI
- for example Like a job briefing: "You are a customer service agent for a shoe company. Always be polite."
- a user can't see them
# user prompts
- the message a user type to an AI 
- for example : "Write me a poem about dogs."
# giving context
- giving background information of the situation to an AI so that it can understand the situation better
- for example instead of saying "fix this email" say I'm a manager writing to a difficult client who complained last week. Fix this email.
- the more context we will give to an AI the more better answers an AI will give
# constraints
- rules or limits we want an AI to stay in
- contraints keep an AI inside boundaries
- for example :"Answer in under 100 words." "Only use simple English." "Don't mention pricing."
# prompt templates
- a prompt template is basicall a ready made message with blank spaces 
- we can fill those blank spaces every time
- for example : a form: "Write a [type] email to [person] about [topic] in a [tone] tone." You just swap the bracketed parts each time.
-  we can save what worked for us or we can get form communities or from internet
# clear instructions
- being specific about what you want
for example : "Write a short poem" is vague. "Write a 4-line rhyming poem for a 6-year-old about rain" is clear.
- # how we teach AI (types of prompts)
# zero-shot prompting
- asking AI to do  something directly without specifying any example 
- for example : "Is this sentence positive or negative? → I love this phone."
# few-shot prompting
- asking an AI to do something by giving it few examples before asking actual quetion
- so we show it an output pattren by giving it examples
- for Example: Give examples first, then ask.
    - "I love this phone → positive
    - This is terrible → negative
    - Worst purchase ever → negative
    - i hate this phone - ?
- we showed it 3 examples of the pattern first. Now it knows exactly what we want when it sees the real question.
# chain of thought 
- we tell AI to think step by step before asking
- for Example : "A shop has 24 apples. They sold half in the morning and 4 more in the evening. How many are left? Think step by step."

      - Instead of just saying "8", the AI will walk through it:
      - Start with 24
      - Half sold in morning → 24 ÷ 2 = 12 left
      - 4 more sold in evening → 12 − 4 = 8 left
      - Answer: 8
- The phrase "think step by step" is literally all we need to trigger this. It stops the AI from rushing to an answer and forces it to work through the problem properly.
- # what we get back
# output formatting
- telling AI how to present its Answers (the format it should use)
- For Example: "Give me a bullet-point list." "Use headers." "Write it as a table."
# structured output
When we want the answer in a neat, organized format that a computer can easily read or process, not just free-flowing text.
# JSON output
- JSON means key-value pairs
- the format we use to store and share data across the systems
- we instruct AI to give answr in JSON format so that websites or an APPs can use it
- For Example : A real life situation where this matters:

- Imagine we're building a CV reading app. Hundreds of CVs come in as plain text. we need to pull out name, experience, and skills from each one.

- Our prompt would be:
    - "Read this CV and extract the information. Reply in JSON only with these fields: name, years of experience, skills."
- Now Oir app gets clean, organized data from every CV automatically. No human needed to read and sort them.
# question-answering prompts
- we give the AI some information, then ask questions about it.
- For Example:  "Here is a document. Based on this, what is the return policy?" 
- The AI reads what we gave it and answers from that.
- # What we ask AI to do
# extraction prompts
- we give AI a big chunk of Text and ask it to extract some specific pieces of info from it
- for example: "From this article, extract all the dates and names mentioned."
# classification prompts
- we ask AI to put things in categories
- for example we can give it multiple customer reviews and then ask it
- "are these customer reviews positive, negative, or neutral?" 
- The AI reads them and puts the review in a bucket (category).
# summarization prompts
- asking AI to shorten something while keeping the key points
- "Summarize this 5-page report in 3 sentences."
# rewriting prompts
- asking Ai to change how something is written while keeping its meaning same (change wording)
- for eaxmple : "Rewrite this in simpler English." "Make this more formal." "Make this shorter."

# Prompt Injection
- Prompt Injection is when someone hides fake instructions inside text that the AI is supposed to just read, in order to trick the AI into forgetting your real instructions and following theirs instead.
- AI may forget its own real rules and instructions and start following unintened(ghair iraadi) commands
- Prompt injection can come from the user, but also from anything the AI is told to read — because the AI can't always tell the difference between content and commands.
- Where it comes from : and     Who is responsible
     - User types it 	         The user
     - Webpage content	         The website owner
     - Document or file /email    Whoever made the file
      