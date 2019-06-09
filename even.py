a,b=map(int,input().split())
l=[]
for i in range(a+1,b):
  if(i%2==0):
    l.append(i)
for x in l:
  print(x,end=" ")
print()
