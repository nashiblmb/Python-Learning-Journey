#exercise to calculate average height without using len() or sum()
student_heights = input("Input a list of student heights: ").split()

x = 0
total = 0
for i in range (0, len(student_heights)):
    student_heights[i] = int(student_heights[i])
print(student_heights)

for height in student_heights:
    x += 1
    total += height

average = round(total / x)
print(average)