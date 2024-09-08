# from langchain_core.prompts import ChatPromptTemplate 
# from langchain_core.output_parsers import StrOutputParser
# from langchain_community.llms import Ollama 
# import streamlit as st 


# import os    
# from dotenv import load_dotenv 

# load_dotenv()

# ##################Langsmith tracking #############################
# os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
# os.environ["LANGCHAIN_TRACING_V2"] = "true" 
# os.environ["LANGCHAIN_PROJECT"] ="Q&A Chatbot Using Ollama"


# #####Setting the Prompt Template #######
# prompt = ChatPromptTemplate.from_messages(
#     [
#         ("system", "You are a hepful assistant. Please response to the user queries"),
#         ("user", "Question: {question}")
#     ]
# )


# def generate_response(question, llm, temperature, max_tokens):
#     # openai.api_key = api_key
#     llm = Ollama(model=llm)
#     output_parser = StrOutputParser()
#     chain = prompt|llm|output_parser 
#     answer = chain.invoke({"question":question})
#     return answer 



# ######################################## STEAMLIT APP #########################################

# ################ App Title #########################################
# st.title("OLLAMA Enhanced Q&A Chatbot")


# ######################################## Sidebar For Settings #########################################
# st.sidebar.title("Settings")
# # api_key = st.sidebar.text_input("Enter Your OpenAI API Key", type="password")

# ######################################## Setting up a Dropdown to select various openai model #########################################
# llm=st.sidebar.selectbox("Select an Open AI Model", ["gemma2:2b", "mistral", "phi3"])


# ######################################## Adjust response parameters #########################################
# temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)
# max_tokens = st.sidebar.slider("Max Token", min_value=50, max_value=300, value=150)


# ######################################## Defining The main interface for getting user input #########################################
# st.write("Feel free to ask your question below:")
# user_input = st.text_input("You:")


# if user_input:
#     response=generate_response(user_input,llm, temperature, max_tokens)
#     st.write(response)
# else:
#     st.write("Awaiting your input. Please enter a question.")


from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

##################Langsmith tracking #############################
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Q&A Chatbot Using Ollama"

#####Setting the Prompt Template #######
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user queries"),
        ("user", "Question: {question}")
    ]
)

def generate_response(question, llm, temperature, max_tokens):
    try:
        llm = Ollama(model=llm)
        output_parser = StrOutputParser()
        chain = prompt | llm | output_parser
        answer = chain.invoke({"question": question})
        return answer
    except Exception as e:
        return f"An error occurred: {str(e)}. Make sure the model is pulled using 'ollama pull {llm}'."

######################################## STEAMLIT APP #########################################

st.title("OLLAMA Enhanced Q&A Chatbot")

######################################## Sidebar For Settings #########################################
st.sidebar.title("Settings")
llm = st.sidebar.selectbox("Select an Ollama Model", ["gemma2:2b", "mistral", "phi3"])
temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)
max_tokens = st.sidebar.slider("Max Token", min_value=50, max_value=300, value=150)

st.write("Feel free to ask your question below:")
user_input = st.text_input("You:")

if user_input:
    response = generate_response(user_input, llm, temperature, max_tokens)
    st.write(response)
else:
    st.write("Awaiting your input. Please enter a question.")
