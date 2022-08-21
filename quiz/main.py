from question_model import Quesiton
from data import question_data
from quiz_brain import QuizBrain

question_bank=[]
for q in question_data:
    new_question = Quesiton(q["text"], q["answer"])
    question_bank.append(new_question)

question_list= QuizBrain(question_bank)

print("\n")
while question_list.still_has_question():
    question_list.next_question()

print("You've completed the quiz")
print(f"Your final score is: {question_list.score}/{question_list.question_number}")



