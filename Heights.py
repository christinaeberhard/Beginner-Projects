student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

# summe = sum(student_heights)
# anzahl = len(student_heights)
# result = round(summe / anzahl)
# print(result)

total_height = 0
for height in student_heights:
    total_height += height

print(total_height)

number_of_students = 0
for number in student_heights:
    number_of_students += 1

print(number_of_students)

result = round(total_height / number_of_students)
print(result)
