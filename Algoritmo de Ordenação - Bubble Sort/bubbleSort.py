# Implementação do Bubble sort

def bubble_sort(v):

	len_v = len(v)

	for i in range(len_v - 1, 0, -1):
		swapped = False
		for j in range(i):
			if v[j] > v[j + 1]:
				v[j], v[j + 1] = v[j + 1], v[j]
				swapped = True
		if not swapped:
			break


v = [10, 40, 5, 15, 30, 70, 20]
bubble_sort(v)
print(v)