class MyArray:
	"""docstring for array"""
	def __init__(self):
		print("array initiated")
		self.line = []

	def size(self):
		return len(self.line)

	def myPrint(self):
		print self.line

	def is_empty(self):
		return True if len(self.line) == 0 else False

	def at(self, index):
		return self.line[index]

	def push(self, item):
		self.line.append(item)

	def insert(self, index, item):
		newLine = self.line[:index]
		newLine.append(item)
		newLine.extend(self.line[index:])
		self.line = newLine

	def prepend(self, item):
		self.line = [item] + self.line

	def pop(self):
		self.line.pop()

	def delete(self, index):
		self.line = self.line[:index] + self.line[index+1:]

	def remove(self, item):
		for i, v in enumerate(self.line):
			if v == item:
				self.delete(i)
				break

	def find(self, item):
		for i, v in enumerate(self.line):
			if v == item:
				return i
		return -1

def main():
	a = MyArray()
	# test size and is_empty, should return 0 and True
	print a.size()
	print a.is_empty()

	# test push, should return 3, False, [1,2,3]
	a.push(1)
	a.push(2)
	a.push(3)
	print a.size()
	print a.is_empty()
	a.myPrint()

	# test insert, should return [1,4,2,3]
	a.insert(1, 4)
	a.myPrint()

	# test at, should return 4
	print a.at(1)

	# test push, should return [1,4,2,3,5]
	a.push(5)
	a.myPrint()

	# test prepend, should return [0,1,4,2,3,5]
	a.prepend(0)
	a.myPrint()

	# test pop, should return [0,1,4,2,3]
	a.pop()
	a.myPrint()

	# test delete, should return [0,1,2,3]
	a.delete(2)
	a.myPrint()

	# test remove, should return [0,1,3]
	a.remove(2)
	a.myPrint()

	# test find, should return 2
	print a.find(3)

if __name__ == "__main__":
		main()










		