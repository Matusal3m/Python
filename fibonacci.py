n = int(input('Digite o n-ésimo termo da sequência de Fibonacci: '))
sequencia = [0, 1]
for i in range(n-1):
    sequencia.append(sequencia[i] + sequencia[i+1])
sequencia.remove(0)
print(sequencia)