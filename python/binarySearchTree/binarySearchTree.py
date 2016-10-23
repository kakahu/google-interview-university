from treeNode import treeNode

class binarySearchTree:
	"""docstring for binarySearchTree"""
	def __init__(self, rootNode = None):
		self.root = rootNode
		self.numOfNodes = 1 if rootNode else 0

	def insert(self, v):
		if self.root is not None:
			self.insertHelper(self.root, v)
		else:
			self.root = treeNode(None, None, v)
			print("insert as root with value ", v)
			self.numOfNodes = 1

	def insertHelper(self, node, v):
		if v == node.value:
			print "value already exists"
			return
		elif v < node.value and node.left is None:
			node.left = treeNode(None, None, v)
			print("insert", v, " as the left child of ", node.value)
			self.numOfNodes += 1
		elif v < node.value and node.left is not None:
			self.insertHelper(node.left, v)
		elif v > node.value and node.right is None:
			node.right = treeNode(None, None, v)
			print("insert", v, " as the right chlid of ", node.value)
			self.numOfNodes += 1
		else:
			self.insertHelper(node.right, v)


	def getNodeCount(self):
		return self.numOfNodes

	def printValues(self):
		print self.inorder(self.root)

	def inorder(self, node):
		if node is None:
			return []
		else:
			return self.inorder(node.left) + [node.value] + self.inorder(node.right)

	def deleteTree(self):
		self.root = None
		self.numOfNodes = 0

	def isInTree(self, v):
		line = self.inorder(self.root)
		return True if v in line else False

	def getHeight(self):
		return self.getHeightHelper(self.root, 0)

	def getHeightHelper(self, node, level):
	  	if not node:
	  		return level
	  	else:
	  		l = self.getHeightHelper(node.left, level + 1)
	  		r = self.getHeightHelper(node.right, level + 1)
	  		return max(l, r)   

	def getmin(self):
		if self.root is None:
			return None
		tmp = self.root
		while tmp.left != None:
			tmp = tmp.left
		return tmp.value

	def getmax(self):
		if self.root is None:
			return None
		tmp = self.root
		while tmp.right != None:
			tmp = tmp.right
		return tmp.value
	def getSuccessor(self, v):
		line = self.inorder(self.root)
		for (i, value) in enumerate(line):
			if value == v and i != len(line) - 1:
				return line[i+1] 
		return None

def main():
	print "test insert, getNodeCount, print_values"
	tree = binarySearchTree()
	print tree.numOfNodes
	tree.insert(2)
	tree.insert(1)
	tree.insert(3)
	print tree.getNodeCount()
	tree.printValues()

	print "test deleteTree"
	tree.deleteTree()
	print tree.numOfNodes
	tree.printValues()

	print "test isInTree"
	tree.insert(2)
	tree.insert(1)
	tree.insert(3)
	tree.insert(5)
	print tree.isInTree(1)
	print tree.isInTree(5)
	print tree.isInTree(7)

	print "test get height"
	print tree.getHeight()
	tree.insert(6)
	print tree.getHeight()

	print "test get min and max"
	print tree.getmin()
	tree.insert(-1)
	print tree.getmin()
	print tree.getmax()

	print "test get successor"
	print tree.getSuccessor(1)
	print tree.getSuccessor(6)
	print tree.getSuccessor(5)
	print tree.getSuccessor(4.5)
	



if __name__ == "__main__":
	main()








