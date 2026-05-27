students_list = [
   {"name" : "Apoorva" , "score" : 92},
    {"name" : "Vinita" , "score" : 98},
    {"name" : "Vidit" , "score" : 87},
    {"name" : "Rashi" , "score" : 94},
]

name_student = input("Enter your name :")
student_score = int(input("Enter your score :"))
students_list.append({"name" : name_student, "score" : student_score})

for students in students_list:
    score = students["score"]
    if(score >= 90):
        grade = "A"
    elif(score >= 75):
        grade = "B"
    elif(score >= 60):
        grade = "C"
    else:
        grade = "F"
        
    print(students["name"], "scored", students["score"], "→ Grade:", grade)

toppers_name = students_list[0]["name"]
toppers_score = students_list[0]["score"]

for students in students_list:
    if students["score"] > toppers_score:
     toppers_name = students["name"]
     toppers_score = students["score"]

print("Topper:" , toppers_name, "with",  toppers_score )





    
    
    
    

