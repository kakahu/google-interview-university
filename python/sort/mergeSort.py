class mergeSort():
	"""docstring for mergeSort"""
	def __init__(self):
		pass
	def doSort(self, h1, h2):
		h1 = sorted(h1)
		h2 = sorted(h2)
		len1 = len(h1)
		len2 = len(h2)
		i,j = 0,0
		returnValue = []
		while i < len1 and j < len2:
			if h1[i] < h2[j]:
				returnValue.append(h1[i])
				i += 1
			else:
				returnValue.append(h2[j])
				j += 1
		if i == len1:
			returnValue.extend(h2[j:len2])
		else:
			returnValue.extend(h1[i:len1])
		return returnValue


def main():
	myList1 = []
	myList2 = [0,3,5,6,8]
	mySort = mergeSort()
	print mySort.doSort(myList1, myList2)

if __name__ == "__main__":
	main()
		