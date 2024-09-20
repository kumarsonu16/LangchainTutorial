## Integrate our code OpenAI API

import os
from constants import openai_key
from langchain_community.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain

import streamlit as st

os.environ["OPENAI_API_KEY"] = openai_key

# streamlit framework specific
st.title("Langchain Demo with OpenAI API")
input_text = st.text_input("Search the topic you want")


# Initialize OpenAI LLM
llm = OpenAI(temperature=0.8)

#Propmt Template
first_input_prompt = PromptTemplate(
    input_variables=["name"],
    template="Tell me about celebrity {name}"
)

# Initialize LLM chain
chain = LLMChain(llm=llm, prompt = first_input_prompt, verbose=True, output_key='person')

second_input_prompt = PromptTemplate(
 input_variables=["person"],
 template="when was {person} born"   
)

chain2 = LLMChain(llm=llm, prompt = second_input_prompt, verbose=True, output_key='dob')

third_input_prompt = PromptTemplate(
 input_variables=["dob"],
 template="Mention 5 major events happend around {dob} in the world"   
)

chain3 = LLMChain(llm=llm, prompt = third_input_prompt, verbose=True, output_key='description')

parent_chain = SequentialChain(chains =[chain, chain2, chain3], input_variables=['name'], output_variables = ['person','dob', 'description'], verbose=True)

# Define the function to generate a question-answering model response

if input_text:
    st.write(parent_chain({'name':input_text}))