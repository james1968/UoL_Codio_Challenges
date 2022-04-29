def generate_sentences(subjects, predicates, objects):
  '''provide implementation'''
  subjects.sort()
  predicates.sort()
  objects.sort()
  ans = ''

  for i in range(0, len(subjects)):
    for j in range(0, len(predicates)):
      for k in range(0, len(objects)):
        ans += subjects[i] + " " + predicates[j]+ " " + objects[k] + ". "

  print(ans.rstrip())
  return ans.rstrip()

generate_sentences(["John", "Mary"], ["hates", "loves"], ["apples", "bananas"])

"John hates apples. John hates bananas. "\
"John loves apples. John loves bananas. Mary hates apples. "\
"Mary hates bananas. Mary loves apples. Mary loves bananas."