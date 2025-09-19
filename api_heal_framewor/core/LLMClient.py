from typing import Any

from google import genai
from google.genai import types
import os

class LLMClient:
    def __init__(self,api_key:str,model_name:str):
        self.api_key = api_key
        self.model_name = model_name
        self.genai_client=genai.Client(api_key=self.api_key)
        self.model = model_name

    def generate_llm_response(self,prompt:str)-> str | None :
        try:
         resp = self.genai_client.models.generate_content(
            model=self.model,
            contents=prompt)

         return getattr(resp, "text", str(resp))
        except Exception as e:
            print(e)


# Test the client
# client = LLMClient(api_key="AIzaSyAhg_whnBwllZte0L0GiBTXs1Vt5iudwEk",model_name="gemini-2.5-flash")
# promt ='''
# Return only code without any comment explanations markdown
# and contents like ```python  and ``` , backticks should be removed from response
# only working code it returns no extra doc string characters the format like
# function():
#
#   my prompt is reverse a string in Python
# '''
# print(client.generate_llm_response(prompt=promt))