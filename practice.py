je=[0,1,1,2,2,2,2,2,3,4,5]

je.reverse()
print(je)
def find(x):
 l=0
 r=len(je)
 while l < r:
  m = (l + r) // 2
  if je[m] < x:
   r = m
  else:
   l = m + 1
 return l


print(find(2))


def find(x):
 l = 0
 r = K
 while l < r:
  m = (l + r) // 2
  if bp[m] < x:
   r = m
  else:
   l = m + 1
 return l