import collections
def convert(wcal):
    '''implement this function'''
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    ans = []
    ans_dict = dict()
    for key, values in wcal.items():
        ans.append(values)

    for i in range(0, len(ans)):
        for key, value in ans[i].items():
            if key not in ans_dict:
                ans_dict[key] = {value}
            else:
                ans_dict[key].add(value)

    print(ans_dict)


w1 = {"Thu": 1, "Fri": 2, "Sat": 3, "Sun": 4}
w2 = {"Mon": 5, "Tue": 6, "Wed": 7, "Thu": 8, "Fri": 9, "Sat": 10, "Sun": 11}
w3 = {"Mon": 12, "Tue": 13, "Wed": 14, "Thu": 15, "Fri": 16, "Sat": 17, "Sun": 18}
w4 = {"Mon": 19, "Tue": 20, "Wed": 21, "Thu": 22, "Fri": 23, "Sat": 24, "Sun": 25}
w5 = {"Mon": 26, "Tue": 27, "Wed": 28, "Thu": 29, "Fri": 30}

wcal = ({1:w1, 2:w2, 3:w3, 4:w4, 5:w5})

convert(wcal)