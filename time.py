n=int(input())
h=0
m=0
while(n>=60):
    h=h+1
    m=n-60
    n=n-60
print(h,m)
