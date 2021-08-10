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



