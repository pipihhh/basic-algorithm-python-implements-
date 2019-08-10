class SingleNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class SingleLinkList(object):
    __slots__ = ("_head", "_tail", "_length")
    __len__ = lambda self: self._length

    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0

    def create_link_list_by_iter(self, iterable):
        if not self._head:
            iterable = iter(iterable)
            node = SingleNode(iterable.__next__())
            self._length = 1
            tmp = node
            for i in iterable:
                node.next = SingleNode(i)
                node = node.next
                self._length += 1
            self._tail = node
            self._head = tmp
        else:
            raise Exception("链表已经有节点了")

    def is_empty(self):
        return self._length == 0

    def extends(self, iterable):
        if self.is_empty():
            raise RuntimeError("链表为空")
        iterable = iter(iterable)
        for i in iterable:
            node = SingleNode(i)
            self._tail.next = node
            self._tail = self._tail.next
            self._length += 1

    def _create_if_head_not_exist(self, node):
        if self._head is None:
            self._tail = node
            self._head = node
            return True
        return False

    def right_push(self, val):
        node = SingleNode(val)
        self._length += 1
        if not self._create_if_head_not_exist(node):
            self._tail.next = node
            self._tail = self._tail.next

    def left_push(self, val):
        node = SingleNode(val)
        self._length += 1
        if not self._create_if_head_not_exist(node):
            node.next = self._head
            self._head = node

    def left_pop(self):
        if self._head:
            tmp = self._head
            self._head = self._head.next
            val = tmp.val
            self._length -= 1
            return val
        raise LookupError("链表为空")

    def _traversing(self):
        tmp = self._head
        while tmp:
            yield tmp.val
            tmp = tmp.next

    def __iter__(self):
        return self._traversing()

    def reverse(self):
        cur = self._head
        tmp2 = self._head
        pre = None
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        self._head = pre
        self._tail = tmp2

    def __reversed__(self):
        self.reverse()
        return self

    def sort(self):
        self._sort(self._head, None)

    def _sort(self, head, tail):
        if head != tail:
            pre = self._partition(head, tail)
            self._sort(head, pre)
            self._sort(pre.next, tail)

    def _partition(self, head, tail):
        if head == tail:
            return head
        slow = head.next
        pre = head
        val = head.val
        while True:
            while slow != tail and slow.val < val:
                slow = slow.next
                pre = pre.next
            if slow == tail:
                break
            fast = slow.next
            while fast != tail and fast.val > val:
                fast = fast.next
            if fast == tail:
                break
            slow.val, fast.val = fast.val, slow.val
            pre = slow
            slow = slow.next
        head.val, pre.val = pre.val, head.val
        return pre


if __name__ == '__main__':

    a = SingleLinkList()
    a.create_link_list_by_iter([1, 2, 4, 3, 5, 6])
    a.sort()
    for i in a:
        print(i)
