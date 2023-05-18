# ALTERANDO A VARIÁVEL GLOBAL ATRAVES DA VARIAVEL LOCAL.
def teste(b):
    global a # Faz a variável global adotar o valor de "a" local.
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')



a = 5
teste(a)
print(f'A fora vale {a}')
          