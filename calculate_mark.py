def calculate_mark(s):
  '''implement this function'''
  s_list = s.split(" ")

  try:
    int(s_list[0])
  except Exception as e:
    raise SyntaxError
  mark = int(s_list[1]) - int(s_list[2])
  try:
    mark > 0
  except Exception as e:
    raise ValueError

  mark_st = str(mark)
  student = s_list[0]

  print(f"{student} {mark_st}")
  return f"{student} {mark_st}"


#calculate_mark("123 78 50")
calculate_mark("john xx 30")
#calculate_mark("123 35 50")