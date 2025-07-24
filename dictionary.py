dictionary = {
    "name" : "이지수",
    "type" : "SCH STUDENT",
    "food" : ["apple", "banna", "mango"]
}
print()

print("이름: ", dictionary["name"])
print("소속: ", dictionary["type"])
print("과일: ", dictionary["food"][1])
print()

name = "이름"
dict_key = {
    name: "jisoo lee"
}
print(dict_key)
print()

#딕셔너리 값 추가/제거 하기
dictionary["price"] = 5000
print(dictionary)
print()

del dictionary["food"][2]
print(dictionary)
print()

#딕셔너리 내부 특정 키 이름 존재하지 않을경우 keyerror발생! 키가 있는지 확인하기 in키워드
dictionary_key = {
    "a" : 1000,
    "b" : 2000,
    "c" : 3000
}
value = dictionary_key.get("a")
print("값:", value) #1000

value = dictionary_key.get("b")
print("값:", value) #2000

print("값:", dictionary_key.get("d", 0))

print(dictionary_key) #a b c 존재 d는 존재 x

value = dictionary_key.get("e") #초기값을 안넣어줬으니 None으로 접근

if value == None: #에러없이 None으로 빠짐
    print("존재하지 않는 키 접근")