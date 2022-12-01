# 6603 로또

def dfs(depth, index):
  if depth==6:
    print(*out)
    return
  
  for i in range(index, k):
    out.append(s[i])
    dfs(depth+1, i+1)
    out.pop() # 리셋

while True:
  a = list(map(int, input().split()))
  if a == [0]:
    break
  k = a[0] 
  s = a[1:]
  out = []
  dfs(0,0)
