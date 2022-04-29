results = input()
result_lst = results.split()
try:
  students = open("student.txt")
except Exception as e:
  print("There was an error with the file upload:  See error details ", e)

students = []

students_lst = []
for line in students:
  student_line = line.split()
  students_lst.append(student_line)

count_false = 0
ans = dict()
for i in range(0, len(students_lst)):
  count_true = 0
  for j in range(1, len(students_lst[i])):
    if students_lst[i][j] == result_lst[j - 1]:
      count_true += 1
    ans[students_lst[i][0]] = count_true

for key, values in ans.items():
  print(key, values)


