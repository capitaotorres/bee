def vetor():
    x = int(input())
    if x <= 50:
        for i in range(10):
            if i == 0:
                print(f"N[{i}] = {x}")
            else:
                print(f"N[{i}] = {x}")
            x = x * 2


vetor()