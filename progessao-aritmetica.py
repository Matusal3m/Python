sequencia = []

t1 = int(input('Digite o valor de um termo qualquer em uma PA.\n'))

posicao_primeiro = int(input('Informe a posição deste termo da PA.\n'))

t2 = int(input('Digite o valor de outro termo qualquer da PA.\n'))

posicao_segundo = int(input('Informe a posição deste outro termo.\n'))

if posicao_primeiro > posicao_segundo:
    razao = (t1-t2)/(posicao_primeiro-posicao_segundo)
else:
    razao = (t2-t1)/(posicao_segundo-posicao_primeiro)

primeiro_termo = -(razao*(posicao_primeiro-1) - t1)

print(f'A razão é {int(razao)}')

for i in range (10):
    sequencia.append(primeiro_termo+((i)*razao))

print("E seus 10 primeiros termos são:",sequencia)