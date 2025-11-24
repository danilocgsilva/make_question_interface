from dataclasses import dataclass
import pickle
import base64
import json

@dataclass
class Results:
    raw_answer: any
    raw_answer_serialized: str
    raw_answer_dict: dict
    timestamp_start: float
    timestamp_end: float
    implementation_name: str
    model_name: str
    parameters: dict
    response_content: str
    
    def __init__(
        self, 
        raw_answer: any, 
        timestamp_start: float, 
        timestamp_end: float,
        implementation_name: str,
        model_name: str,
        parameters: dict = None,
        response_content: str = "",
        raw_answer_dict: dict = None
    ):
        self.raw_answer = raw_answer
        self.raw_answer_serialized = self.serialize(raw_answer)
        self.raw_answer_dict = raw_answer_dict if raw_answer_dict is not None else {}
        self.timestamp_start = timestamp_start
        self.timestamp_end = timestamp_end
        self.implementation_name = implementation_name
        self.model_name = model_name
        self.parameters = parameters if parameters is not None else {}
        self.response_content = response_content
        
    def to_dict(self) -> dict:
        return {
            "raw_answer_serialized": self.raw_answer_serialized,
            "timestamp_start": self.timestamp_start,
            "timestamp_end": self.timestamp_end,
            "implementation_name": self.implementation_name,
            "model_name": self.model_name,
            "parameters": self.parameters,
            "response_content": self.response_content,
            "raw_answer_dict": self.raw_answer_dict
        }
        
    def to_json(self, formatted: bool = False) -> str:
        return json.dumps(self.to_dict(), indent=4 if formatted else None)
    
    def get_raw_answer(self):
        return pickle.loads(base64.b64decode(self.raw_answer_serialized.encode('utf-8')))
    
    @staticmethod
    def serialize(content: any) -> str:
        return base64.b64encode(pickle.dumps(content)).decode('utf-8')
    
    @staticmethod
    def deserialize(serialized_content: str) -> any:
        return pickle.loads(base64.b64decode(serialized_content.encode('utf-8')))

