class binaryHeap:
	def __init__(self):
		self.heapList = [0]
		self.sizeOfHeap = 0

	def insert(self, v):
		self.heapList.append(v)
		self.sizeOfHeap += 1
		self.shiftUp(self.sizeOfHeap)

	def shiftUp(self, i):
		while i / 2 > 0:
			if self.heapList[i] > self.heapList[i/2]:
				self.heapList[i], self.heapList[i/2] = self.heapList[i/2], self.heapList[i]
			i = i / 2

	def getMax(self):
		if self.sizeOfHeap == 0:
			return None
		return self.heapList[1]

	def getSize(self):
		return self.sizeOfHeap

	def extractMax(self):
		if self.sizeOfHeap == 0:
			return None
		returnValue = self.heapList[1]
		self.heapList[1] = self.heapList[self.sizeOfHeap]
		self.sizeOfHeap -= 1
		self.shiftDown(1)
		self.heapList = self.heapList[0:self.sizeOfHeap+1]
		return returnValue

	def shiftDown(self, i):
		tmp = i
		while tmp * 2 <= self.sizeOfHeap:
			if self.sizeOfHeap > tmp * 2:
				if self.heapList[tmp*2] > self.heapList[tmp*2+1]:
					if self.heapList[tmp] < self.heapList[tmp*2]:
						self.heapList[tmp], self.heapList[tmp*2] = self.heapList[tmp*2], self.heapList[tmp]
						print("swap ", self.heapList[tmp], self.heapList[tmp*2])
						tmp = tmp * 2
					else:
						return
				else:
					if self.heapList[tmp] < self.heapList[tmp*2+1]:
						self.heapList[tmp], self.heapList[tmp*2+1] = self.heapList[tmp*2+1], self.heapList[tmp]
						print("swap ", self.heapList[tmp], self.heapList[tmp*2 + 1])						
						tmp = tmp*2 + 1
					else:
						return
			else:
				if self.heapList[tmp*2] > self.heapList[tmp]:
					self.heapList[tmp*2], self.heapList[tmp] = self.heapList[tmp], self.heapList[tmp*2]
					print("swap ", self.heapList[tmp], self.heapList[tmp*2])					
					tmp = tmp * 2
				else:
					return

	def heapify(self, l):
		i = len(l) / 2
		self.sizeOfHeap = len(l)
		self.heapList = [0] + l[:]
		while i > 0:
			print i
			self.shiftDown(i)
			i -= 1

	def heapSort(self, l):
		self.heapify(l)
		returnValue = []
		while self.sizeOfHeap > 0:
			returnValue += [self.extractMax()]
		return returnValue[::-1]


def main():
	myList = [1,2,3,4,5]
	myHeap = binaryHeap()
	print myHeap.sizeOfHeap
	print myHeap.heapList
	myHeap.heapify(myList)
	print myHeap.sizeOfHeap
	print myHeap.heapList
	myHeap.insert(8)
	print myHeap.sizeOfHeap
	print myHeap.heapList

	myHeap.extractMax()
	print myHeap.heapList
	myHeap.extractMax()
	print myHeap.heapList	
	myHeap.extractMax()
	print myHeap.heapList
	myHeap.insert(100)
	print myHeap.heapList

	testList = [9, 5, 6, 3, 4, 1]
	myHeap = binaryHeap()
	print myHeap.heapSort(testList)


if __name__ == "__main__":
	main()






