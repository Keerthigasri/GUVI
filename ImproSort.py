n=int(input())
if(n<=100000):
  l1=list(map(int,input().split()))
  l2=l1[:n]
print(*sorted(l2))
