class Node:
  def __init__(self, val=0, left=None, right=None):
    self.val, self.left, self.right = val, left, right


def in_order(root):
  stack = []
  curr = root

  while curr or stack:
    while curr:
      stack.append(curr)
      curr = curr.left

    curr = stack.pop()

    print(curr.val)

    curr = curr.right


def post_order(root):
  s1, s2 = [root], []

  while s1:
    curr = s1.pop()

    if not curr:
      continue

    s1.append(curr.left)
    s1.append(curr.right)
    s2.append(curr)

  while s2:
    print(s2.pop().val)


def pre_order(root):
  stack = [root]

  while stack:
    curr = stack.pop()

    if not curr:
      continue

    print(curr.val)

    stack.append(curr.left)
    stack.append(curr.right)


if __name__ == '__main__':
  nodes = {i: Node(i) for i in range(5)}

  #     3
  #    / \
  #   1   4
  #  / \
  # 0   2
  nodes[3].left = nodes[1]
  nodes[3].right = nodes[4]
  nodes[1].left = nodes[0]
  nodes[1].right = nodes[2]

  root = nodes[3]

  print('in order')
  in_order(root)

  print('post_order')
  post_order(root)

  print('pre_order')
  pre_order(root)
