import random
original_list = [random.randint(-100, 100) for _ in range(20)]

sorted_list = sorted(original_list)

max_index = original_list.index(max(original_list))
min_index = original_list.index(min(original_list))

print("Lista ordenada:", sorted_list)
print("Lista original:", original_list)
print("Índice do maior valor:", max_index)
print("Índice do menor valor:", min_index)