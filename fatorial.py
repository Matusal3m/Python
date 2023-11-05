while True:
    while True:
        try:
            numero = int(input('Insira o valor desejado.\n'))
            while numero < 0 or numero >= 16:
                while True:
                    try:
                        numero = int(input('Valor inválido. Digite um número inteiro positivo menor que 16.\n'))
                        break
                    except ValueError:
                        print('Digite um número inteiro positivo menor que 16. Tente novamente.')
                        
            break
        except ValueError:
            print('É necessário que o valor seja um número inteiro positivo menor que 16.')
    
    inicial = numero
    controle = numero - 1
    
    while controle > 0:
        numero *= controle
        controle -= 1
    if numero == 0:
        print('O valor de 0! é 1.')
    else:
        print(f'O resultado de {inicial}! é {numero}')
    parar = input('Digite \'0\' para encerrar o programa, se quiser continuar digite qualquer outra caracter.\n')   
    if parar == '0':
        print('Programa encerrado.')
        break