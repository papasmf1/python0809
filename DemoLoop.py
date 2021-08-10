# DemoLoop.py 

#구구단 출력 
for x in [2,3,4,5,6]:
    print("---{0}단---".format(x))
    for y in [1,2,3,4,5,6,7,8,9]:
        print("{0} * {1} = {2}".format(x, y, x*y))


#break는 탈출
lst = [1,2,3,4,5,6,7,8,9,10]
for i in lst:
    if i > 5:
        break 
    print("Item:{0}".format(i))

print("---continue구문---")
for i in lst:
    if i % 2 == 0:
        continue
    print("Item:{0}".format(i))

#수열을 생성하는 함수
print( range(10) )
print( list(range(10)) )
print( list(range(1, 11)) )
print( list(range(10, 0, -1)) )


#리스트 내장(리스트 함축)
lst = [1,2,3,4,5,6,7,8,9,10]
result = [i**2 for i in lst if i > 5]
print(result)

#필터링 함수
lst = [10, 25, 30]
iterL = filter(None, lst)
for item in iterL:
    print(item)

#함수 정의
def getBiggerThan20(i):
    return i>20 

print("---필터링---")
iterL = filter(getBiggerThan20, lst)
for item in iterL:
    print(item)

#람다 함수
iterL = filter(lambda x:x>20, lst)
for item in iterL:
    print(item)

#맵핑함수 
def add10(i):
    return i + 10 

#호출(스칼라==>단일값) 
lst = [1,2,3]
for i in map(add10, lst):
    print(i)

