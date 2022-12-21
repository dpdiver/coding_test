# 분할정복
## 1. 병합 정렬
1. 분할: p와 r의 중간 q 찾기 : (p + r)//2
2. 정복: 하위 배열 array[p..q]를 재귀적으로 정렬하고 또 하위 배열array[q+1..r]을 재귀적으로 정렬
3. 결합: 정렬된 두 하위 배열을 하나의 정렬된 하위 배열인 array[p..r]로 결합 
- 탈출 조건 : 2개 미만의 요소가 포함된 하위 배열 (p≥r)

<br/>

![ace963383bea8d154f6abd1322a06a73b56b4628](https://user-images.githubusercontent.com/108377249/208903722-8b5badf8-e736-4d10-a8f7-42c5b18b94df.png)

<br/>
```python
def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr
```
