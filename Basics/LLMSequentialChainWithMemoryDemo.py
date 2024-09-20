## Integrate our code OpenAI API

import os
from constants import openai_key
from langchain_community.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from langchain.memory import ConversationBufferMemory

import streamlit as st

os.environ["OPENAI_API_KEY"] = openai_key

# streamlit framework specific
st.title("Langchain Demo with OpenAI API")
input_text = st.text_input("Search the topic you want")


# Memory
person_memory = ConversationBufferMemory(input_key='name', memory_key='chat_history')
dob_memory = ConversationBufferMemory(input_key='person', memory_key='chat_history')
desciption_memory = ConversationBufferMemory(input_key='dob', memory_key='desciption_history')

# Initialize OpenAI LLM
llm = OpenAI(temperature=0.8)

#Propmt Template
first_input_prompt = PromptTemplate(
    input_variables=["name"],
    template="Tell me about celebrity {name}"
)

# Initialize LLM chain
chain = LLMChain(llm=llm, prompt = first_input_prompt, verbose=True, output_key='person', memory=person_memory)

second_input_prompt = PromptTemplate(
 input_variables=["person"],
 template="when was {person} born"   
)

chain2 = LLMChain(llm=llm, prompt = second_input_prompt, verbose=True, output_key='dob', memory=dob_memory)

third_input_prompt = PromptTemplate(
 input_variables=["dob"],
 template="Mention 5 major events happend around {dob} in the world"   
)

chain3 = LLMChain(llm=llm, prompt = third_input_prompt, verbose=True, output_key='description', memory=desciption_memory)

parent_chain = SequentialChain(chains =[chain, chain2, chain3], input_variables=['name'], output_variables = ['person','dob', 'description'], verbose=True)

# Define the function to generate a question-answering model response

if input_text:
    st.write(parent_chain({'name':input_text}))
    
    with st.expander('Person Name'): 
        st.info(person_memory.buffer)

    with st.expander('Major Events'): 
        st.info(desciption_memory.buffer)