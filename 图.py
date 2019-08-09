from 并查集 import UnionFindSet
from queue import PriorityQueue
from collections import defaultdict


class Edge(object):
    def __init__(self, weight):
        self.weight = weight
        self.enter = None
        self.out = None

    __eq__ = lambda self, other: self.weight == other.weight
    __lt__ = lambda self, other: self.weight < other.weight
    __gt__ = lambda self, other: self.weight > other.weight
    __str__ = lambda self: f"{str(self.enter)}->{str(self.out)}:{self.weight}"
    __hash__ = lambda self: id(self)


class Node(object):
    def __init__(self, val):
        self.val = val
        self.in_val = 0
        self.out_val = 0
        self.next_nodes = []
        self.edges = []

    def __str__(self):
        return str(self.val)

    __hash__ = lambda self: id(self)


class Graph(object):
    def __init__(self):
        self.nodes = {}
        self.edges = set()

    def kruskal(self):
        q = PriorityQueue()
        for edge in self.edges:
            q.put(edge)
        s = UnionFindSet(self.nodes.values())
        ret = []
        while not q.empty():
            edge = q.get()
            if not s.is_same_set(edge.enter, edge.out):
                s.union(edge.enter, edge.out)
                ret.append(edge)
        return ret

    def create_graph_by_tuple(self, tuple_list):
        """
        将(weight,from,to)形式的边组成的元组列表改为我的类形式的图的函数
        :param tuple_list: 一个以上面形式的边组成的列表
        :return: None
        """
        for tup in tuple_list:
            weight = tup[0]
            _from = tup[1]
            _to = tup[2]
            if self.nodes.get(_from) is None:
                from_node = Node(_from)
                self.nodes[_from] = from_node
            if self.nodes.get(_to) is None:
                to_node = Node(_to)
                self.nodes[_to] = to_node
            self.nodes[_from].next_nodes.append(self.nodes[_to])
            self.nodes[_from].out_val += 1
            self.nodes[_to].in_val += 1
            edge = Edge(weight)
            edge.enter = self.nodes[_from]
            edge.out = self.nodes[_to]
            self.nodes[_from].edges.append(edge)
            self.edges.add(edge)

    def dfs_traversing(self, start):
        """
        图的广度优先遍历。
        :param start: 从start这个结点开始
        :return:
        """
        from collections import deque
        q = deque()
        s = set()
        first = self.nodes.get(start)
        q.appendleft(first)
        s.add(first)
        while q.__len__():
            node = q.pop()
            for n in node.next_nodes:
                if n not in s:
                    s.add(n)
                    q.appendleft(n)
            yield node

    def bfs_traversing(self, start):
        s = set()
        stack = [self.nodes.get(start), ]
        s.add(self.nodes.get(start))
        while stack:
            node = stack.pop()
            for child in node.next_nodes:
                if child not in s:
                    s.add(child)
                    stack.append(child)
            yield node

    def topology(self):
        """
        拓扑排序，类似运筹学中的，紧后工序
        :return:
        """
        ans = []
        s = set()
        for _ in self.nodes.values():
            for node in self.nodes.values():
                if node not in s:
                    if node.in_val == 0:
                        ans.append(node)
                        s.add(node)
                        for child in node.next_nodes:
                            child.in_val -= 1
        return ans

    def prim(self):
        ret = []
        queue = PriorityQueue()
        node_set = set()
        for node in self.nodes.values():
            if node not in node_set:
                node_set.add(node)
                for edge in node.edges:
                    if edge not in ret:
                        queue.put(edge)
                while not queue.empty():
                    edge = queue.get()
                    if edge.enter in node_set and edge.out not in node_set:
                        ret.append(edge)
                        node_set.add(edge.out)
                        for edge in edge.out.edges:
                            queue.put(edge)

        # while not queue.empty():
        #     edge = queue.get()
        #     from_node = edge.enter
        #     to_node = edge.out
        #     if from_node not in node_set or to_node not in node_set:
        #         ret.append(edge)
        return ret

    def dijkstra(self, start):
        node = self.nodes.get(start)
        selected_node = set()
        edge_set = set()
        ret = defaultdict(lambda: float('inf'))
        ret[node] = 0
        selected_node.add(node)
        queue = PriorityQueue()
        for edge in node.edges:
            queue.put(edge)
            edge_set.add(edge)
        while not queue.empty():
            edge = queue.get()
            if ret[edge.enter] + edge.weight < ret[edge.out]:
                ret[edge.out] = ret[edge.enter] + edge.weight
                for e in edge.out.edges:
                    if e not in edge_set:
                        edge_set.add(e)
                        queue.put(e)
        return ret


a = Graph()
# a.create_graph_by_tuple([
#     (1, 'F', 'A'),
#     (1, 'F', 'G'),
#     (1, 'G', 'A'),
#     (1, 'A', 'C'),
# ])
# a.create_graph_by_tuple([
#     (1, 'a', 'b'),
#     (2, 'a', 'c'),
#     (3, 'a', 'd'),
#     (4, 'b', 'c'),
#     (5, 'c', 'e'),
#     (6, 'b', 'e'),
#     (7, 'd', 'e'),
# ])
# print(a)
# for i in a.topology():
#     print(i)
# for node in a.dfs_traversing('a'):
#     print(node.val)

a.create_graph_by_tuple([
    (6, 'a', 'd'),
    (10, 'a', 'c'),
    (1, 'a', 'b'),
    (50, 'd', 'c'),
    (2, 'b', 'c'),
    (50, 'c', 'd'),
    (100, 'b', 'd'),
    (100, 'd', 'b'),
    (2, 'c', 'b'),
])

for i, j in a.dijkstra("a").items():
    print(i, j)
