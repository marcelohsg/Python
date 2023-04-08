# Um professor quer sotear um dos seus quadros alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
import random
n1 = input('Digite o nome do primeiro aluno: ')
n2 = input('Digite o nome do segundo aluno: ')
n3 = input('Digite o nome do terceiro aluno: ')
n4 = input('Digite o nome do quarto aluno: ')
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista) # Escolhe um item da lista aleatóriamente
print(f'O(A) aluno(a) escolhido(a) foi o(a) {escolhido}')
