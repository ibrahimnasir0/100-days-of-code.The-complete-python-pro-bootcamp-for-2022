from operator import ne
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []
# for x in range(12):
#     q1 = data[x]['text']
#     a1 = data[x]['answer']
#     Q ={q1:a1}
#     question_bank.append(Q)
# print(question_bank)

for question in question_data:
    question_text = question['question']
    question_answer = question["correct_answer"]
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)
# print(question_bank[0].answer)


quiz = QuizBrain(question_bank)
while quiz.still_has_question():
  
   quiz.next_question()
print("You have completed the quiz.")
print(f"Your final Score was : {quiz.score} / {quiz.question_no}")