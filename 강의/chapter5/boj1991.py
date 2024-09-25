import sys
input = sys.stdin.readline

class Node():
  def __init__(self, item, left, right):
    self.item = item
    self.left = left
    self.right = right

def preorder(node):
  print(node.item, end = '')
  if node.left != '.':
    preorder(tree[node.left])

N = int(input())
my_tree = []





