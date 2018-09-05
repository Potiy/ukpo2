
from PyQt4 import QtCore, QtGui
from lab5_ui import Ui_MainWindow
from PyQt4.QtGui import QWidget, QMessageBox, QApplication
import sys

class mainwindow (QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self): #конструктор класса
        super().__init__()
        QtGui.QMainWindow.__init__(self) #вызов конструктора родителя
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.clr)#присоед. к кнопеке ф-ю clr
        self.pushButton.setToolTip('Count repeated strings')
        self.pushButton_3.clicked.connect(self.ext)
        self.pushButton.clicked.connect(self.f_1)
        self.pushButton_5.clicked.connect(self.fileMy)
        self.filedialog = QtGui.QFileDialog()


    def fileMy (self):
      
        pr=self.filedialog.getOpenFileName(directory="text.txt")
        self.plainTextEdit.setPlainText(open(pr).read())
        
    def clr(self):
        self.plainTextEdit.clear()
        self.plainTextEdit_2.clear()

    def ext(self, event):
        
        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes |
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            import sys
            sys.exit()    


    def f_1(self): #через селф передается ссыль на объект этого класса 
        dictionary = {} #map
        input_str = self.plainTextEdit.toPlainText()
        if not input_str:
            self.plainTextEdit_2.clear()
            self.plainTextEdit_2.insertPlainText("Enter the text")
            return
        for i in "!\"'()*,-./:;?@[\\]_{|}~":#clear from symbols
            input_str = input_str.replace(i,'')
        input_str = input_str.lower()
        words_mass = [x for x in input_str.split(' ') if x]#разб и изб от пробелов
        
        for i in range (2, len(words_mass) + 1): 
            k = 0
            while (k + i + 1) <= len(words_mass):
                glue = ' '.join(words_mass[k:k+i+1])
                p = 0
                count = 0
                while input_str.find(glue, p) != -1: #найдено что-то 
                    count += 1
                    p = input_str.find(glue, p) + len(glue)
                if count > 1:
                    dictionary[glue] = count
                k += 1
        out = ""
        
        for (first, second) in dictionary.items():
            out += "{}: {};".format(first, second)
        self.plainTextEdit_2.clear()
        self.plainTextEdit_2.insertPlainText(out)
        if not self.plainTextEdit_2.toPlainText():
            self.plainTextEdit_2.insertPlainText("No repeated strings")




if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    window = mainwindow()
    window.show()
    #ex = mainwindow.ext(self, )
    sys.exit(app.exec_())

