# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparecem a letra 'A'
# Em que posição ela aparece a primeira vez 
# Em que posição ela aparece a última vez
frase = input('Digite uma frase: ')
frase = frase.strip().lower()
analise = frase.count('a')
encontrar = frase.find('a')
encontrar2 = frase.rfind('a') 
print(f'A letra "A" aparece {analise} vezes na frase!')
print(f'A primeira letra "A" aparece na posição {encontrar + 1}')
print(f'A ultima letra "A" aparece na posição {encontrar2 + 1}')
