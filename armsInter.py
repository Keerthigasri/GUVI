a,b=map(int,input().split())
l=[]
for i in range(a+1,b):
  n=i
  cub=0
  while(n!=0):
    dig=n%10
    n=n//10
    cub=cub+(dig**3)
  if(cub==i):
    l.append(i)
print(*l)
