def remove_multiplo(valor, lista): 
    for i in lista:
        if i%valor==0 and i != valor:
            lista.remove(i)
    return lista
numero = int(input('Insira um número: '))
lista = []
n = [2, 3, 5, 7 ,11]

for i in range(2, numero+1):
    lista.append(i)
for i in n:
    lista = remove_multiplo(i, lista)
print(lista)