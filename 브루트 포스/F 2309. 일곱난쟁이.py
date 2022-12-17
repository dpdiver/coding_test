# 2309 일곱 난쟁이
arr =[]

for _ in range(9):
  arr.append(int(input()))

def dfs(depth, index):
  if depth == 7: 
    if sum(arr2) ==100:
      for j in sorted(arr2):
        print(j)
      exit() 
    else:
      return 
    
  for i in range(index,9):
    arr2.append(arr[i])
    dfs(depth+1, i+1)
    arr2.pop()

arr2=[]
dfs(0, 0) 
