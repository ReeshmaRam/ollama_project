import os
from dotenv import load_dotenv
load_dotenv()
import streamlit as st
##pip install -U langsmith
from langchain_core.prompts import  ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
#from langchain_community.llms import Ollama
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGSMITH_TRACING"]="true"
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")

from langchain_community.llms import Ollama

# Create an instance of the Ollama LLM
llm = Ollama(model="gemma:2b")
out_parsers=StrOutputParser()




prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please respond to the question asked"),
        ("user","Question:{question}")
    ]
)
chain=prompt|llm|out_parsers

# streamlit app
st.title("Langchain Demo With Gemma Model")
input_text=st.text_input("Enter the question in your mind")

if input_text:
    st.write(chain.invoke({"question":input_text}))