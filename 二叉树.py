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

    def pos_traversing(self):
        stack1 = [self._head, ]
        stack2 = []
        while stack1:
            cur = stack1.pop()
            stack2.append(cur)
            stack1.append(cur.left) if cur.left else None
            stack1.append(cur.right) if cur.right else None
        while stack2:
            yield stack2.pop().val

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

    def mirrors_traversing(self):
        """
        先序mirrors遍历
        :return:
        """
        cur = self._head
        while cur:
            if self._is_have_left(cur):
                right_node = self._get_the_last_right(cur.left, cur)
                if right_node and right_node.right == cur:
                    # 第二次来到该节点
                    right_node.right = None
                    cur = cur.right
                else:
                    # 第一次来到该节点
                    right_node.right = cur
                    yield cur.val
                    cur = cur.left
            else:
                # 来到了只会走一次的节点，直接打印
                yield cur.val
                cur = cur.right

    def _is_have_left(self, node):
        return node.left is not None

    def _get_the_last_right(self, node, cur):
        tmp = node
        while tmp and tmp.right and tmp.right != cur:
            tmp = tmp.right
        return tmp

    def mirrors_pos_traversing(self):
        cur = self._head
        while cur:
            if self._is_have_left(cur):
                right_node = self._get_the_last_right(cur.left, cur)
                if right_node and right_node.right == cur:
                    # 第二次来到该节点
                    right_node.right = None
                    for val in self._yield_edge(cur.left):
                        yield val
                    cur = cur.right
                else:
                    # 第一次来到该节点
                    right_node.right = cur
                    cur = cur.left
            else:
                # 来到了只会走一次的节点，直接打印
                cur = cur.right
        for val in self._yield_edge(self._head):
            yield val

    def _yield_edge(self, node):
        cur = node
        while cur and cur.right:
            cur = cur.right
        tail = cur
        self._reverse(node)
        while cur:
            yield cur.val
            cur = cur.right
        self._reverse(tail)

    def _reverse(self, node):
        """
        将树节点反转，仅用于mirrors的后序遍历
        :param node:
        :return:
        """
        _from = None
        cur = node
        while cur:
            tmp = cur.right
            cur.right = _from
            _from = cur
            cur = tmp


a = BinarySearchTree([5, 1, 2, 3, 6, 7, 8])
print("============================")
for i in a.mirrors_pos_traversing():
    print(i)
print("============================")
for i in a.pos_traversing():
    print(i)
