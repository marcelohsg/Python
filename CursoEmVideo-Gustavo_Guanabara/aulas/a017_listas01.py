num = [2, 5, 9, 1]
num[2] = 3 # Adiciona o número 3 na posição 2, eliminando seu antecessor.
num.append(7) # Adiciona o número 7 ao final da lista
num.sort(reverse=True) # Organiza a lista de forma descresente
num.insert(2,0) # Adiciona o número 0 a posição 2, realocando os outros números para o lado
num.pop(2) # Apagou o número que tá no index 2.
print(num)
print(f'Essa lista tem {len(num)} elementos.')