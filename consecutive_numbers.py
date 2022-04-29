def shortest_continuous_segment(s):
    '''implement the function'''
    ans = {}
    count = 1
    for i in range(0, len(s) - 1):
        if s[i] == s[i+1]:
            count += 1
            n = i
        elif s[i] != s[i+1]:
            ans[n] = count
            count = 1
    ans[n] = count

    print(ans)

    temp = min(ans.values())
    print(temp)
    res = [key for key in ans if ans[key] == temp]
    print(res)
    for i in res:
        print((s[i], temp))

shortest_continuous_segment([1,1,2,2,2,1,1,1])
shortest_continuous_segment([5,5,5,3,3,3,2,2])