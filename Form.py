# Form.py 
# Form.ui(화면을 저장) + Form.py(로직을 저장)
import sys 
from PyQt5.QtWidgets import * 
from PyQt5 import uic 

#미리 저장한 화면을 로딩
form_class = uic.loadUiType("Form.ui")[0]

#폼클래스 정의
class DemoForm(QDialog, form_class):
    def __inㅑt__(self):
        super().__init__() 
        self.setupUi(self)
        self.label.setText("첫번째 Qt데모")

#직접 모듈을 실행했으면 실행
if __name__ == "__main__":
    #실행 프로세스를 생성 
    app = QApplication(sys.argv)
    #클래스의 인스턴스 생성
    demoWindow = DemoForm()
    #화면 보여주기 
    demoWindow.show()
    #계속 프로세스 대기중 
    app.exec_() 