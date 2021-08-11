# DemoFile.py
#파일 객체를 리턴받기(Write Text)
f = open("c:\\work\\demo.txt", "wt")
f.write("한글\nabcd\n1234\n")
f.close()

#파일 읽기(Read Text) 
f = open("c:\\work\\demo.txt", "rt")
result = f.read()
print( result )
#어디쯤 읽고있어? 
print( f.tell() )
#다시 처음으로 돌아가(리셋)
f.seek(0)
#한번에 한줄씩 읽기
print( f.readline() )
print( f.readline() )

#다시 처음
f.seek(0)
#리스트로 전체를 리턴 
result = f.readlines()
print( result )

#반복구문
for item in result:
    print(item)


f.close() 


