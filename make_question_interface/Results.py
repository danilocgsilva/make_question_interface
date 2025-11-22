from dataclasses import dataclass

@dataclass
class Results:
    raw_answer: str
    timestamp_start: float
    timestamp_end: float
    implementation_name: str
    model_name: str
    
    def __init__(
        self, 
        raw_answer: str, 
        timestamp_start: float, 
        timestamp_end: float,
        implementation_name: str,
        model_name: str,
        parameters: dict = None
    ):
        self.raw_answer = raw_answer
        self.timestamp_start = timestamp_start
        self.timestamp_end = timestamp_end
        self.implementation_name = implementation_name
        self.model_name = model_name
        self.parameters = parameters if parameters is not None else {}
