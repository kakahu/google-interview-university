class treeNode(object):
	"""docstring for treeNode"""
	def __init__(self, l = None, r = None, v = None):
		super(treeNode, self).__init__()
		self.value = v
		self.left = l
		self.right = r
		