results = open('students')
students = []
results_dict = dict()
for line in results:
  results = line.split()
  results_dict[results[1]] = results[0]

results_dict = dict(sorted(results_dict.items(), key=lambda item: item[0]))
print(results_dict)

while True:
  student = input()
  if student == "END":
    break
  if student in results_dict.values():
    keys = [k for k, v in results_dict.items() if v == student]
    print(" ".join(keys))
  else:
    print("Not Known")