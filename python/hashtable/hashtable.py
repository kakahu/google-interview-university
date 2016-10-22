import string
import random
import scipy
import matplotlib.pyplot as plt

class hashTable():
	def __init__(self, ins):
		self.input = ins
		self.input_count = len(self.input)
		self.middle = int(self.input_count / 2)
		self.prime = self.first_prime_greater_than(self.input_count)
		self.buckets = [0] * self.middle

	def hashProcess(self):
		for w in self.input:
			hash = self.polyhash_prime(w, 31, self.prime, self.middle)
			self.buckets[hash] += 1

	def is_prime(self, n):
		d_max = scipy.sqrt(n)

		if n == 2:
			return True
		if n % 2 == 0:
			return False

		d = 3
		while n % d != 0 and d < d_max:
			d += 2
		return d > d_max


	def first_prime_greater_than(self, min):
		for n in scipy.arange(min + 1, min * 2):
			if self.is_prime(n):
				return n
		return None


	def polyhash_prime(self, word, a, p, m):
		hash = 0
		for c in word:
			hash = (hash * a + ord(c)) % p
		return abs(hash % m)


	def show_distribution(self):
		counts = {}
		for v in self.buckets:
			if v in counts.keys():
				counts[v] += 1
			else:
				counts[v] = 1

		plt.bar(counts.keys(), counts.values())
		plt.title("hash with prime")
		plt.xlabel("Bucket size")
		plt.ylabel("Buckets")
		plt.show()




def load_words():
	words = {}
	exclude = set(string.punctuation + "\n")
	word_count = 0

	with open("tale-of-two-cities.txt", "r") as content:
		for line in content:
			line = line.replace("--", ' ')
			line_words = line.split(" ")
			for word in line_words:
				word = ''.join(ch for ch in word if ch not in exclude)
				if word:
					word = word.lower()
					word_count += 1
					if word in words:
						words[word] += 1
					else:
						words[word] = 1
	return words


def main():
	words = load_words()
	ht = hashTable(words)
	ht.hashProcess()
	ht.show_distribution()



if __name__ == "__main__":
	main()


























