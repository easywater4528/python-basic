#input() 자료형은 항상 문자열 -> 숫자로 변환하는 int(), float()가 있다. cast라고 부름 / 숫자를 문자열로 변환 str()함수
string_a = input("입력A> ") #200
int_a = int(string_a)

string_b = input("입력B> ") #50
int_b = int(string_b)

print("문자열 자료:", string_a+string_b) #20050
print("숫자 자료:", int_a+int_b) #250

#원주율
str_input = input("원의 반지름 입력>") #3
num_input = float(str_input)
print("넓이:", 3.14*num_input**2)

#변수교체 swap
a = input()
b = input()
print(a,b) #안녕 지수
c=a
a=b
b=c
print(b,a) #지수 안녕