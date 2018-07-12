n,k=int(input()), int(input())
a=[]
s=0
for i in range (0,n):
    a.append(int(input()))
for i in range(0,k):
    s+=a[i]
print(s)
