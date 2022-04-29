def verticle_sum(M):
    n = len(M)
    m = len(M[0])
    sums = [0]*m
    print(sums)
    for i in range(0, n):
        print(i)
        for j in range(0, m):
            sums[j]+=M[i][j]
            print(sums)
    print(sums)
    return sums


M = [[1,2,3], [4,5,6], [7,8,9], [10,11,12]]

verticle_sum(M)