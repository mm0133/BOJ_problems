
N=int(input())
cur=['***','* *','***']
def build():
    global cur
    tem1=[cur[i]*3 for i in range(len(cur))]
    tem2=[cur[i]+' '*len(cur[i])+cur[i] for i in range(len(cur))]
    cur=tem1+tem2+tem1
while N!=3:
    N = N / 3
    build()
print('\n'.join(cur))
#프린트 문을 반복하는것보다 문자열을 하나로 합쳐 한번 프린트하는 것이 빠르다
# for i in cur:
#     print(i)