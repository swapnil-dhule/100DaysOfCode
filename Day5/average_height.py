# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
count = 0
sum_of_height = 0

for i in student_heights:
    sum_of_height += i
    count += 1

avg_height = sum_of_height/count

# print(int(avg_height)) ----- This doesn't work always as it just drop everything after decimal point
print(round(avg_height))
