import sorts
from random import shuffle
from time import sleep
from itertools import zip_longest
import matplotlib.pyplot as plt

# num_inversions(arr) is the number of inversions
# (pairs of elements in the wrong order)
# in arr
def num_inversions(arr):
	count = 0
	for i in range(len(arr)):
		for j in range(i, len(arr)):
			if arr[i] > arr[j]:
				count += 1
	return count

def run(Sort_class, size):
	arr = [i for i in range(1,size+1)]
	shuffle(arr)
	invs = [num_inversions(arr)]
	s = Sort_class()
	for step in s.sort(arr):
		invs.append(num_inversions(arr))
	return invs

#requirements: array of length n has elements (1, 2, ... n)

if __name__ == '__main__':
	num_iterations = 50
	sorts = [
			 # (sorts.Bubble, "Bubble sort"),
			 (sorts.Comb, "Comb sort"),
			 (sorts.Merge, "Merge sort"),
			 (sorts.Insertion, "Insertion sort"),
			 (sorts.Selection, "Selection sort")
			]
	size = 30

	for (sorter, name) in sorts:
		results = run(Sort_class=sorter, size=size)
		for i in range(num_iterations - 1):
			r = run(Sort_class=sorter, size=size)
			results = [(n+m)/2 for (n,m) in zip_longest(results, r, fillvalue=0)]
		plt.plot(results, label=name)
	# plot each individually
	# for i in range(num_iterations):
	# 	res = run(Sort_class=sorter, size=size)
	# 	plt.plot(res)
	plt.ylim((0, size*(size-1)/2)) # min number of inversions is 0, max is n(n-1)/2
	plt.ylabel("Number of inversions")
	plt.xlabel("Iterations")
	plt.legend()
	plt.show()