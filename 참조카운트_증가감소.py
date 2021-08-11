
class MyClass:
    #가장 먼저 초기화를 수행하는 메서드(생성자)
    def __init__(self, value):
        self.Value = value 
        print("Instance is created! Value = ", value)
    #가장 마지막에 수행되는 메서드(소멸자)    
    def __del__(self):
        print("Instance is deleted!")
        
#인스턴스 생성 
c = MyClass(10)
#del c 

print("전체 코드 실행 종료")


