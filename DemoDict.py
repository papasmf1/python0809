# DemoDict.py 

#초기화 
colors = {"apple":"red", "banana":"yellow"}
print( len(colors) )
print( colors )
print( colors["apple"] )

#입력
colors["cherry"] = "red"
print( colors )

#중단점(Break Point)
for item in colors.items():
    print(item)

for k,v in colors.items():
    print(k,v)

#디바이스를 관리(딕셔너리)
device = {"아이폰":5,"아이패드":10,"윈도우":20}
print( device )
#입력
device["맥프레"] = 15 
print( device )
#수정
device["아이폰"] = 6 
print( device )
#삭제
del device["윈도우"]
print( device )
#검색
print( device["아이폰"] )

#반복구문
for key in device.keys():
    print(key)

for value in device.values():
    print(value)

for k,v in device.items():
    print(k,v)


#명함 관리
phone = {"kim":"1111", "lee":"2222", "park":"3333"}
print( "kim" in phone )
print( "moon" in phone )
print( "moon" not in phone )

#참조만 복사
p = phone 
print( p )
p["kang"] = "1234"
print( phone )
print( p )

