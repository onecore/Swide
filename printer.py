import sys

from PyQt4.QtGui import *
from PyQt4.QtCore import *


class MyWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.edit = QTextEdit()
        self.edit.setWindowTitle("QTextEdit Standard Output Redirection")
        self.button = QPushButton('Run ldconfig')
        self.button.clicked.connect(self.onClick)
        layout = QVBoxLayout(self)
        layout.addWidget(self.edit)
        layout.addWidget(self.button)

    @pyqtSlot()
    def readStdOutput(self):
        self.edit.append(QString(self.proc.readAllStandardOutput()))

    def onClick(self):
        self.proc = QProcess()
        self.proc.start("python looper.py")
        self.proc.setProcessChannelMode(QProcess.MergedChannels);
        QObject.connect(self.proc, SIGNAL("readyReadStandardOutput()"), self, SLOT("readStdOutput()"));



def main():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    return app.exec_()

if __name__ == '__main__':
    main()