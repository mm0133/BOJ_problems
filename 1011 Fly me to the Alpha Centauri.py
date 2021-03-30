N=int(input())
for i in range(N):
    a,b=map(int,input().split())
    x=b-a
    sx=int(x**0.5)
    tem=x-sx*sx
    if tem%sx==0:
        ans =2*sx-1+ tem // sx
    else:
        ans=2*sx+tem // sx
    print(ans)


