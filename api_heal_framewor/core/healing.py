import json
import re

from core.LLMClient import LLMClient as genai_client
from FileReader import FileReader
from core.review import Reviewer
from core.schema_validator import SchemaValidator


class Healing:
    def __init__(self,payload:dict,schema:dict,error:str):
        self.payload = payload
        self.schema = schema
        self.error = error

    def request_llm_for_healing(self):
        prompt ="""
        Send payload & schema to Gemini and extract corrected JSON only.
        """
        prompt = f"""
                    You are an API auto-healer.
                    Schema:
                            {self.schema}

                    Invalid payload:
                            {self.payload}
                    Error:
                            {self.error}

                    Fix the payload so it passes schema validation.
                    Return ONLY corrected JSON, no markdown, no text.
                  """
        client = genai_client(api_key="AIzaSyAhg_whnBwllZte0L0GiBTXs1Vt5iudwEk", model_name="gemini-2.5-flash")
        fall_back = client.generate_llm_response(prompt)
        print(fall_back)
        return fall_back

#Test


user_payload = FileReader().load_json("requirements/user_payload.json")
user_schema = FileReader().load_json("requirements/user_schema.json")
schema_error = SchemaValidator(payload=user_payload, schema=user_schema)
heal = Healing(user_payload,user_schema,schema_error)
suggestion1=heal.request_llm_for_healing()


# Extract JSON from response
match = re.search(r"\{[\s\S]*\}", suggestion1)

suggestion= json.loads(match.group(0))

reviewer = Reviewer(mode="cli")
if reviewer.review(user_payload,suggestion):
    newpayload = json.dumps(suggestion)
    FileReader.write_json("requirements/payloads_healed.json", json.loads(newpayload))

    is_valid, error = SchemaValidator(suggestion,schema=user_schema).validate_schema()
    assert is_valid, f"Healed payload still invalid: {error}"
else:
    assert False, f"User rejected fix. Error: "