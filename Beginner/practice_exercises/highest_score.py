#calculate highest score from a list of scores
#Not allowed to use max or min function

student_scores = input("Input a list of student scores: ").split()
for i in range(0, len(student_scores)):
    student_scores[i] = int(student_scores[i])
print(student_scores)

max_value = 0
for score in student_scores:
    if score > max_value:
        max_value = score
print(f"The highest score is: {max_value}")

