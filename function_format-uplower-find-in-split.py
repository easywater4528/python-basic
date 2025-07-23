#format()함수로 숫자를 문자열로 반환하기
format_a = "{}만원".format(5000) #5000만원

#함수 안에 index 별로 {} 존재해야함. {} <= index 구조
format_b = "{} {}".format(1,2) #1 2

#{:d} 는 매개변수 안에 정수만 올 수 있다
output_a = "{:d}.format(52)"

#{:d} 는 매개변수 안에 소수돈 올 수 있다
output_a = "{:f}.format(52.34)"

#{:5d} 는 5칸을 잡고 뒤에서부터 채워라
output_b = "{:5d}.format(52)" #   52

#{:05d} 는 5칸에 빈곳은 0으로 채우기
output_c = "{:05d}.format(52)" #00052
output_d = "{:05d}.format(-52)" #-0052

#소수점 아래 자릿수 지정하기
output_e = "{:5.2f}.format(52.273)" # 52.27

#{:g} 의미 없는 소수점 제거
output_f = "{:g}".format(52.345) #52

#upper() 대문자 변경, lower() 소문자 변경
a = "   Hi Jisoo"
a.upper() #HI JISOO
a.lower() #hi jisoo

#문자열 양옆의 공백 제거 strip()
print(a.strip()) #Hi Jisoo

#문자열 찾기 왼쪽:find() 오른쪽:rfind()
output_g = "안녕안녕하세요".find("안녕")
print(output_g) #0 0번째에 있음

output_h = "안녕안녕하세요".rfind("안녕")
print(output_g) #2 2번째에 있음

#in 연산자 T or F 나옴
print("안녕" in "안녕하세요") #T
print("잘자" in "안녕하세요") #F

#문자열 자르기 split()
a = "10, 20, 30".split(" ") #공백을 기준으로 자른다. 라는 뜻
#['10', '20', '30']