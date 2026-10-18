# Function Calling / Tool Calling
## What tool calling is
## Tool schemas
## Arguments
## LLM choosing a tool
## Executing Python functions
## Returning tool results to the LLM
## Multiple tools
## Tool errors



##  1. What is tool calling in LLMs?
Tool calling allows an LLM to request external tools, services, or functions through an application. It helps the LLM perform tasks or access information that it cannot reliably handle on its own.

## - function calling vs tool calling 
" Function calling" was the older term, and "tool calling" is the newer, more general one. It's more general because a tool can be more than a function, like web search or code execution.
## when to use tool calling?
- Database query: the LLM asks for a function that fetches a user's orders from your database.
- Sending email: the LLM asks your code to send a message, and your function does it.
- Calculator: LLMs can be bad at exact math, so a function does the calculation.
- Reading files: the LLM asks for a function that opens a PDF or file and returns its text.
- Calendar or booking: the LLM asks your code to check free time or book a slot.
## Why do LLMs need tool calling?
An LLM needs tool calling to access external information and perform tasks that it cannot reliably handle on its own.
## How does tool calling work internally?

### Step 1. Tool calling allow an LLM to call external tools through application to perform tasks which it cant perform on its own 
- An LLM is a model which receive user’s question and generate response
- External tool is something our application  make available to the LLM
- It could be a python function,database query/operation,API
- But LLM  can’t acess every external tool,it can acess only the tools our application connect it to 
- For example our application provide these three tools:
       - A calucualtor function(simply performing calculations)
       - A weather API
       - A function searching database
- Tool calling will allow LLM to call one of thses toolswhen it needs one
- The important point is LLM request a tool through application . application manage the execution according to the request
- A calculator function or any normal function we write in the code is not a part of tool calling till LLM can’t choose it ,our application execute it ,and return result of the function to the LLM

### Step 2. "The LLM decides which tool is needed."
- When a user ask the question an LLM receive the user’s question with the information about the available tools
- The LLM then decide whether it can generate answer on its own or it should use a tool or if should use a tool then which tool it should use 
- Suppose the user asks a question that requires retrieving a record from a database.
- The LLM can identify that the database search tool is appropriate for this task.
- How an LLM decide which tool to choose ?
          - When an LLM recive user’s quetion along with info about the avilible tools that info include each tool’s name , description, and expected input(tool schema) based on that information an LLM decide which tool to choose 
- This is the decision step
- The tool is not executed yet ,here only an LLM is deciding which tool to request

### Step 3. "The LLM generates a structured request with the required information."
- Now as LLM chooses which tool to request ,now and LLM needs to communicate that request  to the application
- It communicate with an application by generating a structured request 
- Structured here means the request usually follow a format that application can process
- One common format is JSON for example :
   {"tool": "get_stock_price", "args": {"name": "AAPL"}}
- This request tells the application two main things:
    1.	Which tool the LLM wants to use.(tool’s name)
    2.	 What information the tool needs to perform the task
- The information here means the tool’s argument or the required input the function need to perform task
- Why is this necessary?
    - So that an application can identify which tool to use and can return the correct results
    - A structured applicaton makes it possible
- At this stage an LLM requested a tool ,the tool is not executed yet


### Step 4. "The application executes the tool."

- Now our application recive the structured request from the LLM (with args+tool name)
- Our application code now will identify the corresponding tool or function according to request
- Now our application will pass the required args to the tool or function and execute it
- The tool perform its actual task 
- For example, a Python function might process a calculation, or an API request might retrieve information from an external service.
- The important distinction is :
    - The LLM request a tool according to the task and application execute the requested tool
- The application must also validate inputs and ensure that the model can only request tools that the application permits.

### Step 5. "The application returns the result to the LLM."
- After executing the tool the application receive its results
- The result might contain a calculated number, database records, or information returned by an API.
- The application then send the results back to the LLM as a part of tool calling conversation
- Why send it back?
     - Because the LLM needs the result to continue the process and formulate its response.
     - Without receiving the result, the LLM would not know what the tool actually returned.
- The tool's output and the LLM's final response are two different things. A tool returns data or a result. The LLM can turn that result into a response that makes sense to the user.

### Step 6. "The LLM generates a response for the user."
- Now the LLM recv the returned tool result
- An llm uses two things to generate answers
       - User’s question
       - Returned information
- Our application then displays the ansr to the user 
- The final anser generated by an LLm and the returned information both are different
- At this point, the process is complete if the LLM produces a final response. 
- Sometimes the LLM may request another tool, in which case the application repeats the execution and result-return steps.



## What is a tool schema?
- A tool schema define structure and requiremnts of tool's input
- it specify what arguments tool need , what should be the data type of arguments,what areguments are required(should must be provided)
- an LLM use this information to generate the request which it send to the application

## What information does a tool schema contain?
A tool schema contains:

1. Tool parameters, the inputs the tool needs.
2. Data types, such as string, number, or boolean.
3. Required fields, the inputs that must be provided.
4. Parameter descriptions, what each input means.
5. The expected input structure, often defined using JSON Schema.

## What are tool arguments in LLM tool calling?
- Tool arguments are the input values an LLM provides when requesting a tool.
- They tell the tool what information to use to perform its task.
- For example, a calculator tool might receive the arguments a = 5 and b = 10.
## How does an LLM decide which tool to call?
An LLM decides which tool to call based on the user's question and the tool information provided by the application, information includes the tool's name, description, and expected inputs.
## How does an LLM generate arguments for a tool?
an  LLM generate arguments for a tool by extracting the required information from user's question and match that extracted information with tool schema which will have(wihc arg,arg's data type etc)
## How does an LLM call a Python function?
The LLM sends a structured request to the application containing the Python function’s name and its input values or arguments. The application then executes the function and returns the result to the LLM.
## What happens after the Python function executes?
After the Python function executes, the application returns its output to the LLM, which uses the result to generate a response for the user.
## How are tool results returned to the LLM?
The application sends the tool's output back to the LLM as a tool result in the conversation, allowing the LLM to use it to generate the final response.

## How does the LLM use the tool result to generate the final answer?
- an LLM rcv tool's output and conversation context 
- LLM understand how output is related to the user's question
- and LLM generate the final anser based on that
- if the 1 tool output can't fully anser the user's question it may requet another tool call or explain whats missing
## How does tool calling work with multiple tools?
- When multiple tools are available, the LLM chooses the tool that best matches the user's question based on each tool's name, description, and schema.
- If the task requires multiple tools, the LLM can request them one after another. The application executes each requested tool and returns its result to the LLM. The LLM then uses those results to generate the final answer.
- the LLM can receive the first tool's result, then decide whether to request a second tool based on that result.
- However, if the tools are independent, the application may execute multiple tool calls in the same round before returning their results to the LLM.
- Both are possible. The LLM can request multiple independent tools at once, or request them one by one when the next tool depends on the previous tool's result.
## How does an LLM choose between multiple tools?
- An LLM chooses between multiple tools based on the tool's name, description, and schema.
     1. Name: Identifies what the tool is called.
     2. Description: Explains what the tool does and when to use it.
     3. Schema: Defines the required parameters and their data types.
- The description helps the LLM decide which tool fits the user's request. The schema helps it generate the correct tool call.
## What happens when a tool call fails?
- When a tool call fails:
     1. The tool returns an error message instead of the expected result.
     2. The LLM receives the error message.
     3. The LLM may retry the call, correct the arguments, choose another tool, or explain the problem to the user.
- The LLM's next action depends on the error and its instructions.
## How should tool errors be handled?
Tool errors should be handled by checking the error message, correcting the problem, and retrying if appropriate. If the tool still fails, the LLM can try another tool or inform the user that it could not complete the task.
## What happens if the LLM provides invalid tool arguments?
- If the LLM provides invalid tool arguments:
    1. The tool or validation system rejects the arguments.
    2. An error message is returned to the LLM.
    3. The LLM can correct the arguments and try again.
- For example, if a tool requires a number but the LLM provides text, the system may reject the call.
## What is the difference between normal function calling and tool calling?
Normal function calling means calling a function directly in your code. Tool calling means the LLM decides when to call a function or external tool based on the user's request.
Example:
Normal function calling: Your code calls get_weather() directly.
Tool calling: The LLM decides to call get_weather() because the user asks about the weather.
19. What is the complete flow of an LLM tool calling system?
- already discussed 
# practical
20. How to implement LLM tool calling with Python
21. How to define tools with JSON schema
22. How to implement multiple tools with Python and an LLM
23. How to handle tool calling errors in Python


# --> Points To Remember ::

- an LLM is trained on Text and other data like audios,videos,code depends on model and generate responses based on that data
- an LLM can't have information about the events happens after its last training 
- it does not alwys need external sources to generate evry resposne
- aik LLM ko external tools ke zrurat tab hoti hai jab aik task ke required info ya action aik LLM  ke existing capabilities perform na kr sken
- like an LLM can perform simple calcualtions because it was tarined on text , but for complex caclculation we may need to call a calcualtr tool for reliable results
- we can say tool calling is a building block and automation is what you build with it
- anything the LLM can't do alone becomes a function.
- Tool schema mein actual value 5 nahi hoti. Usmein argument ka naam, datatype aur requirements define hoti hain.
- For example, agar argument age hai, to schema batayega ke age ek number hona chahiye.
- Jab user question mein age 5 batayega, to LLM actual argument value 5 generate karega.
- Yani schema mein rule hota hai, actual value nahi.

- #### bind_tools() is a method provided by LangChain chat models, including ChatGroq.
- #### use python's built in loader bcz we need a dictionary not a documnt,langchian dont have any loader that can return raw json as a python dictionary
- ## from langchain_groq import ChatGroq  packege hai or us main classes hain