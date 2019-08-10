class DoublyLinkNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prefix = None


class DoublyLinkList(object):
    __slots__ = ("_head", "_tail", "_length")
    __len__ = lambda self: self._length

    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0

    def is_empty(self):
        return self._length == 0

    def create_link_list_by_iter(self, iterable):
        if not self._head:
            iterable = iter(iterable)
            head = DoublyLinkNode(iterable.__next__())
            self._length = 1
            tmp = head
            for i in iterable:
                new_node = DoublyLinkNode(i)
                new_node.prefix = tmp
                tmp.next = new_node
                tmp = tmp.next
                self._length += 1
            self._head = head
            self._tail = tmp

    def left_push(self, val):
        new_node = DoublyLinkNode(val)
        if self.is_empty():
            self._head = new_node
            self._tail = new_node
        else:
            new_node.next = self._head
            self._head.prefix = new_node
            self._head = new_node
        self._length = 1

    def right_push(self, val):
        new_node = DoublyLinkNode(val)
        if self.is_empty():
            self._head = new_node
            self._tail = new_node
        else:
            new_node.prefix = self._tail
            self._tail.next = new_node
            self._tail = new_node
        self._length = 1

    def left_pop(self):
        if self.is_empty():
            raise Exception("链表为空")
        tmp = self._head
        self._head = self._head.next
        self._head.prefix = None
        val = tmp.val
        del tmp
        return val

    def right_pop(self):
        if self.is_empty():
            raise Exception("链表为空")
        tmp = self._tail
        self._tail = self._tail.prefix
        self._tail.next = None
        val = tmp.val
        del tmp
        return val

    def reverse(self):
        tail = self._head
        cur = self._head
        while cur:
            tmp1 = cur.next
            tmp2 = cur.prefix
            cur.prefix = cur.next
            cur.next = tmp2
            cur = tmp1
        self._head = tmp2.prefix
        self._tail = tail

    def __iter__(self):
        tmp = self._head
        while tmp:
            yield tmp.val
            tmp = tmp.next


if __name__ == '__main__':
    link = DoublyLinkList()
    link.create_link_list_by_iter([1, 2])
    for l in link:
        print(l)
    link.reverse()
    print(link)
