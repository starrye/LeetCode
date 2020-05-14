# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 递归 不推荐使用
def front_digui(self, root):
    """利用递归实现树的先序遍历"""
    if root == None:
        return
    print(root.elem)
    self.front_digui(root.lchild)
    self.front_digui(root.rchild)


def middle_digui(self, root):
    """利用递归实现树的中序遍历"""
    if root == None:
        return
    self.middle_digui(root.lchild)
    print(root.elem)
    self.middle_digui(root.rchild)


def later_digui(self, root):
    """利用递归实现树的后序遍历"""
    if root == None:
        return
    self.later_digui(root.lchild)
    self.later_digui(root.rchild)
    print(root.elem)


def level_queue(self, root):
    """利用双端队列实现树的层级遍历"""
    from collections import deque
    queue = deque()
    queue.append(root)
    while queue:
        current_level_num = queue.popleft()
        print(current_level_num.elem)
        if current_level_num.left is not None:
            queue.append(current_level_num.left)
        if current_level_num.right is not None:
            queue.append(current_level_num.right)


# 迭代 推荐！！
def front_diedai(self, root: TreeNode):
    stack, res = [root], []
    while stack:
        i = stack.pop()
        if isinstance(i, TreeNode):
            stack.extend([i.right, i.left, i.val])
        elif isinstance(i, int):
            res.append(i)
    return res

def middle_diedai(self, root: TreeNode):
    stack, res = [root], []
    while stack:
        i = stack.pop()
        if isinstance(i, TreeNode):
            stack.extend([i.right, i.val, i.left])
        elif isinstance(i, int):
            res.append(i)
    return res

def later_diedai(self, root: TreeNode):
    stack, res = [root], []
    while stack:
        i = stack.pop()
        if isinstance(i, TreeNode):
            stack.extend([i.val,i.right,i.left])
        elif isinstance(i, int):
            res.append(i)
    return res

def leve_diedai(self, root: TreeNode):
    queue, rst = [root], []
    while queue:
        i = queue.pop(0)
        if isinstance(i, TreeNode):
            queue.extend([i.val, i.left, i.right])
        elif isinstance(i, int):
            rst.append(i)
    return rst