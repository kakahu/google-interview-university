class selectionSort:
	def __init__(self):
		pass

	def doSort(self, line):
		for i in range(len(line)-1):
			minPos = self.findMinStartFrom(line, i)
			line[i], line[minPos] = line[minPos], line[i]
			print line
		return line

	def findMinStartFrom(self, line, i):
		minValue = line[i]
		minID = i
		for j in range(i+1, len(line)):
			if line[j] < minValue:
				minID = j
				minValue = line[j]
		return minID

def main():
	line = [0,4,5,6,3,5,2]
	mySort = selectionSort()
	mySort.doSort(line)
	print line



if __name__ == "__main__":
	main() 
