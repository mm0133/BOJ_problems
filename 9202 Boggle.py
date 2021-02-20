class Node:
    def __init__(self,v):
        self.v=v
        self.chil={}
        self.end=0


def build(node, word, x):
    if word[x] in node.chil:
        if x == len(word) - 1:
            node.chil[word[x]].end = 1
            return
        build(node.chil[word[x]], word, x + 1)

    else:
        ch = Node(word[x])
        node.chil[word[x]] = ch
        if x == len(word) - 1:
            ch.end = 1
            return
        build(ch, word, x + 1)

root=Node(None)

w=int(input())
for i in range(w):
    word=input()
    build(root,word,0)

dx=[0,1,1,1,0,-1,-1,-1]
dy=[1,1,0,-1,-1,-1,0,1]

def dfs(node,x,y,word,m):
    if 0<node.end<m:
        global maxword, wordnum, score
        node.end=m
        length=len(word)
        if len(maxword)<length or (len(maxword)==length and word<maxword):
            maxword=word
        wordnum+=1

        if  length<3:
            pass
        elif length<5:
            score+=1
        elif length<6:
            score+=2
        elif length<7:
            score+=3
        elif length<8:
            score+=5
        elif length==8:
            score+=11

    for i in range(8):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<4 and 0<=ny<4 and vi[ny][nx]==0:
            if bo[ny][nx] in node.chil:
                vi[ny][nx]=1
                dfs(node.chil[bo[ny][nx]],nx,ny,word+node.chil[bo[ny][nx]].v,m)
                vi[ny][nx]=0
input()
b=int(input())

for i in range(b):
    bo=[]
    vi=[[0]*4 for _ in range(4)]
    maxword = ''
    score=0
    wordnum=0
    for j in range(4):
        bo.append(input())
    for k in range(4):
        for l in range(4):
            if bo[k][l] in root.chil:
                vi[k][l]=1
                dfs(root.chil[bo[k][l]], l, k,bo[k][l],i+2)
                vi[k][l]=0
    print(score,maxword,wordnum)
    if i<b-1:
        input()
