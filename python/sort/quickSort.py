class quickSort():
	"""docstring for quickSort"""
	def __init__(self):
		pass

	def doSort(self, line):
		if len(line) <= 1:
			return line
		else:
			p = line[0]
			smaller = [x for x in line[1:] if x < p]
			bigger = [x for x in line[1:] if x > p]
		return self.doSort(smaller) + [p] + self.doSort(bigger)

def main():
	line = [9,3,4,5]
	mySort = quickSort()
	print mySort.doSort(line)
	l = line
	q_sort = lambda l: l if len(l)<=1 else q_sort([x for x in l[1:] if x<l[0]])+[l[0]]+q_sort([x for x in l[1:] if x>=l[0]])
	print q_sort(l)

if __name__ == "__main__":
	main()
		