def retorna_abono(abono_verificar):
    if abono_verificar == 0:
        abono_verificar = 0
    elif abono_verificar < 100:
        abono_verificar = 100
    return abono_verificar

def verifica_salario(a):
    while True:
        try:
            salario_verificado = float(input(f'Digite o salário do profissional {a} ou digite "0" para encerrar o programa:\n' ))
            while salario_verificado < 0:
                print('\nO valor digitado deve ser positivo. Tente Novamente.')
                salario_verificado = float(input(f'Digite o salário do profissional {a} ou digite "0" para encerrar o programa:\n' ))
            break
        except ValueError:
            print('\nO valor inserido foi inválido, digite apenas números positivos. Tente novamente.')
    return salario_verificado

print('\nColoque o valor do salário de cada funcionário para calcular o valor dos abonos, quantidade de colaboradores, seus salários, respectivos abonos, maior abono e qual o valor do maior abono.\n')

salario = []
abono = []
salario.append(None)
abono.append(None)
a = 1
abono_total = 0

while salario[a-1] != 0:
    salario.append(verifica_salario(a))
    abono.append(retorna_abono(salario[a]*1/5))
    abono_total += retorna_abono(salario[a]*1/5)
    a += 1

salario.remove(None)
salario.remove(0)
abono.remove(None)
abono.remove(0)

for i in range (len(salario)):
    print(f'O trabalhador {i+1} com salário R${salario[i]} recebeu abono de valor R${abono[i]}.')
print(f'O total a ser gasto com abonos será de R${abono_total}, houve {a-2} colaboradores, {abono.count(100)} ganharam o valor minimo e o maior abono foi de R${max(abono)}.')