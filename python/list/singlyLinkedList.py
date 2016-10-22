from node import node
import copy

class LinkedList:
	def __init__(self):
		self.head = node()
		self.sizeOfList = 0
		self.tail = self.head

	def append(self, v):
		self.tail.next = node(v)
		self.tail = self.tail.next
		self.sizeOfList = self.sizeOfList + 1


	def size(self):
		return self.sizeOfList

	def empty(self):
		return True if self.sizeOfList == 0 else False

	def value_at(self, index):
		if self.empty():
			print("error, no such node with index:", index)
			return

		ptr = self.head
		while index >= 0:
			if ptr.next is None:
				print("error, no such node with index:", index)
				return
			ptr = ptr.next
			index = index - 1
		return ptr.value

	def push_front(self, value):
		if self.empty():
			self.tail = node(value)
			self.head.next = self.tail
		else:
			tmp = self.head.next
			self.head.next = node(value, tmp)
		self.sizeOfList = self.sizeOfList + 1

	def pop_front(self):
		if self.empty():
			print("error, no node in list")
		elif self.sizeOfList == 1:
			returnValue = self.head.next.value
			self.head.next = None
			self.tail = self.head
			self.sizeOfList = 0
			return returnValue
		else:
			returnValue = self.head.next.value
			self.head.next = self.head.next.next
			self.sizeOfList = self.sizeOfList - 1
			return returnValue

	def push_back(self, value):
		self.tail.next = node(value)
		self.tail = self.tail.next
		self.sizeOfList = self.sizeOfList + 1


	def pop_back(self):
		if self.empty():
			print("error, no node in list")
		elif self.sizeOfList == 1:
			return self.pop_front()
		else:
			tmp = self.head
			while tmp.next != self.tail:
				tmp = tmp.next
			returnValue = self.tail.value
			tmp.next = None
			self.tail = tmp
			self.sizeOfList = self.sizeOfList - 1
			return returnValue



	def front(self):
		if self.empty():
			print("error, no node in list")
		else:
			return self.head.next.value

	def back(self):
		if self.empty():
			print("error, no node in list")
		else:
			return self.tail.value


	def insert(self, index, value):
		if self.sizeOfList < index:
			print("error, index out of range")
		elif self.sizeOfList == index:
			self.push_back(value)
		else:
			tmp = self.head
			while index > 0:
				tmp = tmp.next
				index = index - 1
			tmp.next = node(value, tmp.next)
			self.sizeOfList = self.sizeOfList + 1

	def earse(self, index):
		if self.sizeOfList <= index:
			print("error, index out of range")
		elif self.sizeOfList - 1 == index:
			self.pop_back()
		else:
			tmp = self.head
			while index > 0:
				tmp = tmp.next
				index = index - 1
			tmp.next = tmp.next.next
			self.sizeOfList = self.sizeOfList - 1



	def value_n_from_end(self, n):
		if n > self.sizeOfList - 1:
			print("error, n out of range")
		else:
			tmp = self.head
			front = self.head
			while n > 0:
				front = front.next
				n = n - 1
			while front != self.tail:
				front = front.next
				tmp = tmp.next
			return tmp.value


	def reverse(self):
		newList = LinkedList()
		values = []
		while not self.empty():
			values.append(self.pop_front())
		values = values[::-1]
		for i in values:
			newList.append(i)
		self.head = newList.head
		self.tail = newList.tail
		self.sizeOfList = newList.sizeOfList

	def remove_value(self, value):
		tmp = self.head
		while tmp.next is not None:
			if tmp.next.value == value:
				if tmp.next.next is None:
					self.pop_back()
				else:
					tmp.next = tmp.next.next
					self.sizeOfList = self.sizeOfList - 1
				print(value, " deleted.")
				return
			else:
				tmp = tmp.next
		print(value, " not found")

	def printList(self):
		tmp = self.head
		line = []
		while tmp.next is not None:
			line.append(tmp.next.value)
			tmp = tmp.next
		print line

def main():
	# test size, empty
	myList = LinkedList()
	print myList.size()
	print myList.empty()

	# test printList, size, empty, push_front

	myList.push_front(3)
	myList.push_front(2)
	myList.push_front(1)
	myList.printList()

	# test value_at
	print myList.value_at(0)
	print myList.value_at(1)
	print myList.value_at(2)

	# test pop_front
	print myList.pop_front()
	myList.printList()
	myList.push_front(1)
	myList.printList()

	# test push_back
	myList.push_back(4)
	print myList.head.next.next.next.value
	print myList.tail.value
	print myList.size()
	myList.printList()

	# test pop_back
	myList.pop_back()
	myList.printList()
	myList.push_back(4)
	myList.printList()

	# test front, back
	print myList.front()
	print myList.back()

	# test insert
	myList.insert(4,5)
	myList.printList()
	myList.insert(7,4.5)
	myList.printList()
	myList.insert(4,3.5)
	myList.printList()

	# test earse
	print("test earse")
	myList.earse(7)
	myList.earse(4)
	myList.printList()

	print("test value_n_from_end")
	print myList.value_n_from_end(0)
	myList.value_n_from_end(7)
	print myList.value_n_from_end(3)

	print("test reverse")
	myList.reverse()
	myList.printList()

	print("test remove_value")
	myList.remove_value(6)
	myList.remove_value(1)
	myList.printList()
	myList.remove_value(3)
	myList.printList()



if __name__ == "__main__":
	main()







