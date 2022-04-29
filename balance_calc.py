def balance(init_sum, int_rate, tfl, tax_rate, M):
    '''provide your implementation'''
    s = init_sum
    count = 0

    while count < M:
        interest = s * int_rate / 100
        print(f"interest: {interest}")
        if tfl > s:
            tax = 0
            print(f"tax: {tax}")
        else:
            tax = (s - tfl) * tax_rate / 100
            print(f"tax: {tax}")
        count += 1
        s = s + interest - tax
        print(f"balance: {s}")
        print(s)
    return s

balance(19800, 2, 20000, 1, 2)