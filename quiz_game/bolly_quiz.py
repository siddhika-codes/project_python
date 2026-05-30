# Second mini project - Bollywood Quiz Game
bollywood_details = [
    {
    "question" : "Who is the King of Bollywood?",
    "answer" : "Shah Rukh Khan",
    },
   
    {
    "question" : "Who is the oldest Male Actor in Bollywood?",
    "answer" : "Dharmendra",
    },

    {
    "question" : "Who is the oldest Female Actress in Bollywood?",
    "answer" : "Kamini Kaushal",
    },

    {
    "question" : "Who is the most goodlooking Actress in Bollywood",
    "answer" : "Deepika Padukone",
    },

    {
    "question" : "Who is the Most Handsome Actor in Bollywood?",
    "answer" : "Hrithik Roshan",
    },
]

score_counter = 0
for elements in bollywood_details:
    print(elements["question"])
    user_answer = input("give your answer here :")
    if user_answer == elements["answer"]:
        print("answer is correct!")
        score_counter += 1
    else:
        print("wrong try again")

print("You scored", score_counter, "out of 5")



    
    