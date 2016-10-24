class insertionSort:
	def __init__(self):
		pass

	def doSort(self, l):
		length = len(l)
		for i in range(length):
			for j in range(i):
				if l[j] <= l[i]:
					pass
				else:
					tmp = l[i]
					l[j+1:i+1] = l[j:i] 
					l[j] = tmp
		return l

def main():
	myList = []
	mySort = insertionSort()
	print mySort.doSort(myList)


if __name__ == "__main__":
	main()

