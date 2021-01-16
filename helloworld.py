import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('First Hello.')
window.setGeometry(100,100,280,80)
window.move(60,15)
helloMSG  = QLabel('<h1>Hello world</h1>', parent=window)
helloMSG.move(60,15)
window.show()
sys.exit(app.exec_())