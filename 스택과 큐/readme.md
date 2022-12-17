# 스택 
- Last-In-First-Out
- 파이썬에서는 list를 이용

# 큐
- First-In-First-Out
- list를 이용시 append()로 뒤에 요소 추가, pop(0)으로 맨 앞의 요소 제거
  - list는 무작위 접근에 최적화 -> 연산이 느려짐
- deque를 이용시 append()로 뒤에 요소 추가, popleft()로 맨 앞의 요소 제거
