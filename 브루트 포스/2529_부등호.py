# 2529 부등호
# https://www.acmicpc.net/problem/25294

n = int(input()) 
sign = input().split()
check = [False]*10
max, min = "",""

# 부등호가 성립하는지 확인
def possible(i,j,k):
  if k=='<':
    return i<j
  else:
    return i>j


def dfs(cnt,s):
  global max, min
  if cnt == n+1: #숫자개수 = 부등호개수+1
    if not len(min): 
      min = s
    else:
      max = s
    return
  for i in range(10):
    if not check[i]:
      if cnt==0 or possible(s[-1], str(i), sign[cnt-1]):
        check[i]=True
        dfs(cnt+1, s+str(i))
        check[i]=False

dfs(0, "")
print(max)
print(min)
