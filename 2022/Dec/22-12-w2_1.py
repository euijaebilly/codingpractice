'''
BST의 범위 합

이진 탐색 트리의 root 노드와 두 정수 low과 high가 주어지면 포함 범위 [low, high]에 있는 값을 가진 모든 노드의 값 합계를 반환합니다.
'''
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def to_binary_tree(items):
    n = len(items)
    if n == 0:
        return None

    def insert_node(i):
        if n <= i or items[i] is None:
            return None

        node = TreeNode(items[i])
        node.left = insert_node(2 * i + 1)
        node.right = insert_node(2 * i + 2)
        return node

    return insert_node(0)

def rangeSumBST(root, low, high):
    res = []

    def traversal(node):
        if node is None:
            return

        if low <= node.val <= high:
            res.append(node.val)
        if low < node.val:
            traversal(node.left)
        if node.val < high:
            traversal(node.right)

    traversal(root)

    return sum(res)


if __name__ == '__main__':
    root =  [10, 5, 15, 3, 7, 13, 18, 1, None, 6]
    low = 6
    high = 10
    root = to_binary_tree(root)
    print(rangeSumBST(root, low, high))