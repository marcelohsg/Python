#  Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.
from moeda import aumentar, diminuir, dobro, metade, moeda

valor = float(input('Digite um valor: R$'))
print(f'O dobro de {moeda(valor)} é {moeda(dobro(valor))}')
print(f'A metade de {moeda(valor)} é {moeda(metade(valor))}')
print(f'Aumentando em 10%, temos {moeda(aumentar(valor, 10))}')
print(f'Diminuindo em 10%, temos {moeda(diminuir(valor, 10))}')

