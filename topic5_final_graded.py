import math
def print_distances(coordinates, filename):
  '''implement this function'''
  print(coordinates)
  ans = []
  outfile = open(filename, "w")
  for i in range(0, len(coordinates)-1):
    ans.append(math.sqrt(((coordinates[i][0] - coordinates[i+1][0]) ** 2) + ((coordinates[i][1] - coordinates[i+1][1]) ** 2)))
    distance = math.sqrt(((coordinates[i][0] - coordinates[i + 1][0]) ** 2) + ((coordinates[i][1] - coordinates[i + 1][1]) ** 2))
    print(f"{distance:10.2F}")
    str_dist = f"{distance:10.2F}: ({coordinates[i][0]},{coordinates[i][1]})->({coordinates[i+1][0]},{coordinates[i+1][1]})\n"
    outfile.write(str_dist)
  outfile.close()

print_distances([(1,2), (5,8), (10,10), (34,12)], "distances1.txt")