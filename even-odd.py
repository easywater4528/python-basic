#첫 번째 sol.
number = input()

#마지막 자리 숫자 추출
last_character = number[-1]

#숫자로 변환
last_number = int(last_character)

#짝수 확인
if last_number == 0 \
    or last_number == 2 \
    or last_number == 4 \
    or last_number == 6 \
    or last_number == 8:
    print("짝수")

#홀수 확인
if last_number == 1 \
    or last_number == 3 \
    or last_number == 5 \
    or last_number == 7 \
    or last_number == 9:
    print("홀수")


#sol2
number2 = input()
last_character2 = number2[-1]

if last_character2 in "02468":
    print("짝수")
if last_character2 in "13579":
    print("홀수")

#sol3
number3 = int(input())

if number3 % 2 == 0:
    print("짝수")

if number3 % 2 == 1:
    print("홀수")