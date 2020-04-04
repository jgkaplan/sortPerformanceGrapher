from abc import ABC, abstractmethod

class Sorter(ABC):
	@abstractmethod
	def sort(arr):
		#In place sort of array
		pass

	def swap(self, arr, i, j):
		arr[i], arr[j] = arr[j], arr[i]

	@classmethod
	def __subclasshook__(cls, C):
		if cls is Sorter:
			if any("sort" in B.__dict__ for B in C.__mro__):
				return True
		return NotImplemented


class Bubble(Sorter):
	def sort(self, arr):
		for i in range(len(arr)-1):
			for j in range(len(arr)-1):
				if arr[j] > arr[j+1]:
					self.swap(arr, j, j+1)
					yield

class Comb(Sorter):
	#taken from https://en.wikipedia.org/wiki/Comb_sort
	def sort(self, arr):
		length = len(arr)
		shrink = 1.3
		_gap = length
		sorted = False
		while not sorted:
			# Python has no builtin 'floor' function, so we/I just have one variable (_gap) to be shrunk,
			# and an integer variable (gap) to store the truncation (of the other variable) in and 
			# to use for stuff pertaining to indexing
			_gap /= shrink
			#gap = np.floor(_gap)
			gap = int(_gap)
			if gap <= 1:
				sorted=True
				gap=1
			# equivalent to `i = 0; while (i + gap) < length: ...{loop body}... i += 1`
			for i in range(length - gap):
				sm = gap+i
				if arr[i] > arr[sm]:
					self.swap(arr,i,sm)
					sorted = False
					yield

class Insertion(Sorter):
	def sort(self, arr):
		for i in range(1, len(arr)):
			x = arr[i]
			j = i - 1
			while j >= 0 and arr[j] > x:
				arr[j+1] = arr[j]
				j -= 1
			arr[j+1] = x
			yield

class Selection(Sorter):
	def sort(self, arr):
		for i in range(0,len(arr)-1):
			m = i
			for j in range(i+1,len(arr)):
				if arr[j] < arr[m]:
					m = j
			if m != i:
				self.swap(arr, m,i)
			yield

class Merge(Sorter):
	def merge(self, arr, start, mid, end):
		start2 = mid + 1
		if arr[start2] > arr[mid]:
			return
		while start <= mid and start2 <= end:
			if arr[start2] > arr[start]:
				start += 1
			else:
				value = arr[start2]
				index = start2
				while(index != start):
					arr[index] = arr[index - 1]
					index -= 1
				arr[start] = value
				start += 1
				mid += 1
				start2 += 1

	def mergesort_helper(self, arr, l, r):
		if l < r:
			m = l + (r - l) // 2
			yield from self.mergesort_helper(arr, l, m)
			yield from self.mergesort_helper(arr, m+1, r)
			self.merge(arr, l, m, r)
			yield
			
	def sort(self, arr):
		yield from self.mergesort_helper(arr, 0, len(arr)-1)