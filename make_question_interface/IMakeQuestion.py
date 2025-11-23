import abc
from make_question_interface.Results import Results

class IMakeQuestion(abc.ABC):
    def make_question(self, question: str):
        pass
    
    def get_answer_text_raw(self) -> str:
        pass
    
    def get_results(self) -> Results:
        pass
    
    def get_implementation_alias(self) -> str:
        pass
