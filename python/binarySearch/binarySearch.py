class binarySearch:
	def __init__(self):
		self.line = []
		self.value = None

	def input(self, nums, v):
		self.line = sorted(nums)
		self.value = v

	def search(self):
		l, r = 0, len(self.line) - 1
		while r - l > 0:
			mid = int((l + r) / 2) + 1
			if self.value == self.line[mid]: 
				return True
			elif self.line[mid] < self.value:
				l = mid + 1
			else:
				r = mid - 1
		if r == l:
			return self.value == self.line[r]
		return False

	def searchByRecursion(self):
		return self.searchByRecursionHelper(0, len(self.line) - 1)

	def searchByRecursionHelper(self, l, r):
		mid =  int((l + r)/2) + 1
		if l == r:
			return self.value == self.line[l]
		elif l > r:
			return False
		else:
			if self.line[mid] == self.value:
				return True
			elif self.line[mid] < self.value:
				return self.searchByRecursionHelper(mid + 1, r)
			else:
				return self.searchByRecursionHelper(l, mid - 1)




def main():
	nums = [2, 3, 4, 5, 534, 346, 74, 6, 34, 54, 45778, 345, 67345, 7]
	print nums
	searchEngine = binarySearch()
	v = 67345
	searchEngine.input(nums, v)
	print searchEngine.search()
	print searchEngine.searchByRecursion()

if __name__ == "__main__":
	main()