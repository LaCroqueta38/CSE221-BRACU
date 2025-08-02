# Task01
inp=int(input())
for i in range(inp):
  num=int(input())
  if num%2==1:
    print(f"{num} is an Odd number.")
  else:
    print(f"{num} is an Even number.")

# Task02
inp=int(input())
for i in range(inp):
  inpstr=input().split()
  a=int(inpstr[1])
  op=inpstr[2]
  b=int(inpstr[3])
  if op=="+":
    res=a+b
  elif op=="-":
    res=a-b
  elif op=="*":
    res=a*b
  elif op=="/":
    res=a/b
  print("{0:.6f}".format(res))

# Task03
a,b=map(int,input().split())
arr01=list(map(int,input().split()))
print(' '.join(map(str, arr01[:b][::-1])))

# Task04
inp=int(input())
sum=0
for i in range(inp):
  num=int(input())
  sum=((num*(num+1))//2)
  print(sum)

# Task05
def bubbleSort(arr01):                                                 
    flag=True
    for i in range(len(arr01)-1):
        for j in range(len(arr01)-i-1): 
            if arr01[j] > arr01[j+1]:
              arr01[j], arr01[j+1] = arr01[j+1], arr01[j]
              flag=False
        if flag==True:
              break
    return arr01
n=int(input())
arr01=list(map(int,input().split()))
bubbleSort(arr01)
print(' '.join(map(str, arr01)))

# Task06
inp=int(input())
stdid=list(map(int,input().split()))
stdmark=list(map(int,input().split()))
std=[]
for i in range(inp):
  std.append((-stdmark[i], stdid[i]))
swapct=0
for i in range(inp-1):
  minidx=i
  for j in range(i+1,inp):
    if std[j]<std[minidx]:
      minidx=j
  if minidx != i:
        std[i], std[minidx] = std[minidx], std[i]
        swapct+= 1    
print(f"Minimum swaps: {swapct}")
for i in std:
    print(f"ID: {i[1]} Mark: {-i[0]}")
  

# Task07
inp=int(input())
tr=[]
for i in range(inp):
  stmt=input().strip()
  tn, pre= stmt.split(" will departure for ")
  des, time=pre.split(" at ")
  hr, min=map(int,time.split(":"))
  tmin=(hr*60)+min
  tr.append((tn, -tmin, i, stmt))

swapped=True
i=0
while swapped and i<inp-1:
  swapped= False
  for j in range(inp-i-1):
    curr=tr[j]
    nxttr=tr[j+1]
    if curr[0]>nxttr[0]:
      tr[j], tr[j+1]= tr[j+1], tr[j]
      swapped=True
    elif curr[0]==nxttr[0]:
      if curr[1]>nxttr[1]:
        tr[j], tr[j+1]= tr[j+1], tr[j]
        swapped= True
      elif curr[1]==nxttr[1]:
        if curr[2]>nxttr[2]:
          tr[j], tr[j+1]=tr[j+1], tr[j]
          swapped= True
  i+=1
for k in tr:
  print(k[3])