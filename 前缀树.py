class TrieNode(object):
    def __init__(self):
        self.passed = 0
        self.end = 0
        self.next_node = {}


class TrieTree(object):
    def __init__(self):
        self._head = TrieNode()

    def add(self, string):
        tmp = self._head
        tmp.passed += 1
        for s in string:
            next_node = tmp.next_node.get(s)
            if next_node is None:
                tmp.next_node[s] = TrieNode()
            tmp = tmp.next_node[s]
            tmp.passed += 1
        tmp.end += 1

    def __contains__(self, string):
        tmp = self._head
        for item in string:
            tmp = tmp.next_node.get(item)
            if tmp is None:
                return False
        return tmp.end != 0

    def remove(self, string):
        if string in self:
            tmp = self._head
            tmp.passed -= 1
            for s in string:
                last = tmp
                tmp = tmp.next_node.get(s)
                tmp.passed -= 1
                if tmp.passed == 0:
                    last.next_node.pop(s)
                    return 1
            tmp.end -= 1
            return 1
        return 0

    def search(self, string):
        tmp = self._head
        for item in string:
            tmp = tmp.next_node.get(item)
            if tmp is None:
                return 0
        return tmp.end

    def prefix_number(self, string):
        tmp = self._head
        for i in range(len(string)):
            tmp = tmp.next_node.get(string[i])
            if tmp is None:
                return 0
        return tmp.passed

    __len__ = lambda self: self._head.passed


a = TrieTree()
a.add("abc")
a.add("abe")
a.add("abkf")
a.remove("abkf")
print(len(a))
