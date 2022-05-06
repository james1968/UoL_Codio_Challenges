def delete_every_2nd(s: str, term: str)->str:
    if not term:
        raise ValueError("Value Error Thrown")

    if not s:
        raise ValueError("Value Error Thrown")
    n = 2
    count = 0
    s_arr = []
    print(s)
    for i in s:
        s_arr.append(i)
    for j in range(0, len(s_arr)-2):
        if (s_arr[j] + s_arr[j + 1] == term) and ((s_arr[j + 1] + (s_arr[j + 2]) != term)):
            count += 1
        if (s_arr[j] + s_arr[j + 1] == term) and ((s_arr[j + 1] + (s_arr[j + 2]) != term)) and  (count % 2 == 0):
            s_arr[j] = ""
            s_arr[j + 1] = ""
    print(count)
    ans = "".join(s_arr)
    return ans

    return s

delete_every_2nd("aabcdaaaxyaa11aa2", "aa")