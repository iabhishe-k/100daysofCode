from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for que in question_data:
    new_question = Question(que["text"], que["answer"])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()


print("You have completed the quiz.")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")
