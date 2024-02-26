### Method1.
from collections import deque
def maxDepth(root) :
	max_depth = 0
	if root is None :
		return max_depth
	
	q = deque()
	q.append((root, 1))
	while q :
		cur_node, cur_depth = q.popleft()
		max_depth = cur_depth  # or max(max_depth, cur_depth)
		# binary tree 이므로 left, right만 확인해주면 된다.
		if cur_node.left :
			q.append((cur_node.left, cur_depth+1))
		if cur_node.right :
			q.append((cur_node.right, cur_depth+1))		
	
	return max_depth
maxDepth(root)


### Method2.
def postorder(cur_node) :
	if cur_node is None :
		return
	
	postorder(cur_node.left)
	portorder(cur_node.right)
	print(cur_node.value)

postorder(root)
