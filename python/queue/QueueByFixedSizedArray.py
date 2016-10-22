class Queue:
	def __init__(self, l):
		self.line = []
		self.maxLength = l
		self.length = 0

	def empty(self):
		return True if len(self.line) == 0 else False

	def enqueue(self, v):
		if self.length == self.maxLength:
			self.line = self.line[1:] + [v]
		else:
			self.line.append(v)
			self.length += 1

	def dequeue(self):
		if self.empty():
			print "error, no item to dequeue"
		else:
			self.length -= 1
			returnValue = self.line[self.length]
			self.line.pop()
			return returnValue

	def printQueue(self):
		print self.line

	def full(self):
		return True if self.length == self.maxLength else False


def main():
	myQueue = Queue(5)

	print "test empty"
	print myQueue.empty()

	print "test enqueue and empty and full"
	myQueue.enqueue(1)
	myQueue.enqueue(2)
	myQueue.enqueue(3)
	print myQueue.empty()
	print myQueue.full()
	myQueue.printQueue()
	myQueue.enqueue(4)
	myQueue.enqueue(5)
	myQueue.printQueue()
	myQueue.enqueue(6)
	print myQueue.full()
	myQueue.printQueue()

	print "test dequeue"
	print myQueue.dequeue()
	myQueue.printQueue()
	print myQueue.dequeue()
	myQueue.printQueue()
	print myQueue.dequeue()
	myQueue.printQueue()
	print myQueue.dequeue()
	myQueue.printQueue()
	print myQueue.dequeue()
	myQueue.printQueue()
	myQueue.dequeue()


if __name__ == "__main__":
	main()



