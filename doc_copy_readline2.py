#정규 표현식 사용 
import re 

#운영자(웹서버, DB서버 운영하면서 로그파일을 분석)
#원본 로그파일 
f=open('c:\\work\\PV3.txt','rt')
#복사본 파일 
g=open('c:\\work\\PV3_copy.txt','wt',encoding='utf-8')

#로그파일은 500MB ~ 1GB  
#많은 라인의 파일이면 
#한번에 한줄씩 읽어서 처리한다.  
#파일의 EOF(End Of File)이 아니면 계속 읽도록 한다. 
line = f.readline()
while (line != ''):
    if (re.search("error", line)):
        g.write(line + "\n")
    line = f.readline()

f.close() 
g.close()








