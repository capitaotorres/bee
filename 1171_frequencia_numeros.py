def freq():
    x = int(input())
    lista = []
    count = 0
    for i in range(x):
        n = int(input())
        lista.append(n)
        lista.sort(key=int)

    for i in range(x):
        for j in lista:
            if lista[i] == j and j != lista[i-1]:
                if lista.count(j) > 1:
                    print(f"{lista[i]} aparece {lista.count(j)} vez(es)")

        '''for j in lista:
        lista[j] 
        if j == j:
            print(f"{j} aparece {lista.count(j)} vez(es)")
            print(i)'''




'''
    
    print(lista)
    for n in lista:

        print(f"{lista[n]} aparece {lista.count(lista[n]}")

'''


freq()
