import abc

class IMakeQuestion(abc.ABC):
    def make_question(self, question: str):
        pass
    
    def get_answer_text_raw(self) -> str:
        pass
