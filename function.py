def nullify_first_column(x):
    import copy
    y = copy.copy(x)
    for i in range(0,len(y)):
        y[i][0] = 0
    return y

nullify_first_column([[1,2,3],[4,5,6]])

import copy
def nullify_first_column( x ):
  '''x is list of lists of integers, e.g., M=[[1,2,3],[4,5,6]]'''
  y = copy.deepcopy(x)
  for i in range(0, len( y )):
    y[i][0] = 0
    print(x)
    print(y)
  return y

nullify_first_column([[1,2,3],[4,5,6]])

