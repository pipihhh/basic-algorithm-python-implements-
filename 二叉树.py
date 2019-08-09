from collections import deque


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)


class BinarySearchTree(object):
    def __init__(self, iterable):
        self._head = None
        self._create_tree(iterable)

    def _create_tree(self, iterable):
        iterable = iter(iterable)
        self._head = Node(iterable.__next__())
        for i in iterable:
            self.insert_val(i)

    def bfs_traversing(self):
        head = self._head
        queue = deque()
        queue.appendleft(head)
        while len(queue):
            node = queue.pop()
            queue.appendleft(node.left) if node.left else None
            queue.appendleft(node.right) if node.right else None
            yield node

    def bfs_serializer(self):
        head = self._head
        ret = ""
        queue = deque()
        queue.appendleft(head)
        while len(queue):
            node = queue.pop()
            if node:
                queue.appendleft(node.left)
                queue.appendleft(node.right)
                ret += str(node.val) + "_"
            else:
                ret += "#_"
        return ret

    def bfs_load(self, string):
        node_list = string.split("_")
        node_list.pop()
        queue = deque()
        head = Node(node_list[0])
        queue.appendleft(head)
        index = 1
        while index < len(node_list):
            node = queue.pop()
            left = node_list[index]
            index += 1
            right = node_list[index]
            index += 1
            if left != "#":
                node.left = Node(int(left))
                queue.appendleft(node.left)
            if right != "#":
                node.right = Node(int(right))
                queue.appendleft(node.right)
        self._head = head

    def insert_val(self, val):
        head = self._head
        pre = None
        while head:
            pre = head
            if val.__gt__(head.val):
                head = head.right
            else:
                head = head.left
        if pre and val.__gt__(pre.val):
            pre.right = Node(val)
        elif pre:
            pre.left = Node(val)
        else:
            return

    def pro_traversing(self):
        stack = [self._head, ]
        while stack:
            node = stack.pop()
            stack.append(node.left) if node.left else None
            stack.append(node.right) if node.right else None
            yield node.val

    def mid_traversing(self):
        stack = [self._head, ]
        is_append = True
        while stack:
            if is_append:
                if stack[-1].left:
                    stack.append(stack[-1].left)
                else:
                    node = stack.pop()
                    if node.right:
                        stack.append(node.right)
                    if node.left is None and node.right is None:
                        is_append = False
                    yield node.val
            else:
                node = stack.pop()
                is_append = True
                if node.right:
                    stack.append(node.right)
                yield node.val

    def recursive_mid(self, head):
        if head is not None:
            self.recursive_mid(head.left)
            print(head.val)
            self.recursive_mid(head.right)

    def _pro_traversing(self):
        pass

    def _recursive_mid(self, head):
        if head is None:
            return "#_"
        left = self._recursive_mid(head.left)
        res = left + str(head.val) + "_"
        right = self._recursive_mid(head.right)
        return res + right

    def mid_serializer(self):
        return self._recursive_mid(self._head)


a = BinarySearchTree([5, 1, 2, 3, 6, 7, 8])
print("============================")
ret = a.bfs_serializer()
print(ret)
a.bfs_load(ret)
print(a.bfs_serializer())
