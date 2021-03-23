N=int(input())
k=0
while N!=3:
    N=N//3
    k+=1
cur=['***','* *','***']
def build():
    global cur
    tem1=[cur[i]*3 for i in range(len(cur))]
    tem2=[cur[i]+' '*len(cur[i])+cur[i] for i in range(len(cur))]
    cur=tem1+tem2+tem1
for i in range(k):
    build()
for i in cur:
    print(i)