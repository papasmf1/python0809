class Person:
    #클래스 소속 변수
    num_person = 0 
    #생성자 메서드(인스턴스의 초기화를 담당)
    def __init__(self):
        #인스턴스 멤버 변수 초기화
        self.name = "default name"
        Person.num_person += 1 
    def print(self):
        print("My name is {0}".format(self.name))

#인스턴스를 생성
p1 = Person()
p2 = Person() 
print("인스턴스 갯수:{0}".format(Person.num_person) )


