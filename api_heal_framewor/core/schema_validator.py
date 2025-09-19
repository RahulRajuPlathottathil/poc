from jsonschema import ValidationError,validate



class SchemaValidator:
    def __init__(self,payload:dict, schema:dict):
        self.payload = payload
        self.schema = schema

    def validate_schema(self):
        try:
            validate(instance=self.payload, schema=self.schema)
            return True, None
        except ValidationError as e:
            return False, str(e)