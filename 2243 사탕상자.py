#segment tree
#실행시간 줄이는법, 클래스 말고 list로 구현해보기,
#이 때 tree 를 2^n꼴로 설정해놓으면 모든리프가 전부 같은 높이에 있어서 구현하기 쉬워짐 (메모리조금 낭비)
#segment tree 의 노드 갯수 => 데이터의 갯수 *2 보다 큰 2^n중 가장 작은것으로 설정


import sys

N = int(sys.stdin.readline())


class Node:
    def __init__(self, s, e, v):
        self.start = s
        self.end = e
        self.val = v
        self.r = None
        self.l = None


root = Node(1, 1000000, 0)


def go(node):
    if node.start == node.end:
        return
    else:
        ln = Node(node.start, (node.start + node.end) // 2, 0)
        node.l = ln
        go(ln)
        rn = Node((node.start + node.end) // 2 + 1, node.end, 0)
        node.r = rn
        go(rn)


go(root)


def find(node, k):
    node.val -= 1
    if node.start == node.end:
        return node.start
    else:
        if k <= node.l.val:
            return find(node.l, k)
        else:
            return find(node.r, k - node.l.val)


def update(node, B, C):
    node.val += C
    if node.start == node.end:
        return
    if B <= (node.start + node.end) // 2:
        update(node.l, B, C)
    else:
        update(node.r, B, C)


for i in range(N):
    l = list(map(int, sys.stdin.readline().split()))
    if l[0] == 1:
        print(find(root, l[1]))
    else:
        update(root, l[1], l[2])
