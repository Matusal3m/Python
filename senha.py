senha = input('Digite sua senha.\n')
number = any(char.isdigit() for char in senha)
lower = any(char.islower() for char in senha)
upper = any(char.upper() for char in senha)
while upper==False or lower==False or number == False or len(senha) < 8:
    senha = input('Senha inválida, digite novamente.\n')
    number = any(char.isdigit() for char in senha)
    lower = any(char.islower() for char in senha)
    upper = any(char.isupper() for char in senha)
print('Senha salva!')