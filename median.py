n=int(input())
l1=list(map(int,input().split()))
l2=sorted(l1[:n])
print(l2[n//2])
