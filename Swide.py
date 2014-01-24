# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Swide.ui'
#
# Created: Wed Jan 22 19:38:31 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4.QtGui import QApplication
from PyQt4 import QtCore, QtGui
from PyQt4 import Qsci
from PyQt4.Qsci import QsciScintilla, QsciScintillaBase, QsciLexerPython
from Settings import Settings
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_sawaIDE(object):
    def __init__(self):
        swideSettings = Setting
    def setupUi(self, sawaIDE):
        sawaIDE.setObjectName(_fromUtf8("sawaIDE"))
        sawaIDE.resize(926, 802)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../Python/python.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        sawaIDE.setWindowIcon(icon)
        sawaIDE.setStyleSheet(_fromUtf8("background: rgb(102, 102, 102);\n"
"color: rgb(245, 245, 245);"))
        self.compileNow = QtGui.QPushButton(sawaIDE)
        self.compileNow.setGeometry(QtCore.QRect(330, 10, 161, 41))
        self.compileNow.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.compileNow.setStyleSheet(_fromUtf8("QPushButton {\n"
"  background: rgb(255, 119, 0);\n"
"  border-radius: 28px;\n"
"  font-family: Arial;\n"
"  color: #ffffff;\n"
"  font-size: 15px;\n"
"  padding: 10px 20px 10px 20px;\n"
"  text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background: rgb(255, 190, 85);\n"
"  text-decoration: none;\n"
"}"))
        self.compileNow.setObjectName(_fromUtf8("compileNow"))
        self.File = QtGui.QPushButton(sawaIDE)
        self.File.setGeometry(QtCore.QRect(10, 10, 161, 41))
        self.File.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.File.setStyleSheet(_fromUtf8("QPushButton {\n"
"  background: rgb(0, 77, 113);\n"
"  border-radius: 28px;\n"
"  font-family: Arial;\n"
"  color: #ffffff;\n"
"  font-size: 15px;\n"
"  padding: 10px 20px 10px 20px;\n"
"  text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background: rgb(0, 108, 158);\n"
"  text-decoration: none;\n"
"}"))
        self.File.setObjectName(_fromUtf8("File"))





        self.options = QtGui.QPushButton(sawaIDE)
        self.options.setGeometry(QtCore.QRect(170, 10, 161, 41))
        self.options.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.options.setStyleSheet(_fromUtf8("QPushButton {\n"
"  background: rgb(0, 77, 113);\n"
"  border-radius: 28px;\n"
"  font-family: Arial;\n"
"  color: #ffffff;\n"
"  font-size: 15px;\n"
"  padding: 10px 20px 10px 20px;\n"
"  text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background: rgb(0, 108, 158);\n"
"  text-decoration: none;\n"
"}"))
        self.options.setObjectName(_fromUtf8("options"))
        self.itsSwide = QtGui.QLabel(sawaIDE)
        self.itsSwide.setGeometry(QtCore.QRect(690, 20, 211, 31))
        self.itsSwide.setStyleSheet(_fromUtf8("background: transparent;"))
        self.itsSwide.setText(_fromUtf8(""))
        self.itsSwide.setPixmap(QtGui.QPixmap(_fromUtf8("../../../../Python/LJ5J591388303749.png")))
        self.itsSwide.setScaledContents(True)
        self.itsSwide.setObjectName(_fromUtf8("itsSwide"))
        self.consoleDockObj = QtGui.QDockWidget(sawaIDE)
        self.consoleDockObj.setGeometry(QtCore.QRect(10, 630, 891, 161))
        self.consoleDockObj.setAllowedAreas(QtCore.Qt.NoDockWidgetArea)
        self.consoleDockObj.setObjectName(_fromUtf8("consoleDockObj"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.consoleObj = QtGui.QPlainTextEdit(self.dockWidgetContents)
        self.consoleObj.setGeometry(QtCore.QRect(0, 0, 891, 131))
        self.consoleObj.setObjectName(_fromUtf8("consoleObj"))
        self.consoleDockObj.setWidget(self.dockWidgetContents)
        self.EditorDockObj = QtGui.QDockWidget(sawaIDE)
        self.EditorDockObj.setGeometry(QtCore.QRect(10, 60, 911, 561))
        self.EditorDockObj.setAcceptDrops(False)
        self.EditorDockObj.setWindowIcon(icon)
        self.EditorDockObj.setFloating(False)
        self.EditorDockObj.setFeatures(QtGui.QDockWidget.DockWidgetFloatable|QtGui.QDockWidget.DockWidgetMovable|QtGui.QDockWidget.DockWidgetVerticalTitleBar)
        self.EditorDockObj.setAllowedAreas(QtCore.Qt.AllDockWidgetAreas)
        self.EditorDockObj.setObjectName(_fromUtf8("EditorDockObj"))
        self.dockWidgetContents_2 = QtGui.QWidget()
        self.dockWidgetContents_2.setObjectName(_fromUtf8("dockWidgetContents_2"))
        self.editorObj = QsciScintilla(self.dockWidgetContents_2)
        self.editorObj.setGeometry(QtCore.QRect(0, 0, 871, 561))
        self.EditorDockObj.setWidget(self.dockWidgetContents_2)

        self.start = QtGui.QPushButton(sawaIDE)
        self.start.setGeometry(QtCore.QRect(742, 60, 161, 41))
        self.start.setText('Enable AC')
        self.start.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.start.setStyleSheet(_fromUtf8("QPushButton {\n"
"  background: rgb(0, 77, 113);\n"
"  border-radius: 28px;\n"
"  font-family: Arial;\n"
"  color: #ffffff;\n"
"  font-size: 15px;\n"
"  padding: 10px 20px 10px 20px;\n"
"  text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background: rgb(0, 108, 158);\n"
"  text-decoration: none;\n"
"}"))
        self.start.setObjectName(_fromUtf8("Start"))


        self.retranslateUi(sawaIDE)
        QtCore.QObject.connect(self.compileNow, QtCore.SIGNAL(_fromUtf8("clicked()")), self.compileNowFn)
        QtCore.QObject.connect(self.options, QtCore.SIGNAL(_fromUtf8("clicked()")), self.OptionsFn)
        QtCore.QObject.connect(self.File, QtCore.SIGNAL(_fromUtf8("clicked()")), self.FileObjFn)
        QtCore.QObject.connect(self.start, QtCore.SIGNAL(_fromUtf8("clicked()")), self.startSwide)
        QtCore.QMetaObject.connectSlotsByName(sawaIDE)

    def retranslateUi(self, sawaIDE):
        sawaIDE.setWindowTitle(_translate("sawaIDE", "Swide | SawaIDE - Fresh hunt from the Philippines", None))
        self.compileNow.setText(_translate("sawaIDE", "Run and Compile", None))
        self.File.setText(_translate("sawaIDE", "File", None))
        self.options.setText(_translate("sawaIDE", "Options", None))
        self.consoleDockObj.setWindowTitle(_translate("sawaIDE", "  Python Interpreter", None))
        self.EditorDockObj.setWindowTitle(_translate("sawaIDE", " SWIDE Code View", None))

    def compileNowFn(self):
        pass
    def OptionsFn(self):
        pass
    def FileObjFn(self):
        import time
        from threading import Thread
        swideEditor = self.editorObj
        swideLexer = QsciLexerPython(sawaIDE)
        swideApi = Qsci.QsciAPIs(swideLexer)
        swideApi.add("aLongString")
        swideApi.add("aLongerString")
        swideApi.add("aDifferentString")
        swideApi.add("sOmethingElse")

        swideApi.prepare()
        swideEditor.setLexer(swideLexer)
        swideEditor.setAutoCompletionThreshold(1)
        swideEditor.setAutoCompletionSource(QsciScintilla.AcsAPIs)
        swideEditor.setCaretLineVisible(True)
        swideEditor.setCaretLineBackgroundColor(QtGui.QColor("#CDA869"))
        swideEditor.setEdgeMode(QsciScintilla.EdgeLine)
        swideEditor.setEdgeColumn(138)
        swideEditor.setFolding(QsciScintilla.BoxedTreeFoldStyle)
        swideEditor.setBraceMatching(QsciScintilla.SloppyBraceMatch)
        swideEditor.setEdgeColor(QtGui.QColor("#FF0000"))
        #swideEditor.setMarginsBackgroundColor(QtGui.QColor("#333333"))
        #swideEditor.setMarginsForegroundColor(QtGui.QColor("#CCCCCC"))
        #swideEditor.setFoldMarginColors(QtGui.QColor("#99CC66"),QtGui.QColor("#333300"))
        ## define the font to use
        xfont = QtGui.QFont()
        xfont.setFamily("Consolas")
        xfont.setFixedPitch(True)
        xfont.setPointSize(10)
        xfont.OpenGLCompatible
        # the font metrics here will help
        # building the margin width later
        fm = QtGui.QFontMetrics(xfont)
        swideEditor.setMarginWidth(0, fm.width( "000" ) + 5)
        swideEditor.setMarginLineNumbers(0, True)
        swideEditor.show()
        swideEditor.setText(open("codemodel.py").read())

    def startSwide(self):
        # generic thread using signal
        self.connect( self, QtCore.SIGNAL("add(QString)"), Ui_sawaIDE.FileObjFn)




if __name__ == "__main__":
    import sys
    from threading import Thread

    app = QtGui.QApplication(sys.argv)
    sawaIDE = QtGui.QWidget()
    ui = Ui_sawaIDE()
    ui.setupUi(sawaIDE)
    sawaIDE.show()
    sys.exit(app.exec_())
