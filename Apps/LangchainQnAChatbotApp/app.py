## Conversational Q&A Chatbot
import streamlit as st

from langchain.schema import HumanMessage,SystemMessage,AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

## Streamlit UI
st.set_page_config(page_title="Conversational Q&A Chatbot")
st.header("Hey, Let's Chat")

# load environment variables
load_dotenv()

# Create LLM instance
chatllm = ChatOpenAI(
    api_key=os.environ.get("OPEN_API_KEY"),  # Ensure this is set in your environment variables
    temperature=0.6,
    max_tokens=150,  # Specify a value or use default
    timeout=60,      # Specify a value or use default
    max_retries=2,
    model="gpt-3.5-turbo"  # Corrected model name
)

# Check flownessage message is available 
if 'flowmessages' not in st.session_state:
    st.session_state['flowmessages']=[
        SystemMessage(content="Yor are a comedian AI assitant")
    ]

## Function to load OpenAI and get respones

def get_chat_response(question):
    st.session_state['flowmessages'].append(HumanMessage(content=question))
    answer = chatllm(st.session_state['flowmessages'])
    st.session_state['flowmessages'].append(AIMessage(content=answer.content))
    return answer.content

## Main chat loop

input= st.text_input("Input: ", key="input")
response = get_chat_response(input)

submit = st.button("Ask the equestion")

## If ask button is clicked
if submit:
    st.subheader("The Response is ")
    st.write(response)
    