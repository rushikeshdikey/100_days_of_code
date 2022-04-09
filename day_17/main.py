# start to python day-17 code
# starting code is basics learned
# main project code at end

# Author: Rushikesh Dikey
# Date: 08-03-2022

# # Defining a class
# class Car:
#     def __init__(self, seats):
#         self.seats = seats
#
# # Class called by object
# my_car = Car(5)
#
# print(my_car.seats)
#
# # Defining a class or
#
# class User:
#
#     # class attribute
#     follow = 0
#
#     # Instance attribute
#     def __init__(self, user_id, username):
#         self.id = user_id
#         self.username = username
#         self.followers = 0
#         self.following = 0
#     # method
#     def follow(self, user):
#         user.followers += 1
#         self.following += 1
#
# # Object instantiation
# user_1 = User(1, 'Rushi')
# user_2 = User(2, 'Arpit')
# print(user_1.username)
# print(user_1.id)
#
# # Accessing class methods
# user_1.follow(user_2)
# user_2.follow(user_1)
#
# print(f"Followers of {user_1.username} is {user_1.followers}")
# print(f"{user_1.username} follows {user_1.following}")
#
# print(f"{user_2.username} follows {user_2.following}")
# print(f"Followers of {user_2.username} is {user_2.followers}")

import random

from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
# random_data = random.choice(question_data)
# print(random_data)
# question_bank.append(random_data)
# print(question_bank)
#
# random_data_len = len(question_data)
# # print(r_question_len)

# TO SHUFFLE the questions
random.shuffle(question_data)

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You have completed the quiz")
print(f"Your final score is {quiz.score}/{quiz.question_number}")
if quiz.score > 7:
    print(f"You Passed with {round((quiz.score/quiz.question_number)*100)}%")
else:
    print(f"You Failed with {round((quiz.score/quiz.question_number)*100)}%")
