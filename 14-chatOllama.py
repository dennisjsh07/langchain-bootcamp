## https://stackoverflow.com/questions/78162485/problems-with-python-and-ollama

import os
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import OllamaLLM

load_dotenv()

# langsmith tracking
os.environ["LANGCHAIN_API_KEY"] = os.environ.get("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT2_NAME"] = os.environ.get("LANGCHAIN_PROJECT2_NAME")

# chat prompt template
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant that translates English to French. Translate the user sentence.",
        ),
        ("user", "{input}"),
    ]
)

# streamlit framework
st.title("Chat with Ollama LLM")
input_text = st.text_input("Enter text to translate to French:")

# llm initialization
llm = OllamaLLM(model="gemma3:1b", temperature=0.7, max_tokens=512)
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    response = chain.invoke({"input": input_text})
    st.write("Translated Text:", response)
