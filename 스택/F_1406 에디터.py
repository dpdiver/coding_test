# 시간 초과
s = list(input())
m = int(input())
cur = len(s) 

for _ in range(m):
    command = input().split()
    if command[0]=="L":
        if cur==0:
            continue
        else:
            cur -=1
    elif command[0]=="D":
        if cur==len(s):
            continue
        else:
            cur+=1
    elif command[0]=="B":
        if cur==0:
            continue
        else:
            del s[cur-1]
    else:
        s.insert(cur, command[1])
        cur+=1

print(''.join(s))   

# 스택을 이용한 풀이
import sys

st1 = list(sys.stdin.readline().rstrip()) # 커서기준 왼쪽
st2 = []             # 커서 기준 오른쪽
m = int(input())

for _ in range(m):
    command = sys.stdin.readline().split()
    if command[0]=='L':
        if st1: # 커서가 맨앞이 아님
            st2.append(st1.pop()) 
    elif command[0]=='D':
        if st2: # 커서가 맨 뒤가 아
            st1.append(st2.pop())
    elif command[0]=='B':
        if st1:
            st1.pop()
    else:
        st1.append(command[1])

print(''.join(st1+list(reversed(st2))))
