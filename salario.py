print('\n\n\nColoque o valor do salário de cada funcionário para calcular o valoe total a ser pago para eles. \n****Para encerrar o programa digite "0"****\n')
salario = []
salario.insert(0, 1)
a = 1
total = 0
while salario[a-1] != 0:
    salario.insert(a, float(input(f'Digite o salário do profissional {a}:\n')))
    while salario[a] < 0:
        salario.insert(a, float(input('Digite o sálario do profissional com um valor válido:\n')))
    abono = salario[a]*1/5
    if abono == 0:
        abono = 0
    elif abono < 100:
        abono = 100
    total += abono
    a += 1
print(f'O total a ser pago pela empresa será de R${total}.')