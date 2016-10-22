from node import node

class Queue:
	def __init__(self):
		self.head = node(-1)
		self.sizeOfQueue = 0
		self.tail = self.head

	def empty(self):
		if self.sizeOfQueue == 0:
			return True
		return False

	def enqueue(self, value):
		self.tail.next = node(value)
		self.tail = self.tail.next
		self.sizeOfQueue = self.sizeOfQueue + 1

	def dequeue(self):
		if self.empty():
			print("error, no item in queue")
		elif self.sizeOfQueue == 1:
			returnValue = self.head.next.value
			self.tail = self.head
			self.sizeOfQueue = 0
			self.head.next = None
			return returnValue
		else:
			returnValue = self.head.next.value
			self.head.next = self.head.next.next
			self.sizeOfQueue = self.sizeOfQueue - 1
			return returnValue


	def printQueue(self):
		tmp = self.head
		line = []
		while tmp.next is not None:
			line.append(tmp.next.value)
			tmp = tmp.next
		print line

def main():
	print "test empty"
	myQueue = Queue()
	print myQueue.empty()
	myQueue.enqueue(1)
	print myQueue.empty()
	myQueue.printQueue()

	print "test enqueue"
	myQueue.enqueue(2)
	myQueue.enqueue(3)
	myQueue.printQueue()

	print "test dequeue"
	myQueue.dequeue()
	myQueue.printQueue()

if __name__ == "__main__":
	main()


