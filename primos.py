def remove_multiplo(valor, lista): 
    for i in lista:
        if i%valor==0 and i != valor:
            lista.remove(i)
    return lista
numero = int(input('Insira um número: '))
lista = []
for i in range(2, numero+1):
    lista.append(i)
for i in [2, 3, 5, 7 ,11]:
    lista = remove_multiplo(i, lista)
print(lista)