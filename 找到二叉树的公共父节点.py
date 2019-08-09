def find_node(head, node1, node2):
    if head == node1 or head == node2 or head > max(node1, node2):
        return head
    left = find_node(2*head, node1, node2)
    right = find_node(2*head+1, node1, node2)
    if left in (node1, node2) and right in (node1, node2):
        return head
    if left > max(node1, node2):
        return right
    return left


ret = find_node(1, 10, 4)
print(ret)
