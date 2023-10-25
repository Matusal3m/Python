num1 = float(input('Insira um valor:\n'))
num2 = num1 - 1
pr = num1

if num1 < 0:
    num1 = -num1
    num2 = num1 - 1
    
while num2 > 0:
    num1 *= num2
    num2 -= 1
    
if pr < 0:
    print(f'{pr}! é {-num1}')
elif pr > 0:
    print(f'{pr}! é {num1}')
else:
    print('0! é 1')