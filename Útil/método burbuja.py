
def bubblesort(lista):
    n = len(lista)
    for i in range(n-1):
        for j in range(i+1,n):
            if lista[i] > lista[j]:
                lista[i],lista[j] = lista[j],lista[i]


ln = [0,3,5,18,6565654,6054,654,654]
bubblesort(ln)
print(ln)
