def test():
	ar = [3, 2, 4, 5]
	ar.pop()

	ar.append(6)

	print(ar)
	print("Index of 4: ", ar.index(4))

	ar.remove(4)
	print("Removed 4: ", ar)

	ar.reverse()
	print("reversed: ", ar)
	print("sorted return: ", sorted(ar))

	ar.sort()
	print("sorted in place: ", ar)





def main():
	test()

if __name__ == "__main__":
	main()
