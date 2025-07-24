list_a = [1,2,3]

print("리스트 뒤에 요소 추가")
list_a.append(4)
list_a.append(5)
print(list_a)
print()

print("리스트 중간에 요소 추가")
list_a.insert(0,10)
print(list_a)

print()
print("리스트 중간에 요소 추가")
list_b = [1,2,3]
list_c = [4,5,6]
list_b.extend(list_c)
print(list_b)
print(list_c) #extend:파괴적 처리 / +연산자: 비파괴적 처리
print()

print("인덱스로 리스트의 요소 하나 제거하기: del, pop")
list_d = [0,1,2,3,4,5]
del list_d[1]
print(list_d) #0 2 3 4 5

list_d.pop(2) #pop만쓰면 맨 마지막 요소 제거
print(list_d) #0 2 4 5 
print()

print("del에 대하여")
list_e = [0,1,2,3,4,5,6]
del list_e[3:6] #3부터 6바로 직전까지 삭제 0 1 2 6
print(list_e)
del list_e[:2] #2를 기준으로 2불포함 왼쪽 제거 2 6
print(list_e)
del list_e[1:] #1을 기준으로 6포함 오른쪽 제거
print(list_e)
print()

print("값으로 리스트의 요소 하나 제거하기: remove / clear")
list_d.remove(0)
print(list_d)
list_e.clear()
print(list_e)
