# coding:utf-8

from collections import deque


class TreeNode(object):
	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None

	def __repr__(self):
		return '%s (%s %s)' % (self.val, self.left or '', self.right or '')


def constructTreeFromList(nodes):
	print nodes
	if not nodes:
		return 
	root = TreeNode(nodes[0])
	cur = root
	childs = deque()
	for i, val in enumerate(nodes[1:]):

		if not i % 2:
			cur.left = val if val is None else TreeNode(val)
			childs.append(cur.left)
		else:
			cur.right = val if val is None else TreeNode(val)
			childs.append(cur.right)
		if i % 2:
			cur = childs.popleft()

	return root

print(constructTreeFromList([1,2,3,4,5,None,6, None, None, None, None, 7,8, None, None]))
