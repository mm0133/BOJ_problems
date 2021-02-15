import sys
sys.setrecursionlimit(10001)
li = []
while True:
    try:
        A = int(sys.stdin.readline())
        li.append(A)
    except:
        break


class Node:
    def __init__(self, v):
        self.v = v
        self.r = None
        self.l = None


def construct(node, X):
    if len(X) == 1:
        return
    r = -1
    for i in range(len(X)):
        if X[0] < X[i]:
            r = i
            break
    if r != -1:

        R = X[i:]
        L = X[1:i]
    else:
        R = []
        L = X[1:]
    if R:
        rc = Node(R[0])
        node.r = rc
        construct(rc, R)
    if L:
        lc = Node(L[0])
        node.l = lc
        construct(lc, L)


def print_tree(node):
    if node.l:
        print_tree(node.l)
    if node.r:
        print_tree(node.r)
    print(node.v)

root = Node(li[0])
construct(root, li)
print_tree(root)
