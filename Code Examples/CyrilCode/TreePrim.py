# CMPT 145: Binary trees
# TreePrim.py
# Defines primitive BST tree class
# builtu using tree nodes arranged in an ordered structurece to another treenode or None

import TreeNode as Tn

class TreePrim(object):
	''' implements a primitive Binary Search Tree
	on top of a TreeNode Class'''
	
	def __init__(self):
		self.root = None
		self.size = 0
	
	def ordInsert(self,value):
		''' perform BST ordered insert'''

		def TreeNodeInsert(tnode,value):
			''' perform ordered insert recursively on TreeNode structure'''
			if tnode._data <= value:
				# insert right
				if tnode._right is None:
					tnode._right = Tn.TreeNode(value)
				else:
					TreeNodeInsert(tnode._right,value)
			else:
				# insert left
				if tnode._left is None:
					tnode._left = Tn.TreeNode(value)
				else:
					TreeNodeInsert(tnode._left,value)
			return

		if (self.root == None): 
			self.root = Tn.TreeNode(value)
			self.size += 1
		elif (self.root._data > value):
			if (self.root._left is None):
				self.root._left = Tn.TreeNode(value)
			else:
				TreeNodeInsert(self.root._left,value)
		else:
			if (self.root._right is None):
				self.root._right = Tn.TreeNode(value)
			else:
				TreeNodeInsert(self.root._right,value)

	def traverseInorder(self):
		''' perform tree inorder traversal'''

		def TreeNodeTraverseInorder(tnode):
			''' perform inorder recursive traversal on TreeNode structure'''
			if tnode is None: return
			TreeNodeTraverseInorder(tnode._left)
			print (tnode._data)   # output the data
			TreeNodeTraverseInorder(tnode._right)
			return
		
		TreeNodeTraverseInorder(self.root) 
		return

	def is_member(self,value):
		''' perform a BST search for value in tree. '''

		def TreeNodeBinSearch(tnode,value):
			if tnode is None: return (False)
			if (tnode._data == value): return (True)
			if (tnode._data < value):
				return (TreeNodeBinSearch(tnode._right,value))
			return (TreeNodeBinSearch(tnode._left,value))
		
		return (TreeNodeBinSearch(self.root,value))
		
	def treeBSTdelete(self,value):
		'''Perform a BST inorder delete maintaining the BST property '''

		def TreeNodeInorderDelete(tnode,value):
			if (tnode is None): 
				return (tnode)   # value to be deleted did not exist
			if tnode._data == value:
				# return opposite treenode ref if one ref is None
				if (tnode._left is None): return (tnode._right)
				if (tnode._right is None): return (tnode._left)
				# step one: insert my right Treenode subtree into my left
				tmpNode = tnode._left
				while (tmpNode._right is not None):
					tmpNode = tmpNode._right
				tmpNode._right = tnode._right
				# step two: return my left subtree node as root value for where I was in tree
				return (tnode._left)
			if tnode._data < value:
				tnode._right = TreeNodeInorderDelete(tnode._right,value)
			else:
				tnode._left = TreeNodeInorderDelete(tnode._left,value)
			return (tnode)

		# pass problem to TreeNode structure
		self.root = TreeNodeInorderDelete(self.root,value)
		



