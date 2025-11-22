from dataclasses import dataclass
import pickle
import base64

@dataclass
class Results:
    raw_answer_serialized: str
    timestamp_start: float
    timestamp_end: float
    implementation_name: str
    model_name: str
    parameters: dict
    
    def __init__(
        self, 
        raw_answer: any, 
        timestamp_start: float, 
        timestamp_end: float,
        implementation_name: str,
        model_name: str,
        parameters: dict = None,
    ):
        self.raw_answer = raw_answer
        self.timestamp_start = timestamp_start
        self.timestamp_end = timestamp_end
        self.implementation_name = implementation_name
        self.model_name = model_name
        self.parameters = parameters if parameters is not None else {}
        self.raw_answer_serialized = base64.b64encode(pickle.dumps(raw_answer)).decode('utf-8')
