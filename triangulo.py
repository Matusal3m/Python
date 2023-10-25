h = int(input("Escolha a altura da escada:\n"))
print(' '*(h+1) + '*')
for i in range (h):
    print((h-i)*' ' + '*'*(i+2) +'*'*(i+1))