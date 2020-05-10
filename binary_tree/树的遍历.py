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