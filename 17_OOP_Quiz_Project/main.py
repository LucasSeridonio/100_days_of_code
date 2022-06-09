from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank = list()

for question in question_data:
    question_bank.append(Question(question.get("text"), question.get("answer")))

QuizBrain(question_bank).next_question()

#for q_model in question_bank:
#    print(q_model.text, q_model.answer)