'''Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável. 
Ex: 
escreva("Olá, Mundo!") Saída:
~~~~~~~~~~~~
Olá, mundo!
~~~~~~~~~~~~
'''
def escreva(txt):
    print('~'*(len(txt)+4))
    print(f'  {txt}')
    print('~'*(len(txt)+4))

texto = str(input('Digite um texto: '))
escreva(texto)
