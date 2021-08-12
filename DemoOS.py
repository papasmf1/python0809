# DemoOS.py 
from os.path import * 

#print( dir() )

print( abspath("python.exe") )
print( basename("c:\\work\\python.exe") )
print( getsize("c:\\python38\\python.exe") )
print( exists("c:\\python38\\python.exe") )

#폴더와 파일 리스트 가져오기
import glob 
result = glob.glob("c:\\work\\*.py")
print( result )

#운영체제의 정보나 구문 실행 
import os 
#현재 작업 폴더
print( os.getcwd() )
# ..(부모폴더) .(자기자신) cd \ cd ..
os.chdir("..")
os.chdir("c:\\python38")
print( os.getcwd() )
print("운영체제이름:", os.name )
print("환경변수명:", os.environ.keys() )



