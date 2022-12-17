# 1182 부분수열의 합

def dfs(index, sum):
  global cnt
  if index >= n: 
    return
  sum += arr[index]
  if sum == s:
    cnt+=1
  dfs(index+1, sum-arr[index]) # sum에 해당 인덱스를 포함하는 경우
  dfs(index+1, sum) # 해당 인덱스를 포함하지 않는 경우

n, s = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

dfs(0,0)
print(cnt)
