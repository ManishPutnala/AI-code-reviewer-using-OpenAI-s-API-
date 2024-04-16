from openai import OpenAI
import streamlit as st

key = open('OpenAI app/openai_key.txt')
OPENAI_KEY = key.read()
client = OpenAI(api_key = OPENAI_KEY)

st.title("AI Code Reviewer 🤖")
st.subheader("Get your code reviewed with AI in a blink of an eye ⚡️")

prompt = st.text_input("Enter your python code to debug")
generate = st.button("Review")

if generate:
    response = client.chat.completions.create(
        model = "gpt-3.5-turbo-16k",
        messages = [
        {"role": "system", "content": """You are an expert code reviewer please
        review the given code, debug the code if there are any errors and give me well 	a structured code with an explanation on working of code"""},
        {"role": "user", "content": prompt}
        ]
    )
    st.write(response.choices[0].message.content)
