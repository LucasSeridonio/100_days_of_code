class QuizBrain:
    def __init__(self, q_list) -> None:
        self.question_number = 0
        self.question_list = q_list
    
    def next_question(self):
        q = f'Q.{self.question_number}: {self.question_list[self.question_number].text} (True/False)?: '
        input(q)