def winner(conf):
  '''implement this function'''
  rows = len(conf)
  cols = len(conf[0])
  countX = 0
  countO = 0

  for i in conf:
    for j in i:
      if j == "X":
        countX += 1
      elif j == "O":
        countO += 1

  if abs(countX - countO) > 1:
    print("-")
    return "-"

  result = ''
  for i in range(0, rows):
        for j in range(0, cols-2):
          if conf[i][j] == conf[i][j+1] and conf[i][j] == conf[i][j+2]:
            result = conf[i][j]
          if conf[j][i] == conf[j+1][i] and conf[j][i] == conf[j+2][i]:
            result = conf[j][i]
          if conf[j][j] == conf[j+1][j+1] and conf[j][j] == conf[j+2][j+2]:
            result = conf[i][i]
  print(result)



#winner((("X", "-", "O"), ("X", "O", "-"), ("X", "-", "O")))
#winner((("O", "-", "X"), ("X", "X", "X"), ("O", "-", "O")))
#winner((("O", "", "X"), ("X", "O", "X"), ("O", "-", "O")))
winner((("O", "", "O"), ("O", "O", "X"), ("O", "-", "O")))