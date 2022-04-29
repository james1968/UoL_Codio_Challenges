def shortest_atom(s):
    '''implement this function'''
    s_lis = []
    for i in s:
        s_lis.append(i)
    ind = s_lis[1:]
    m = ind.index(s_lis[0]) + 1
    n = s_lis[:m]
    print("".join(n))

shortest_atom("abababab")
