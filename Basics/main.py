## Integrate our code OpenAI API

import os
from constants import openai_key
from langchain_community.llms import OpenAI
import streamlit as st

os.environ["OPENAI_API_KEY"] = openai_key

# streamlit framework specific
st.title("Langchain Demo with OpenAI API")
input_text = st.text_input("Search the topic you want")


# Initialize OpenAI LLM
llm = OpenAI(temperature=0.8)

# Define the function to generate a question-answering model response

if input_text:
    st.write(llm(input_text))