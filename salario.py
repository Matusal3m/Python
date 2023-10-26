print('\n\n\nColoque o valor do salário de cada funcionário para calcular o valor dos abonos. \n****Para encerrar o programa digite "0"****\n')
salario = []
salario.append(None)
a = 1
abono = []
abono.append(None)
abono_total = 0
abono_verificar = 0
while salario[a-1] != 0:
    salario.append(float(input(f'Digite o salário do profissional {a}:\n')))
    abono_verificar = salario[a]*1/5
    if abono_verificar == 0:
        abono_verificar = 0
    elif abono_verificar < 100:
        abono_verificar = 100
    abono.append(abono_verificar)
    abono_total += abono_verificar
    a += 1
    
salario.remove(None)
salario.remove(0)
abono.remove(None)
abono.remove(0)

print(salario, abono)
for i in range (len(salario)):
    print(f'O trabalhador {i+1} com salário R${salario[i]} recebeu abono de valor R${abono[i]}.')
print(f'O total a ser gasto com abonos será de R${abono_total}, houve {a-2} colaboradores e {abono.count(100)} ganharam o valor minimo.')