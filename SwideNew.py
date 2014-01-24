# -*- coding: utf-8 -*-

__author__ = 'Mark Anthony Pequeras'
__software__ = 'Invictuz Online Game'
__year__ = '2013'
__python__ = '2.7'
__developers__ = 'CoreSEC Software Development Group'


import sys
from PyQt4.QtGui import QApplication
from PyQt4 import QtCore, QtGui
from PyQt4 import Qsci
from PyQt4.Qsci import QsciScintilla, QsciScintillaBase, QsciLexerPython
from Settings import Settings
import ConfigParser
import io
import subprocess

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
        """ Let's Load Useful Stuffs here"""
        self.mainFile = Settings.swideSettings
        self.swideSettings = ConfigParser.RawConfigParser(allow_no_value=True)
        self.swideSettings.readfp(io.BytesIO(self.mainFile))
        self.swideInterpreterSection = 'Swide Interpreter' #interpreter config section
        self.interPath = self.swideSettings.get(self.swideInterpreterSection,'pythonPath')
        self.pythonPath = self.interPath #Interpreter Location Copy
        self.setupFile = ''




    def setupUi(self, sawaIDE):
        sawaIDE.setObjectName(_fromUtf8("sawaIDE"))
        sawaIDE.resize(926, 802)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../Python/python.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        sawaIDE.setWindowIcon(icon)
        sawaIDE.setStyleSheet(_fromUtf8("background: rgb(102, 102, 102);\n"
"color: rgb(245, 245, 245);"))
        self.FileObj = QtGui.QPushButton(sawaIDE)
        self.FileObj.setGeometry(QtCore.QRect(10, 90, 161, 31))
        self.FileObj.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.FileObj.setStyleSheet(_fromUtf8("QPushButton {\n"
"  background: rgb(0, 77, 113);\n"
"  border-radius: 28px;\n"
"  font-family: Arial;\n"
"  color: #ffffff;\n"
"  font-size: 10px;\n"
"  padding: 10px 20px 10px 20px;\n"
"  text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background: rgb(0, 108, 158);\n"
"  text-decoration: none;\n"
"}"))
        self.FileObj.setObjectName(_fromUtf8("FileObj"))
        self.optionsObj = QtGui.QPushButton(sawaIDE)
        self.optionsObj.setGeometry(QtCore.QRect(10, 210, 161, 31))
        self.optionsObj.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.optionsObj.setStyleSheet(_fromUtf8("QPushButton {\n"
"  background: rgb(0, 77, 113);\n"
"  border-radius: 28px;\n"
"  font-family: Arial;\n"
"  color: #ffffff;\n"
"  font-size: 10px;\n"
"  padding: 10px 20px 10px 20px;\n"
"  text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background: rgb(0, 108, 158);\n"
"  text-decoration: none;\n"
"}"))
        self.optionsObj.setObjectName(_fromUtf8("optionsObj"))
        self.itsSwide_2 = QtGui.QLabel(sawaIDE)
        self.itsSwide_2.setGeometry(QtCore.QRect(380, 280, 231, 61))
        self.itsSwide_2.setStyleSheet(_fromUtf8("background: transparent;"))
        self.itsSwide_2.setText(_fromUtf8(""))
        self.itsSwide_2.setPixmap(QtGui.QPixmap(_fromUtf8("../../../../Python/LJ5J591388303749.png")))
        self.itsSwide_2.setScaledContents(True)
        self.itsSwide_2.setObjectName(_fromUtf8("itsSwide_2"))
        self.swirdeLogo = QtGui.QLabel(sawaIDE)
        self.swirdeLogo.setGeometry(QtCore.QRect(20, 20, 141, 21))
        self.swirdeLogo.setStyleSheet(_fromUtf8("background: transparent;"))
        self.swirdeLogo.setText(_fromUtf8(""))
        self.swirdeLogo.setPixmap(QtGui.QPixmap(_fromUtf8("../../../../Python/LJ5J591388303749.png")))
        self.swirdeLogo.setScaledContents(True)
        self.swirdeLogo.setObjectName(_fromUtf8("swirdeLogo"))
        self.consoleDockObj = QtGui.QDockWidget(sawaIDE)
        self.consoleDockObj.setGeometry(QtCore.QRect(10, 630, 901, 161))
        self.consoleDockObj.setAllowedAreas(QtCore.Qt.NoDockWidgetArea)
        self.consoleDockObj.setObjectName(_fromUtf8("consoleDockObj"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.consoleObj = QtGui.QTextEdit(self.dockWidgetContents)
        self.consoleObj.setGeometry(QtCore.QRect(0, 0, 801, 131))
        self.consoleOptionsObj = QtGui.QPushButton(self.dockWidgetContents)
        self.consoleOptionsObj.setGeometry(QtCore.QRect(800, 0, 101, 31))
        self.consoleOptionsObj.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.consoleOptionsObj.setStyleSheet(_fromUtf8("QPushButton {\n"
"  background: rgb(255, 119, 0);\n"
"  border-radius: 28px;\n"
"  font-family: Arial;\n"
"  color: #ffffff;\n"
"  font-size: 10px;\n"
"  padding: 10px 20px 10px 20px;\n"
"  text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background: rgb(255, 190, 85);\n"
"  text-decoration: none;\n"
"}"))
        self.consoleOptionsObj.setObjectName(_fromUtf8("consoleOptionsObj"))
        self.clearConsoleObj = QtGui.QPushButton(self.dockWidgetContents)
        self.clearConsoleObj.setGeometry(QtCore.QRect(800, 30, 101, 31))
        self.clearConsoleObj.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.clearConsoleObj.setStyleSheet(_fromUtf8("QPushButton {\n"
"  background: rgb(255, 119, 0);\n"
"  border-radius: 28px;\n"
"  font-family: Arial;\n"
"  color: #ffffff;\n"
"  font-size: 10px;\n"
"  padding: 10px 20px 10px 20px;\n"
"  text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background: rgb(255, 190, 85);\n"
"  text-decoration: none;\n"
"}"))
        self.clearConsoleObj.setObjectName(_fromUtf8("clearConsoleObj"))
        self.consoleDockObj.setWidget(self.dockWidgetContents)
        self.EditorDockObj = QtGui.QDockWidget(sawaIDE)
        self.EditorDockObj.setGeometry(QtCore.QRect(180, 10, 741, 611))
        self.EditorDockObj.setAcceptDrops(False)
        self.EditorDockObj.setWindowIcon(icon)
        self.EditorDockObj.setFloating(False)
        self.EditorDockObj.setFeatures(QtGui.QDockWidget.DockWidgetFloatable|QtGui.QDockWidget.DockWidgetMovable|QtGui.QDockWidget.DockWidgetVerticalTitleBar)
        self.EditorDockObj.setAllowedAreas(QtCore.Qt.AllDockWidgetAreas)
        self.EditorDockObj.setObjectName(_fromUtf8("EditorDockObj"))
        self.dockWidgetContents_2 = QtGui.QWidget()
        self.dockWidgetContents_2.setObjectName(_fromUtf8("dockWidgetContents_2"))
        self.compileNowObj = QtGui.QPushButton(self.dockWidgetContents_2)
        self.compileNowObj.setGeometry(QtCore.QRect(620, 570, 81, 31))
        self.compileNowObj.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.compileNowObj.setStyleSheet(_fromUtf8("QPushButton {\n"
"  background: rgb(103, 129, 30);\n"
"  border-radius: 28px;\n"
"  font-family: Arial;\n"
"  color: #ffffff;\n"
"  font-size: 10px;\n"
"  padding: 10px 20px 10px 20px;\n"
"  text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background: rgb(255, 190, 85);\n"
"  text-decoration: none;\n"
"}"))
        self.compileNowObj.setObjectName(_fromUtf8("compileNowObj"))
        self.swideEditorUi = QsciScintilla(self.dockWidgetContents_2)
        self.swideEditorUi.setGeometry(QtCore.QRect(10, 10, 601, 591))

        self.setUpCompilerObj = QtGui.QPushButton(self.dockWidgetContents_2)
        self.setUpCompilerObj.setGeometry(QtCore.QRect(620, 540, 81, 31))
        self.setUpCompilerObj.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.setUpCompilerObj.setStyleSheet(_fromUtf8("QPushButton {\n"
"  background: rgb(255, 119, 0);\n"
"  border-radius: 28px;\n"
"  font-family: Arial;\n"
"  color: #ffffff;\n"
"  font-size: 10px;\n"
"  padding: 10px 20px 10px 20px;\n"
"  text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background: rgb(255, 190, 85);\n"
"  text-decoration: none;\n"
"}"))
        self.setUpCompilerObj.setObjectName(_fromUtf8("setUpCompilerObj"))
        self.DockObj = QtGui.QPushButton(self.dockWidgetContents_2)
        self.DockObj.setGeometry(QtCore.QRect(620, 510, 81, 31))
        self.DockObj.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.DockObj.setStyleSheet(_fromUtf8("QPushButton {\n"
"  background: rgb(255, 119, 0);\n"
"  border-radius: 28px;\n"
"  font-family: Arial;\n"
"  color: #ffffff;\n"
"  font-size: 10px;\n"
"  padding: 10px 20px 10px 20px;\n"
"  text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background: rgb(255, 190, 85);\n"
"  text-decoration: none;\n"
"}"))
        self.DockObj.setObjectName(_fromUtf8("DockObj"))
        self.floatDockObj = QtGui.QPushButton(self.dockWidgetContents_2)
        self.floatDockObj.setGeometry(QtCore.QRect(620, 480, 81, 31))
        self.floatDockObj.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.floatDockObj.setStyleSheet(_fromUtf8("QPushButton {\n"
"  background: rgb(255, 119, 0);\n"
"  border-radius: 28px;\n"
"  font-family: Arial;\n"
"  color: #ffffff;\n"
"  font-size: 10px;\n"
"  padding: 10px 20px 10px 20px;\n"
"  text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background: rgb(255, 190, 85);\n"
"  text-decoration: none;\n"
"}"))
        self.floatDockObj.setObjectName(_fromUtf8("floatDockObj"))
        self.saveObj = QtGui.QPushButton(self.dockWidgetContents_2)
        self.saveObj.setGeometry(QtCore.QRect(620, 420, 81, 31))
        self.saveObj.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.saveObj.setStyleSheet(_fromUtf8("QPushButton {\n"
"  background: rgb(255, 119, 0);\n"
"  border-radius: 28px;\n"
"  font-family: Arial;\n"
"  color: #ffffff;\n"
"  font-size: 10px;\n"
"  padding: 10px 20px 10px 20px;\n"
"  text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background: rgb(255, 190, 85);\n"
"  text-decoration: none;\n"
"}"))
        self.saveObj.setObjectName(_fromUtf8("saveObj"))
        self.saveAsObj = QtGui.QPushButton(self.dockWidgetContents_2)
        self.saveAsObj.setGeometry(QtCore.QRect(620, 450, 81, 31))
        self.saveAsObj.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.saveAsObj.setStyleSheet(_fromUtf8("QPushButton {\n"
"  background: rgb(255, 119, 0);\n"
"  border-radius: 28px;\n"
"  font-family: Arial;\n"
"  color: #ffffff;\n"
"  font-size: 10px;\n"
"  padding: 10px 20px 10px 20px;\n"
"  text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background: rgb(255, 190, 85);\n"
"  text-decoration: none;\n"
"}"))
        self.saveAsObj.setObjectName(_fromUtf8("saveAsObj"))
        self.ClassesViewObj = QtGui.QListWidget(self.dockWidgetContents_2)
        self.ClassesViewObj.setGeometry(QtCore.QRect(620, 40, 81, 41))
        self.ClassesViewObj.setStyleSheet(_fromUtf8("border: transparent;"))
        self.ClassesViewObj.setObjectName(_fromUtf8("ClassesViewObj"))
        self.openFileObj = QtGui.QPushButton(self.dockWidgetContents_2)
        self.openFileObj.setGeometry(QtCore.QRect(620, 390, 81, 31))
        self.openFileObj.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.openFileObj.setStyleSheet(_fromUtf8("QPushButton {\n"
"  background: rgb(255, 119, 0);\n"
"  border-radius: 28px;\n"
"  font-family: Arial;\n"
"  color: #ffffff;\n"
"  font-size: 10px;\n"
"  padding: 10px 20px 10px 20px;\n"
"  text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background: rgb(255, 190, 85);\n"
"  text-decoration: none;\n"
"}"))
        self.openFileObj.setObjectName(_fromUtf8("openFileObj"))
        self.ClassesLabel = QtGui.QLabel(self.dockWidgetContents_2)
        self.ClassesLabel.setGeometry(QtCore.QRect(620, 10, 41, 16))
        self.ClassesLabel.setObjectName(_fromUtf8("ClassesLabel"))
        self.functionsLabel = QtGui.QLabel(self.dockWidgetContents_2)
        self.functionsLabel.setGeometry(QtCore.QRect(620, 90, 41, 16))
        self.functionsLabel.setObjectName(_fromUtf8("functionsLabel"))
        self.FunctionsViewObj = QtGui.QListWidget(self.dockWidgetContents_2)
        self.FunctionsViewObj.setGeometry(QtCore.QRect(620, 110, 81, 81))
        self.FunctionsViewObj.setStyleSheet(_fromUtf8("border: transparent;"))
        self.FunctionsViewObj.setObjectName(_fromUtf8("FunctionsViewObj"))
        self.variablesObj = QtGui.QLabel(self.dockWidgetContents_2)
        self.variablesObj.setGeometry(QtCore.QRect(620, 200, 41, 16))
        self.variablesObj.setObjectName(_fromUtf8("variablesObj"))
        self.variableListViewObj = QtGui.QListWidget(self.dockWidgetContents_2)
        self.variableListViewObj.setGeometry(QtCore.QRect(620, 220, 81, 161))
        self.variableListViewObj.setStyleSheet(_fromUtf8("border: transparent;"))
        self.variableListViewObj.setObjectName(_fromUtf8("variableListViewObj"))
        self.EditorDockObj.setWidget(self.dockWidgetContents_2)
        self.AppearanceObj = QtGui.QPushButton(sawaIDE)
        self.AppearanceObj.setGeometry(QtCore.QRect(10, 120, 161, 31))
        self.AppearanceObj.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.AppearanceObj.setStyleSheet(_fromUtf8("QPushButton {\n"
"  background: rgb(0, 77, 113);\n"
"  border-radius: 28px;\n"
"  font-family: Arial;\n"
"  color: #ffffff;\n"
"  font-size: 10px;\n"
"  padding: 10px 20px 10px 20px;\n"
"  text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background: rgb(0, 108, 158);\n"
"  text-decoration: none;\n"
"}"))
        self.AppearanceObj.setObjectName(_fromUtf8("AppearanceObj"))
        self.completionsObj = QtGui.QPushButton(sawaIDE)
        self.completionsObj.setGeometry(QtCore.QRect(10, 150, 161, 31))
        self.completionsObj.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.completionsObj.setStyleSheet(_fromUtf8("QPushButton {\n"
"  background: rgb(0, 77, 113);\n"
"  border-radius: 28px;\n"
"  font-family: Arial;\n"
"  color: #ffffff;\n"
"  font-size: 10px;\n"
"  padding: 10px 20px 10px 20px;\n"
"  text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background: rgb(0, 108, 158);\n"
"  text-decoration: none;\n"
"}"))
        self.completionsObj.setObjectName(_fromUtf8("completionsObj"))
        self.codeModelObj = QtGui.QPushButton(sawaIDE)
        self.codeModelObj.setGeometry(QtCore.QRect(10, 180, 161, 31))
        self.codeModelObj.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.codeModelObj.setStyleSheet(_fromUtf8("QPushButton {\n"
"  background: rgb(0, 77, 113);\n"
"  border-radius: 28px;\n"
"  font-family: Arial;\n"
"  color: #ffffff;\n"
"  font-size: 10px;\n"
"  padding: 10px 20px 10px 20px;\n"
"  text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background: rgb(0, 108, 158);\n"
"  text-decoration: none;\n"
"}"))
        self.codeModelObj.setObjectName(_fromUtf8("codeModelObj"))
        self.directoryViewObj = QtGui.QListView(sawaIDE)
        self.directoryViewObj.setGeometry(QtCore.QRect(10, 281, 161, 341))
        self.directoryViewObj.setObjectName(_fromUtf8("directoryViewObj"))
        self.newFolderProjectObj = QtGui.QPushButton(sawaIDE)
        self.newFolderProjectObj.setGeometry(QtCore.QRect(10, 60, 161, 31))
        self.newFolderProjectObj.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.newFolderProjectObj.setStyleSheet(_fromUtf8("QPushButton {\n"
"  background: rgb(0, 77, 113);\n"
"  border-radius: 28px;\n"
"  font-family: Arial;\n"
"  color: #ffffff;\n"
"  font-size: 10px;\n"
"  padding: 10px 20px 10px 20px;\n"
"  text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background: rgb(0, 108, 158);\n"
"  text-decoration: none;\n"
"}"))
        self.newFolderProjectObj.setObjectName(_fromUtf8("newFolderProjectObj"))
        self.checkforUpdatesObj = QtGui.QPushButton(sawaIDE)
        self.checkforUpdatesObj.setGeometry(QtCore.QRect(10, 240, 161, 31))
        self.checkforUpdatesObj.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.checkforUpdatesObj.setStyleSheet(_fromUtf8("QPushButton {\n"
"  background: rgb(0, 77, 113);\n"
"  border-radius: 28px;\n"
"  font-family: Arial;\n"
"  color: #ffffff;\n"
"  font-size: 10px;\n"
"  padding: 10px 20px 10px 20px;\n"
"  text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background: rgb(0, 108, 158);\n"
"  text-decoration: none;\n"
"}"))
        self.checkforUpdatesObj.setObjectName(_fromUtf8("checkforUpdatesObj"))

        self.retranslateUi(sawaIDE)
        QtCore.QObject.connect(self.optionsObj, QtCore.SIGNAL(_fromUtf8("clicked()")), self._Options)
        QtCore.QObject.connect(self.FileObj, QtCore.SIGNAL(_fromUtf8("clicked()")), self._FileObj)
        QtCore.QObject.connect(self.checkforUpdatesObj, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self._checkUpdate)
        QtCore.QObject.connect(self.codeModelObj, QtCore.SIGNAL(_fromUtf8("clicked()")), self._codeModel)
        QtCore.QObject.connect(self.completionsObj, QtCore.SIGNAL(_fromUtf8("clicked()")), self._completions)
        QtCore.QObject.connect(self.AppearanceObj, QtCore.SIGNAL(_fromUtf8("clicked()")), self._appearance)
        QtCore.QObject.connect(self.newFolderProjectObj, QtCore.SIGNAL(_fromUtf8("clicked()")), self._newProject)
        QtCore.QObject.connect(self.openFileObj, QtCore.SIGNAL(_fromUtf8("clicked()")), self._open)
        QtCore.QObject.connect(self.saveObj, QtCore.SIGNAL(_fromUtf8("clicked()")), self._save)
        QtCore.QObject.connect(self.saveAsObj, QtCore.SIGNAL(_fromUtf8("clicked()")), self._saveAs)
        QtCore.QObject.connect(self.floatDockObj, QtCore.SIGNAL(_fromUtf8("clicked()")), self._detach)
        QtCore.QObject.connect(self.DockObj, QtCore.SIGNAL(_fromUtf8("clicked()")), self._attach)
        QtCore.QObject.connect(self.setUpCompilerObj, QtCore.SIGNAL(_fromUtf8("clicked()")), self._setUp)
        QtCore.QObject.connect(self.compileNowObj, QtCore.SIGNAL(_fromUtf8("clicked()")), self._compileNow)
        QtCore.QObject.connect(self.consoleOptionsObj, QtCore.SIGNAL(_fromUtf8("clicked()")), self._cOptions)
        QtCore.QObject.connect(self.clearConsoleObj, QtCore.SIGNAL(_fromUtf8("clicked()")), self._clearOutput)
        QtCore.QMetaObject.connectSlotsByName(sawaIDE)

    def retranslateUi(self, sawaIDE):
        sawaIDE.setWindowTitle(_translate("sawaIDE", "Swide | Sawa IDE", None))
        self.FileObj.setText(_translate("sawaIDE", "File", None))
        self.optionsObj.setText(_translate("sawaIDE", "Options", None))
        self.consoleDockObj.setWindowTitle(_translate("sawaIDE", "  Python Interpreter", None))
        self.consoleOptionsObj.setText(_translate("sawaIDE", "Options", None))
        self.clearConsoleObj.setText(_translate("sawaIDE", "Clear", None))
        self.EditorDockObj.setWindowTitle(_translate("sawaIDE", "  Code View", None))
        self.compileNowObj.setText(_translate("sawaIDE", "Compile", None))
        self.setUpCompilerObj.setText(_translate("sawaIDE", "Set-Up", None))
        self.DockObj.setText(_translate("sawaIDE", "Attach", None))
        self.floatDockObj.setText(_translate("sawaIDE", "Detach", None))
        self.saveObj.setText(_translate("sawaIDE", "Save", None))
        self.saveAsObj.setText(_translate("sawaIDE", "Save As", None))
        self.openFileObj.setText(_translate("sawaIDE", "Open", None))
        self.ClassesLabel.setText(_translate("sawaIDE", "Classes", None))
        self.functionsLabel.setText(_translate("sawaIDE", "Functions", None))
        self.variablesObj.setText(_translate("sawaIDE", "Variables", None))
        self.AppearanceObj.setText(_translate("sawaIDE", "Appearance", None))
        self.completionsObj.setText(_translate("sawaIDE", "Completions", None))
        self.codeModelObj.setText(_translate("sawaIDE", "Code Model", None))
        self.newFolderProjectObj.setText(_translate("sawaIDE", "New Project", None))
        self.checkforUpdatesObj.setText(_translate("sawaIDE", "Check Updates", None))
    def _clearOutput(self):
        pass
    def _Options(self):
        pass
    def _FileObj(self):
        pass
    def _checkUpdate(self):
        pass
    def _codeModel(self):
        pass
    def _completions(self):
        pass
    def _appearance(self):
        pass
    def _newProject(self):
        pass

# OutPart
    def swideOutput(self):

        self.consoleObj.append(QtCore.QString(self.proc.readAllStandardOutput()))
    def _open(self):
        self.consoleObj.append('<b>Interpreter Started...</b><br>')

        self.consoleObj.setDisabled(0)
        self.proc = QtCore.QProcess()
        self.proc.start("python")
        self.proc.setProcessChannelMode(QtCore.QProcess.MergedChannels);
        QtCore.QObject.connect(self.proc, QtCore.SIGNAL("readyReadStandardOutput()"), self.swideOutput)

# OutPart

    def _save(self):
        print self.swideEditorUi.text()
    def _saveAs(self):
        pass
    def _detach(self):
        """
        I am the Detacher
        """
        self.EditorDockObj.setFloating(1)

    def _attach(self):
        """
        I am the Docker
        """
        self.EditorDockObj.setFloating(0)
        self.EditorDockObj.setGeometry(QtCore.QRect(180, 10, 741, 611))

    def _setUp(self):
        pass
    def _compileNow(self):
        import os
        import thread
        currentDir = os.getcwd()
        console = self.consoleObj
        ppath = self.pythonPath
        fpath = self.setupFile
        editorCode = self.swideEditorUi.text()
        currentCache = open('cache.py','w+')
        currentCache.write(editorCode)
        currentCache.close()
# ----------------------------------------------------------
        def runme():

            gotoCWD = str(currentDir)
            gotoCmd = 'cd {dir}'.format(dir=gotoCWD)
            subprocess.Popen(gotoCmd,shell=True)
            proc = QtCore.QProcess()
            proc.start("cmd")
            #swideComp = "C:/Python/App/python.exe C:\Users\Mark\PycharmProjects\Swide\printer.py" #.format(pythonpath=ppath,setupName=fpath)
            #process = subprocess.Popen(swideComp, shell=True, stdin=None, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            #stdout, stderr = process.communicate()
            out = proc.readAllStandardOutput()
            error = proc.readAllStandardError()
            #console.insertPlainText(stdout)
            #console.insertPlainText(stderr)
            #print stderr,stdout
            print out
        thread.start_new_thread (runme, ())



# ----------------------------------------------------------
    def _cOptions(self):
        optBox = QtGui.QDialog(sawaIDE)
        optBox.setWindowTitle('Interpreter Options')
        optBox.setFixedHeight(300), optBox.setFixedWidth(400)
        # optBox Contents Starts
        # --------------------------------------------------------------
        saveButton = QtGui.QPushButton(optBox)    # SAVE BUTTON
        saveButton.setText('Save')
        saveButton.setGeometry(320,243,70,40)
        saveButton.setStyleSheet("QPushButton {\n"
                                "  background: rgb(0, 77, 113);\n"
                                "  border-radius: 28px;\n"
                                "  font-family: Arial;\n"
                                "  color: #ffffff;\n"
                                "  font-size: 10px;\n"
                                "  padding: 10px 20px 10px 20px;\n"
                                "  text-decoration: none;\n"
                                "}\n"
                                "\n"
                                "QPushButton:hover {\n"
                                "  background: rgb(0, 108, 158);\n"
                                "  text-decoration: none;\n"
                                "}")
        # --------------------------------------------------------------
        getPath = QtGui.QPushButton(optBox)  # Open Path Button
        getPath.setText('Open')
        getPath.setGeometry(305,25,70,20)
        getPath.setStyleSheet("QPushButton {\n"
                                "  background: rgb(0, 77, 113);\n"
                                "  border-radius: 28px;\n"
                                "  font-family: Arial;\n"
                                "  color: #ffffff;\n"
                                "  font-size: 10px;\n"

                                "  text-decoration: none;\n"
                                "}\n"
                                "\n"
                                "QPushButton:hover {\n"
                                "  background: rgb(0, 108, 158);\n"
                                "  text-decoration: none;\n"
                                "}")

        pathLabel = QtGui.QLabel(optBox) #Path Label
        pathLabel.setText('Interpreter:')
        pathLabel.setGeometry(8,30,123,10)
        # --------------------------------------------------------------
        path = QtGui.QPlainTextEdit(optBox) #Path Box
        path.setGeometry(70,25,223,20)
        path.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        # optBox Contents Ends



        def _getPath():
            pypath = None
            ppath = QtGui.QFileDialog.getOpenFileName(pypath, 'Open File', '.exe')
            path.insertPlainText(str(ppath))
            self.pythonPath = path.toPlainText()


        # --------------------------------------------------------------
        QtCore.QObject.connect(getPath, QtCore.SIGNAL(_fromUtf8("clicked()")), _getPath)
        optBox.exec_()
    def _initializeSwide(self):
        import time
        from threading import Thread
        swideEditor = self.swideEditorUi
        swideLexer = QsciLexerPython(sawaIDE)
        swideApi = Qsci.QsciAPIs(swideLexer)
        swideApi.add("def ")
        swideApi.add("as")
        swideApi.add("if")
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
        # the font metrics here will help
        # building the margin width later
        fm = QtGui.QFontMetrics(xfont)
        swideEditor.setMarginWidth(0, fm.width( "00000" ) + 5)
        swideEditor.setMarginLineNumbers(0, True)
        swideEditor.show()
        swideEditor.setText(open("codemodel.py").read())



if __name__ == "__main__":
    import sys
    import thread
    app = QtGui.QApplication(sys.argv)
    sawaIDE = QtGui.QWidget()
    ui = Ui_sawaIDE()
    ui.setupUi(sawaIDE)
    ui._initializeSwide()
    sawaIDE.show()
    sys.exit(app.exec_())

