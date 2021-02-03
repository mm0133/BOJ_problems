s1=input()
s2=input()


dp=[[0]*(len(s2)+1) for i in range(len(s1)+1)]
for i in range(1,(len(s1)+1)):
    for j in range(1,(len(s2)+1)):
        if s1[i-1]==s2[j-1]:
            dp[i][j]= dp[i-1][j-1] +1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j-1])

col=len(s1)
low=len(s2)
ltem=low
cur=dp[col][low]
print(cur)
s=''

while(cur>0):
    if dp[col][low]==cur and dp[col-1][low]==cur-1 and dp[col][low-1]==cur-1 and dp[col-1][low-1]==cur-1:
        s=s1[col-1]+s
        col=col-1
        low=low-1
        ltem=low
        cur-=1
    else:
        if low == 1:
            low=ltem
            col-=1
        else:
            low -=1
print(s)