size1 = int(input("Digite a quantidade de elementos da lista 1: "))
print("Digite os", size1, "elementos da lista 1:")
lista1 = [int(input()) for _ in range(size1)]

size2 = int(input("Digite a quantidade de elementos da lista 2: "))
print("Digite os", size2, "elementos da lista 2:")
lista2 = [int(input()) for _ in range(size2)]

intercalada = []
for i in range(max(size1, size2)):
    if i < size1:
        intercalada.append(lista1[i])
    if i < size2:
        intercalada.append(lista2[i])
print("Lista intercalada:", " ".join(map(str, intercalada)))