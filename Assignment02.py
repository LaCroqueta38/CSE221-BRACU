# Task01
a,b=map(int,input().split())
arr=list(map(int,input().split()))
l=0
r=a-1
found=False
while l<r:
  sum=arr[l]+arr[r]
  if sum==b:
    print(l+1, r+1)
    found=True
    break
  elif sum<b:
    l+=1
  else:
    r-=1
if found==False:
  print(-1)

# Task02
ai=int(input())
al=list(map(int,input().split()))
bi=int(input())
bl=list(map(int,input().split()))
i,j=0,0
result=[]

while i<ai and j<bi:
  if al[i]<bl[j]:
    result.append(str(al[i]))
    i+=1
  else:
    result.append(str(bl[j]))
    j+=1


result.extend(map(str, al[i:]))
result.extend(map(str, bl[j:]))
print(" ".join(result))

# Task03
a,b= map(int, input().split())
c= list(map(int, input().split()))
l=0
sum=0
mlen=0
for r in range(a):
  sum+=c[r]
  while sum>b and l<=r:
    sum-=c[l]
    l+=1
  if sum<=b:
    clen=r-l+1
    if clen>mlen:
      mlen=clen
print(mlen)

# Task04
def f_one_index_finder():
  b=input()
  blen=len(b)
  l=0
  h=blen-1
  res=-1
  while l<=h:
    mid=(l+h)//2
    if b[mid]=="1":
      res=mid+1
      h=mid-1
    else:
      l=mid+1
  if res==-1:
    return -1
  else:
    return res


a=int(input())
for i in range(a):
  print(f_one_index_finder())

# Task05
a,b=map(int,input().split())
arr=list(map(int,input().split()))
for i in range(b):
  c,d=map(int,input().split())
  if c>d:
    c,d=d,c
  l,h=0,a
  while l<h:
    mid=(l+h)//2
    if arr[mid]<c:
      l=mid+1
    else:
      h=mid
  li=l
  l,h=0,a
  while l<h:
    mid=(l+h)//2
    if arr[mid]<=d:
      l=mid+1
    else:
      h=mid
  ri=h
  print(ri-li)