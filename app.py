'''
Agenda : Text to SQL LLM Application
prompt --> LLM --> Gemini pro --> Query --> SQL --> Database 
--> Response
Implementation:
1. SQLlite --- Inssert some records -- python programming
2. LLM Application --> gemini pro ---> SQL Database
'''

from dotenv import load_dotenv
import os
load_dotenv()

import streamlit as st
import sqlite3

import google.generativeai as genai
genai.configure(api_key=os.getenv("GENAI_API_KEY"))

# Function to load gemini model and priovide query as response 

def get_gemini_response(question,prompt):
    model =genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt, question])
    return response.text