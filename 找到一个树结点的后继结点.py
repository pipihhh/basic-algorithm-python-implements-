"""
有一棵特殊的二叉树，除了left与node结点之外 还有一个parent结点指向当前结点的父节点。
则让你写一个函数，输入一个树的结点，让你找到这个结点的后继结点
后继结点的意思为，一颗树的中序遍历结果中，该结点的下一个结点则为此结点的后继结点
"""


class Solution(object):
    def find_suc(self, node):
        # 如果节点有右孩子，则后继结点为右孩子的最左节点
        if node.right is not None:
            tmp = node.left
            ret = tmp
            while tmp:
                ret = tmp
                tmp = tmp.left
            return ret
        else:
            # 如果结点为父亲结点的左结点,则直接返回父节点就是答案
            if node.parent.left == node:
                return node.parent

            # 如果节点为父节点的右孩子，则它的后继结点为父亲结点的
            if node.parent.right == node:
                return self._find_suc(node.parent)

    def _find_suc(self, node):
        if node.parent is None:
            return None
        if node.parent.left == node:
            return node.parent
        if node.parent.right == node:
            return self._find_suc(node.parent)
