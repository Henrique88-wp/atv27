# Solicite ao usuário que insira o nome de até 7 convidados.
# Armazene os nomes em uma lista.
# Permita ao usuário remover um convidado da lista, caso necessário.
# Exiba a lista final de convidados.

# Digite o nome do convidado 1: João
# Digite o nome do convidado 2: Maria
# ...
# Digite o nome do convidado 7: Pedro
# Deseja remover algum convidado da lista? (sim/não): sim
# Digite o nome do convidado a ser removido: Maria


lista = []
for i in range(1,8):
    a = input(f"coloque o nome do convidado {i}:")
    lista.append(a)
b = input("você deseja tirar alguém sim/não?")
if b=="sim":
    c = input("Qual das pessoas você quer tirar?")
    lista.remove(c)
    print(lista)
else:
    print("blz patrão")