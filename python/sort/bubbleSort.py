class bubbleSort:
	def __init__(self):
		pass

	def doSort(self, l):
		length = len(l)
		for i in range(length - 1):
			for j in range(length - i - 1):
				if l[j] > l[j+1]:
					l[j], l[j+1] = l[j+1], l[j]
		return l

def main():
	myList = [4,3,5,2,1]
	mySort = bubbleSort()
	print mySort.doSort(myList)

if __name__ == "__main__":
	main()


