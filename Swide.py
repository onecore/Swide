# -*- coding: utf-8 -*-

__author__ = 'Mark Anthony Pequeras'
__software__ = 'SawaIDE | Python IDE (IDE with Executable Compiler - p2e)'
__year__ = '2013'
__python__ = '2.7'
__version__ = '1.0'
__developers__ = 'CoreSEC Software Development Group'

import sys
from PyQt4.QtGui import QApplication
from PyQt4 import QtCore, QtGui
from PyQt4 import Qsci
from PyQt4.Qsci import QsciScintilla, QsciScintillaBase, QsciLexerPython
from Settings import swideSettings
import ConfigParser
import io
import os
import subprocess
import time

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
        setting = swideSettings
        self.pythonpath = setting.pythonpath
        self.completion = setting.completion
        self.language = setting.language
        self.languagePath = setting.langpath
        self.compiledPath = setting.compiledpath
        self.compiledName = setting.compiledName
        self.version = setting.version
        self.newversion = setting.newversion


# Python Path


    def setupUi(self, sawaIDE):
        sawaIDE.setObjectName(_fromUtf8("sawaIDE"))
        sawaIDE.resize(945, 802)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("swideImages/python-xxl.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        sawaIDE.setWindowIcon(icon)
        sawaIDE.setStyleSheet(_fromUtf8("background: rgb(102, 102, 102);\n"
"color: rgb(245, 245, 245);"))
        self.FileObj = QtGui.QPushButton(sawaIDE)
        self.FileObj.setGeometry(QtCore.QRect(10, 60, 161, 61))
        self.FileObj.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.FileObj.setStyleSheet(_fromUtf8("QPushButton {\n"
"  background: transparent;\n"
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
        self.FileObj.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("swideimages/Actions-filenew-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.FileObj.setIcon(icon1)
        self.FileObj.setIconSize(QtCore.QSize(79, 60))
        self.FileObj.setObjectName(_fromUtf8("FileObj"))
        self.optionsObj = QtGui.QPushButton(sawaIDE)
        self.optionsObj.setGeometry(QtCore.QRect(10, 200, 161, 61))
        self.optionsObj.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.optionsObj.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.optionsObj.setAutoFillBackground(False)
        self.optionsObj.setStyleSheet(_fromUtf8("QPushButton {\n"
"  background: transparent;\n"
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
        self.optionsObj.setInputMethodHints(QtCore.Qt.ImhNone)
        self.optionsObj.setText(_fromUtf8(""))

        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("swideimages/preferences-settings-icone-9030-128.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.optionsObj.setIcon(icon2)
        self.optionsObj.setIconSize(QtCore.QSize(40, 61))
        self.optionsObj.setAutoDefault(False)
        self.optionsObj.setFlat(False)
        self.optionsObj.setObjectName(_fromUtf8("optionsObj"))

        self.consoleDockObj = QtGui.QDockWidget(sawaIDE)
        self.consoleDockObj.setGeometry(QtCore.QRect(10, 630, 921, 161))
        self.consoleDockObj.setFeatures(QtGui.QDockWidget.NoDockWidgetFeatures)
        self.consoleDockObj.setAllowedAreas(QtCore.Qt.NoDockWidgetArea)
        self.consoleDockObj.setObjectName(_fromUtf8("consoleDockObj"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.consoleObj = QtGui.QPlainTextEdit(self.dockWidgetContents)
        self.consoleObj.setGeometry(QtCore.QRect(160, 0, 641, 131))
        self.consoleObj.setObjectName(_fromUtf8("consoleObj"))
        self.consoleObj.setDisabled(1)
        self.consoleObj.setStyleSheet('background: black; color: green;')
        self.clearConsoleObj = QtGui.QPushButton(self.dockWidgetContents)
        self.clearConsoleObj.setGeometry(QtCore.QRect(810, 10, 101, 31))
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
        self.itsSwide_2 = QtGui.QLabel(sawaIDE)
        self.itsSwide_2.setGeometry(QtCore.QRect(380, 280, 231, 61))
        self.itsSwide_2.setStyleSheet(_fromUtf8("background: transparent;"))
        self.itsSwide_2.setText(_fromUtf8(""))
        self.itsSwide_2.setPixmap(QtGui.QPixmap(_fromUtf8("swideimages/LJ5J591388303749.png")))
        self.itsSwide_2.setScaledContents(True)
        self.itsSwide_2.setObjectName(_fromUtf8("itsSwide_2"))
        self.RunCompiledObjBtn2 = QtGui.QPushButton(self.dockWidgetContents)
        self.RunCompiledObjBtn2.setGeometry(QtCore.QRect(810, 80, 101, 51))
        self.RunCompiledObjBtn2.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.RunCompiledObjBtn2.setStyleSheet(_fromUtf8("QPushButton {\n"
"  background:  rgb(103, 129, 30);\n"
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
        self.RunCompiledObjBtn2.setObjectName(_fromUtf8("RunCompiledObjBtn2"))
        self.compileNowObjBtn = QtGui.QPushButton(self.dockWidgetContents)
        self.compileNowObjBtn.setGeometry(QtCore.QRect(810, 40, 101, 41))
        self.compileNowObjBtn.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.compileNowObjBtn.setStyleSheet(_fromUtf8("QPushButton {\n"
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

        self.compileNowObjBtn.setObjectName(_fromUtf8("compileNowObjBtn"))
        self.label_10 = QtGui.QLabel(self.dockWidgetContents)
        self.label_10.setGeometry(QtCore.QRect(820, 96, 21, 21))
        self.label_10.setStyleSheet(_fromUtf8("background: transparent;"))
        self.label_10.setText(_fromUtf8(""))
        self.label_10.setPixmap(QtGui.QPixmap(_fromUtf8("swideimages/right.png")))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(self.dockWidgetContents)
        self.label_11.setGeometry(QtCore.QRect(820, 50, 21, 21))
        self.label_11.setStyleSheet(_fromUtf8("background: transparent;"))
        self.label_11.setText(_fromUtf8(""))
        self.label_11.setPixmap(QtGui.QPixmap(_fromUtf8("swideimages/bv01030 (1).png")))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.InfoObjBox = QtGui.QPlainTextEdit(self.dockWidgetContents)
        self.InfoObjBox.setGeometry(QtCore.QRect(0, 0, 151, 131))
        self.InfoObjBox.setObjectName(_fromUtf8("InfoObjBox"))
        self.consoleDockObj.setWidget(self.dockWidgetContents)
## TABS START
        #1
        self.tab1 = QtGui.QWidget(sawaIDE)
        #2
        self.tab2 = QtGui.QWidget(sawaIDE)
        #3
        self.tab3 = QtGui.QWidget(sawaIDE)
        #4
        self.tab4 = QtGui.QWidget(sawaIDE)
        #5
        self.tab5 = QtGui.QWidget(sawaIDE)

## TABS EMD
        self.fileListObj = QtGui.QTabWidget(sawaIDE)
        self.fileListObj.setGeometry(180,1,760,625)

        self.fileListObj.setStyleSheet('color: black; background: rgb(102, 102, 102); border: none;')
## ADD TABS
        self.fileListObj.addTab(self.tab1, "")


## ADD TABS END
        self.EditorDockObj = QtGui.QDockWidget(self.tab1)
        self.EditorDockObj.setGeometry(QtCore.QRect(0, 4, 741, 591))
        self.EditorDockObj.setAcceptDrops(False)
        self.EditorDockObj.setWindowIcon(icon)
        self.EditorDockObj.setFloating(False)
        self.EditorDockObj.setFeatures(QtGui.QDockWidget.DockWidgetFloatable|QtGui.QDockWidget.DockWidgetMovable|QtGui.QDockWidget.DockWidgetVerticalTitleBar)
        self.EditorDockObj.setAllowedAreas(QtCore.Qt.AllDockWidgetAreas)
        self.EditorDockObj.setObjectName(_fromUtf8("EditorDockObj"))
        self.EditorDockObj.setStyleSheet('color: rgb(245, 245, 245);')
        self.dockWidgetContents_2 = QtGui.QWidget()
        self.dockWidgetContents_2.setObjectName(_fromUtf8("dockWidgetContents_2"))
        self.RunCompiledBtn = QtGui.QPushButton(self.dockWidgetContents_2)
        self.RunCompiledBtn.setGeometry(QtCore.QRect(110, 558, 101, 41))
        self.RunCompiledBtn.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.RunCompiledBtn.setStyleSheet(_fromUtf8("QPushButton {\n"
"  background:  rgb(103, 129, 30);\n"
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
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("swideimages/right.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.RunCompiledBtn.setIcon(icon3)
        self.RunCompiledBtn.setObjectName(_fromUtf8("RunCompiledBtn"))
        self.compileNowObj = QtGui.QPushButton(self.dockWidgetContents_2)
        self.compileNowObj.setGeometry(QtCore.QRect(10, 560, 101, 35))
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
        self.swideEditor = QsciScintilla(self.dockWidgetContents_2)
        self.swideEditor.setGeometry(QtCore.QRect(10, 1, 601, 561))
        self.setUpCompilerObj = QtGui.QPushButton(self.dockWidgetContents_2)
        self.setUpCompilerObj.setGeometry(QtCore.QRect(620, 540, 111, 31))
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
        self.DockObj.setGeometry(QtCore.QRect(620, 510, 111, 31))
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
        self.floatDockObj.setGeometry(QtCore.QRect(620, 480, 111, 31))
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
        self.saveObj.setGeometry(QtCore.QRect(620, 420, 111, 31))
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
        self.saveAsObj.setGeometry(QtCore.QRect(620, 450, 111, 31))
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
        self.saveAsObj.setCheckable(False)
        self.saveAsObj.setAutoDefault(False)
        self.saveAsObj.setDefault(False)
        self.saveAsObj.setFlat(False)
        self.saveAsObj.setObjectName(_fromUtf8("saveAsObj"))
        self.ClassesViewObj = QtGui.QListWidget(self.dockWidgetContents_2)
        self.ClassesViewObj.setGeometry(QtCore.QRect(620, 30, 101, 51))
        self.ClassesViewObj.setStyleSheet(_fromUtf8("border: transparent;"))
        self.ClassesViewObj.setObjectName(_fromUtf8("ClassesViewObj"))
        self.ClassesLabel = QtGui.QLabel(self.dockWidgetContents_2)
        self.ClassesLabel.setGeometry(QtCore.QRect(620, 10, 41, 16))
        self.ClassesLabel.setObjectName(_fromUtf8("ClassesLabel"))
        self.functionsLabel = QtGui.QLabel(self.dockWidgetContents_2)
        self.functionsLabel.setGeometry(QtCore.QRect(620, 90, 41, 16))
        self.functionsLabel.setObjectName(_fromUtf8("functionsLabel"))
        self.FunctionsViewObj = QtGui.QListView(self.dockWidgetContents_2)
        self.FunctionsViewObj.setGeometry(QtCore.QRect(620, 110, 101, 81))
        self.FunctionsViewObj.setStyleSheet(_fromUtf8("border: transparent;"))
        self.FunctionsViewObj.setObjectName(_fromUtf8("FunctionsViewObj"))
        self.variablesObj = QtGui.QLabel(self.dockWidgetContents_2)
        self.variablesObj.setGeometry(QtCore.QRect(620, 200, 41, 16))
        self.variablesObj.setObjectName(_fromUtf8("variablesObj"))
        self.variableListViewObj = QtGui.QListView(self.dockWidgetContents_2)
        self.variableListViewObj.setGeometry(QtCore.QRect(620, 220, 101, 191))
        self.variableListViewObj.setStyleSheet(_fromUtf8("border: transparent;"))
        self.variableListViewObj.setObjectName(_fromUtf8("variableListViewObj"))
        self.label_2 = QtGui.QLabel(self.dockWidgetContents_2)
        self.label_2.setGeometry(QtCore.QRect(630, 430, 16, 16))
        self.label_2.setStyleSheet(_fromUtf8("background: transparent;"))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("swideimages/save-icon.png")))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.dockWidgetContents_2)
        self.label_3.setGeometry(QtCore.QRect(630, 460, 16, 16))
        self.label_3.setStyleSheet(_fromUtf8("background: transparent;"))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8("swideimages/save-icon.png")))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.dockWidgetContents_2)
        self.label_4.setGeometry(QtCore.QRect(630, 490, 16, 16))
        self.label_4.setStyleSheet(_fromUtf8("background: transparent;"))
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setPixmap(QtGui.QPixmap(_fromUtf8("swideimages/python-xxl.png")))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.dockWidgetContents_2)
        self.label_5.setGeometry(QtCore.QRect(630, 520, 16, 16))
        self.label_5.setStyleSheet(_fromUtf8("background: transparent;"))
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setPixmap(QtGui.QPixmap(_fromUtf8("swideimages/python-xxl.png")))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.dockWidgetContents_2)
        self.label_6.setGeometry(QtCore.QRect(630, 550, 16, 16))
        self.label_6.setStyleSheet(_fromUtf8("background: transparent;"))
        self.label_6.setText(_fromUtf8(""))
        self.label_6.setPixmap(QtGui.QPixmap(_fromUtf8("swideimages/python-xxl.png")))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_9 = QtGui.QLabel(self.dockWidgetContents_2)
        self.label_9.setGeometry(QtCore.QRect(20, 569, 16, 16))
        self.label_9.setStyleSheet(_fromUtf8("background: transparent;"))
        self.label_9.setText(_fromUtf8(""))
        self.label_9.setPixmap(QtGui.QPixmap(_fromUtf8("swideimages/bv01030 (1).png")))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName(_fromUtf8("label_9"))

        self.EditorDockObj.setWidget(self.dockWidgetContents_2)

        self.directoryViewObj = QtGui.QListWidget(sawaIDE)
        self.directoryViewObj.setGeometry(QtCore.QRect(10, 331, 161, 291))
        self.directoryViewObj.setObjectName(_fromUtf8("directoryViewObj"))
        self.checkforUpdatesObj = QtGui.QPushButton(sawaIDE)
        self.checkforUpdatesObj.setGeometry(QtCore.QRect(10, 260, 161, 61))
        self.checkforUpdatesObj.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.checkforUpdatesObj.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkforUpdatesObj.setStyleSheet(_fromUtf8("QPushButton {\n"
"  background:transparent;\n"
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
        self.checkforUpdatesObj.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("swideimages/updatePng.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.checkforUpdatesObj.setIcon(icon4)
        self.checkforUpdatesObj.setIconSize(QtCore.QSize(35, 50))
        self.checkforUpdatesObj.setObjectName(_fromUtf8("checkforUpdatesObj"))
        self.newFolderProjectObj = QtGui.QPushButton(sawaIDE)
        self.newFolderProjectObj.setGeometry(QtCore.QRect(10, 130, 161, 71))
        self.newFolderProjectObj.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.newFolderProjectObj.setStyleSheet(_fromUtf8("QPushButton {\n"
"  background: transparent;\n"
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
        self.newFolderProjectObj.setText(_fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("swideimages/Actions-file-open-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.newFolderProjectObj.setIcon(icon5)
        self.newFolderProjectObj.setIconSize(QtCore.QSize(47, 65))
        self.newFolderProjectObj.setObjectName(_fromUtf8("newFolderProjectObj"))

        self.consoleOnly = QtGui.QSlider(self.EditorDockObj)
        self.consoleOnly.setOrientation(QtCore.Qt.Horizontal)
        self.consoleOnly.setMaximum(1) # Console True Patern
        self.consoleOnly.setMinimum(0) # Console False Patern
        self.consoleOnly.setGeometry(408,570,40,15)
        self.consoleOnly.setStyleSheet('background: transparent;')

        self.consoleOnlyLabel = QtGui.QLabel(self.EditorDockObj)
        self.consoleOnlyLabel.setText('Build Only')
        self.consoleOnlyLabel.setGeometry(345,570,50,14)

        self.consoleOnlyLabel = QtGui.QLabel(self.EditorDockObj)
        self.consoleOnlyLabel.setText('Build and Compile')
        self.consoleOnlyLabel.setGeometry(467,570,90,14)
        self.LolaTape = QtGui.QLabel(sawaIDE)
        self.LolaTape.setStyleSheet('background: rgb(102, 102, 102);')
        self.LolaTape.setGeometry(169,620,780,11)

        self.LolaTape1 = QtGui.QLabel(sawaIDE)
        self.LolaTape1.setStyleSheet('background: rgb(102, 102, 102);')
        self.LolaTape1.setGeometry(930,10,13,640)
        self.newTabClue = QtGui.QPlainTextEdit()
        self.newTabClue.insertPlainText('1')
        self.swirdeLogo = QtGui.QLabel(sawaIDE)
        self.swirdeLogo.setGeometry(QtCore.QRect(20, 20, 141, 21))
        self.swirdeLogo.setStyleSheet(_fromUtf8("background: transparent;"))
        self.swirdeLogo.setText(_fromUtf8(""))
        self.swirdeLogo.setPixmap(QtGui.QPixmap(_fromUtf8("swideimages/LJ5J591388303749.png")))
        self.swirdeLogo.setScaledContents(True)
        self.swirdeLogo.setObjectName(_fromUtf8("swirdeLogo"))
        self.retranslateUi(sawaIDE)
        QtCore.QObject.connect(self.optionsObj, QtCore.SIGNAL(_fromUtf8("clicked()")), self._Options)
        QtCore.QObject.connect(self.FileObj, QtCore.SIGNAL(_fromUtf8("clicked()")), self._FileObj)
        QtCore.QObject.connect(self.checkforUpdatesObj, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self._checkUpdate)
        QtCore.QObject.connect(self.newFolderProjectObj, QtCore.SIGNAL(_fromUtf8("clicked()")), self._newProject)
        QtCore.QObject.connect(self.saveObj, QtCore.SIGNAL(_fromUtf8("clicked()")), self._save)
        QtCore.QObject.connect(self.saveAsObj, QtCore.SIGNAL(_fromUtf8("clicked()")), self._saveAs)
        QtCore.QObject.connect(self.floatDockObj, QtCore.SIGNAL(_fromUtf8("clicked()")), self._float)
        QtCore.QObject.connect(self.DockObj, QtCore.SIGNAL(_fromUtf8("clicked()")), self._dock)
        QtCore.QObject.connect(self.setUpCompilerObj, QtCore.SIGNAL(_fromUtf8("clicked()")), self._setUp)
        QtCore.QObject.connect(self.compileNowObj, QtCore.SIGNAL(_fromUtf8("clicked()")), self._compileNow)
        QtCore.QObject.connect(self.clearConsoleObj, QtCore.SIGNAL(_fromUtf8("clicked()")), self._clearOutput)
        QtCore.QObject.connect(self.compileNowObjBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), self._compileNow)
        QtCore.QObject.connect(self.RunCompiledObjBtn2, QtCore.SIGNAL(_fromUtf8("clicked()")), self._runCompiled)
        QtCore.QObject.connect(self.RunCompiledBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), self._runCompiled)
        QtCore.QMetaObject.connectSlotsByName(sawaIDE)

    def retranslateUi(self, sawaIDE):
        sawaIDE.setWindowTitle(_translate("sawaIDE", "Swide | Sawa IDE", None))
        # TABS START
        self.fileListObj.setTabText(self.fileListObj.indexOf(self.tab1), _translate("sawaIDE", "swideBuild.py", None))
        self.fileListObj.setTabText(self.fileListObj.indexOf(self.tab2), _translate("sawaIDE", "Editor 2", None))
        self.fileListObj.setTabText(self.fileListObj.indexOf(self.tab3), _translate("sawaIDE", "Editor 3", None))
        self.fileListObj.setTabText(self.fileListObj.indexOf(self.tab4), _translate("sawaIDE", "Editor 4", None))
        self.fileListObj.setTabText(self.fileListObj.indexOf(self.tab5), _translate("sawaIDE", "Editor 5", None))
        # TABS END
        self.consoleDockObj.setWindowTitle(_translate("sawaIDE", " Interpreter and Information", None))
        self.clearConsoleObj.setText(_translate("sawaIDE", "Clear", None))
        self.RunCompiledObjBtn2.setText(_translate("sawaIDE", "RUN", None))
        self.compileNowObjBtn.setText(_translate("sawaIDE", "   Compile", None))
        self.EditorDockObj.setWindowTitle(_translate("sawaIDE", "  Code View", None))
        self.compileNowObj.setText(_translate("sawaIDE", "   COMPILE", None))
        self.setUpCompilerObj.setText(_translate("sawaIDE", "Set-Up", None))
        self.DockObj.setText(_translate("sawaIDE", "Attach", None))
        self.floatDockObj.setText(_translate("sawaIDE", "Dettach", None))
        self.saveObj.setText(_translate("sawaIDE", "Save", None))
        self.saveAsObj.setText(_translate("sawaIDE", "Save as", None))
        self.ClassesLabel.setText(_translate("sawaIDE", "Classes", None))
        self.functionsLabel.setText(_translate("sawaIDE", "Functions", None))
        self.variablesObj.setText(_translate("sawaIDE", "Variables", None))
        self.RunCompiledBtn.setText(_translate("sawaIDE", "RUN", None))

################################################## START   ###################################################################
##############################################################################################################################

    # Trigger when in need Start
    def _askForSetupfile(self):
        dialog = QtGui.QDialog(sawaIDE)
        dialog.setMaximumHeight(500), dialog.setMaximumWidth(500)


        dialog.exec_()
    def _askForInterpreter(self):
        """
        Ask for Interpreter ;)
        """
        dialog = QtGui.QDialog(sawaIDE)
        dialog.setWindowTitle('Python Path Please')
        dialog.setMaximumHeight(123)
        dialog.setMaximumWidth(300)
        dialog.setStyleSheet('background: grey;')
        get = QtGui.QPushButton(dialog)
        get.setGeometry(202,25,89,25)
        get.setText('Open and Save')
        get.setStyleSheet('background: orange; color: white;')
        pathbox = QtGui.QPlainTextEdit(dialog)
        pathbox.setGeometry(10,25,195,25)
        pathbox.setStyleSheet('color: white;')
        run = 0
        pfile = self.pythonpath
        settings = open(str(pfile),'w+')
        def getNow():
            pypath = None
            ppath = QtGui.QFileDialog.getOpenFileName(pypath, 'Open File', '.exe')
            if 'python' not in str(ppath):
                self.InfoObjBox.appendHtml('<font color=\'red\'><br><b>[error] Python Executable is what i need!</b></font><br>')
                settings.close(), dialog.close()
                return 0
            else:
                pathbox.insertPlainText(str(ppath))
                settings.write(str(ppath))
                self.InfoObjBox.appendHtml('<font color=\'white\'><br><b>[Success] Python Path Successfully Added!</b></font><br>')
                settings.close(), dialog.close()
        QtCore.QObject.connect(get, QtCore.SIGNAL(_fromUtf8("clicked()")), getNow)
        dialog.exec_()
    # Trigger when in need End
###############################################      END   ###################################################################
##############################################################################################################################


    def _Options(self):
        self._askForInterpreter()


    def _FileObj(self):
        dialog = QtGui.QDialog(sawaIDE)
        namelabel = QtGui.QLabel(dialog)
        namelabel.setText('File Name:')
        dialog.setWindowTitle('Swide New file')
        namelabel.setGeometry(10,10,50,50)
        name = QtGui.QPlainTextEdit(dialog)
        name.setGeometry(70,25,200,20)
        name.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        saveButton = QtGui.QPushButton(dialog)
        saveButton.setGeometry(270,25,40,20)
        saveButton.setText('Start')
        saveButton.setStyleSheet('background: orange; color: grey;')
        currentTab = self.newTabClue.toPlainText()

        projectRoot = 'Settings/projects/'

        def saveAll():
            ####### CONTINUE
            self.directoryViewObj.addItem(name.toPlainText())
            fileName = name.toPlainText()
            tab = self.tab1
            dialog.close()

            try:
                if '.py' in str(fileName):
                    self.fileListObj.addTab(tab, QtCore.QString(fileName))
                    codemod = open('codemodel.py','r').read()
                    self.swideEditor.clear(),self.swideEditor.append(codemod)
                    dialog.close()
                    return False

                elif '.py' not in str(fileName):
                    self.fileListObj.addTab(tab, QtCore.QString(fileName+'.py'))
                    codemod = open('codemodel.py','r').read()
                    self.swideEditor.clear(),self.swideEditor.append(codemod)
                    dialog.close()

                elif len(fileName) == 0:
                    self.InfoObjBox.appendHtml('<font color=\'red\'><br><b>[error] I need a Name!!</b></font><br>')
                    dialog.close()
            finally:
                dialog.close()
        QtCore.QObject.connect(saveButton, QtCore.SIGNAL('clicked()'), saveAll)
        dialog.exec_()
    def _checkUpdate(self):
        """
        Check for Updates Function
        """
        version = self.version
        newversion = self.newversion
        if float(newversion) > float(version):
            self.InfoObjBox.insertPlainText('Please Updater your Swide!')

    def loadProject(self):
        old = open('Settings/projects/old.swide')
        oldRead = old.read()

    def _newProject(self):
        """
        Load New File
        """
        dialog = QtGui.QDialog(sawaIDE)
        dialog.setWindowTitle('Load File')
        dialog.setMaximumHeight(123)
        dialog.setMaximumWidth(300)
        dialog.setStyleSheet('background: grey;')
        get = QtGui.QPushButton(dialog)
        get.setGeometry(202,25,89,25)
        get.setText('Load')
        get.setStyleSheet('background: orange; color: white;')
        pathbox = QtGui.QPlainTextEdit(dialog)
        pathbox.setGeometry(10,25,195,25)
        pathbox.setStyleSheet('color: white;')
        run = 0
        pfile = self.pythonpath
        settings = open(str(pfile),'w+')
        def getNow():
            pypath = None
            ppath = QtGui.QFileDialog.getOpenFileName(pypath, 'Open File', '.py')
            source = open(str(ppath),'r')
            code = source.read()
            self.swideEditor.clear(), self.swideEditor.append(code)
            dialog.close()
        QtCore.QObject.connect(get, QtCore.SIGNAL(_fromUtf8("clicked()")), getNow)
        dialog.exec_()

    def _save(self):
        mainFile = open('swideBuild.py','w+')
        source = self.swideEditor.text()
        mainFile.write(source)
        mainFile.close()
        self.InfoObjBox.appendHtml('<b>swideBuild.py  Saved!</b>')
    def _saveAs(self):

        pypath = None
        ppath = QtGui.QFileDialog.getSaveFileName(pypath, 'swideBuild.py', '.exe')
    def _float(self):
        self.EditorDockObj.setFloating(1)
    def _dock(self):
        """
        I am the Docker
        """
        self.EditorDockObj.setFloating(0)
        self.EditorDockObj.setGeometry(QtCore.QRect(0, 4, 741, 591))
    def _setUp(self):
        dialog = QtGui.QDialog(sawaIDE)
        dialog.setWindowTitle('Edit Setup File | Exe Compiler')
        dialog.setMaximumWidth(600)
        dialog.setMinimumHeight(500)
        dialog.setMaximumHeight(500)
        dialog.setMinimumWidth(600)

        cusbutton = QtGui.QPushButton(dialog)
        cusbutton.setText('Edit Custom')
        cusbutton.setGeometry(110,20,90,40)
        cusbutton.setStyleSheet('background: orange; color: black;')

        defbutton = QtGui.QPushButton(dialog)
        defbutton.setText('Edit Default')
        defbutton.setGeometry(10,20,90,40)
        defbutton.setStyleSheet('background: orange; color: black;')

        savbutton = QtGui.QPushButton(dialog)
        savbutton.setText('Save Current')
        savbutton.setGeometry(493,20,90,40)
        savbutton.setStyleSheet('background: orange; color: black;')

        pattern = QtGui.QLabel(dialog)

        setupBox = QtGui.QPlainTextEdit(dialog)
        setupBox.setGeometry(10,70,574,400)

        def loadCustom(): #custom
            pattern.setText('1')
            custom = open('Settings/swidefiles/setup/custom.swide','r+')
            readc = custom.read()
            setupBox.clear(), setupBox.insertPlainText(str(readc))
            custom.close()

        def loadDefault(): #default
            pattern.setText('0')
            custom = open('Settings/swidefiles/setup/default.swide','r+')
            readc = custom.read()
            setupBox.clear(), setupBox.insertPlainText(str(readc))
            custom.close()
        def saveAll(): #save all
            source = setupBox.toPlainText()
            where2save = pattern.text()
            if where2save == '1':
                openCustom = open('Settings/swidefiles/setup/custom.swide','w+')
                openCustom.write(str(source))
                openCustom.close()

            if where2save == '0':
                openDef = open('Settings/swidefiles/setup/default.swide','w+')
                openDef.write(str(source))
                openDef.close()


        QtCore.QObject.connect(savbutton, QtCore.SIGNAL('clicked()'), saveAll)
        QtCore.QObject.connect(defbutton, QtCore.SIGNAL('clicked()'), loadDefault)
        QtCore.QObject.connect(cusbutton, QtCore.SIGNAL('clicked()'), loadCustom)


        dialog.exec_()




    def _clearOutput(self):
        self.consoleObj.clear(), self.InfoObjBox.clear()

    def _showProjects(self):
        lists = os.system('cd Settings/projects/folders && dir')
        leftObj = self.directoryViewObj
        #for folders in lists:
        #    print folders


    def _initializeSwide(self):
        import time
        from threading import Thread
        from Settings import completions
        from Settings.projects import path
        import os
        def check():
            fileCon = open('buildPath.swide','r').read()
            if 'swideCompiled' in str(fileCon):
                pass
            else:
                userhome = os.path.expanduser('~')
                desktop = userhome + '/Desktop/swideCompiled'
                writePath = open('buildPath.swide','w').write(desktop)
                writeFolder = os.system('cd {home} && mkdir swideCompiled'.format(home=desktop))
        check()
        """
        Initialize Swide Scintilla Function
        """

        swideEditor = self.swideEditor
        swideEditor.setAutoFillBackground(True)
        swideEditor.setCallTipsVisible(Qsci.QsciScintilla.CallTipsContext)
        swideEditor.setCallTipsVisible(1)
        swideLexer = QsciLexerPython(sawaIDE)
        swideApi = Qsci.QsciAPIs(swideLexer)
        swideLexer.setAutoIndentStyle(1)

        for string in completions.strings:
            swideApi.add(string) # Add all of the Strings in a Completions file
        swideApi.prepare()
        swideEditor.setLexer(swideLexer)
        swideEditor.setAutoCompletionThreshold(2)
        swideEditor.setAutoIndent(True)
        swideEditor.setIndentationGuides(True)
        swideEditor.setBackspaceUnindents(True)
        swideEditor.setIndentationsUseTabs(True)
        swideEditor.setTabWidth(4)
        swideEditor.setAutoCompletionSource(QsciScintilla.AcsAPIs)
        swideEditor.setCaretLineVisible(True)
        swideEditor.setCaretLineBackgroundColor(QtGui.QColor("#DCDCDC"))
        swideEditor.setCaretForegroundColor(QtGui.QColor("green"))
        swideEditor.setEdgeMode(QsciScintilla.EdgeLine)
        swideEditor.setEdgeColumn(98)
        swideEditor.setFolding(QsciScintilla.CircledTreeFoldStyle)
        swideEditor.setBraceMatching(QsciScintilla.SloppyBraceMatch)
        swideEditor.setEdgeColor(QtGui.QColor("#FF0000"))
        #swideEditor.setMarginsBackgroundColor(QtGui.QColor("#333333"))
        #swideEditor.setMarginsForegroundColor(QtGui.QColor("#CCCCCC"))
        swideEditor.show()
        swideEditor.setText(open("codemodel.py").read())  # Load Codemodel File (File Skeleton)
        swideEditor.setMarginSensitivity(1, True)
        swideEditor.SendScintilla(QsciScintilla.SCI_SETHSCROLLBAR, 0)
        swideEditor.SendScintilla(QsciScintilla.STYLE_DEFAULT,QsciScintilla.SCI_STYLERESETDEFAULT,QsciScintilla.SCI_STYLESETBACK)
        #swideEditor.SendScintilla(QsciScintilla.SC_ALPHA_TRANSPARENT)

        #self.fileDialog = QtGui.QFileDialog(sawaIDE)
        #self.fileDialog.show()



    def swideOutput(self):
        self.consoleObj.insertPlainText(' >>  '+ str(QtCore.QString(self.proc.readAllStandardOutput())))

    def _runCompiled(self):
        """
        Run 'Build' or 'Build + EXE' ;)
        """
        self.consoleObj.setDisabled(1)
        toRun = self.compiledName
        RunPath = self.compiledPath
        interpreter = self.pythonpath
        python = open(interpreter,'r+')
        swideinterpreter = python.read() #dont forget to close it ;)

        source = self.swideEditor.text()
        cachebuild = 'swideBuild.py'
        with open(cachebuild,'w+') as cacheFile:
            cacheFile.write(str(source))
            cacheFile.close()

        if self.consoleOnly.value() == 0:   #Build Only
            if 'python' not in self.pythonpath:
                self.InfoObjBox.appendHtml('<font color=\'white\'><br><b>[Error] Path isn\'t setup properly!</b></font><br>')
            if len(self.pythonpath) < 3:
                self.InfoObjBox.appendHtml('<font color=\'white\'><br><b>[Error] Path isn\'t setup properly!</b></font><br>')

            else:
                self.consoleObj.clear()
                self.consoleObj.insertPlainText('Interpreter Started...\n')
                self.consoleObj.setDisabled(1)
                self.proc = QtCore.QProcess()
                compileMe = "{python} {cache}".format(python=swideinterpreter, cache=cachebuild)
                python.close()
                self.proc.start(compileMe)
                self.proc.setProcessChannelMode(QtCore.QProcess.MergedChannels);
                QtCore.QObject.connect(self.proc, QtCore.SIGNAL("readyReadStandardOutput()"), self.swideOutput)
                QtCore.QObject.connect(self.proc, QtCore.SIGNAL("readyReadStandardError()"), self.swideOutput)


        if self.consoleOnly.value() == 1:   #Build with Compile
            try:
                os.system('START dist/swideBuild.exe')
            except:
                self.consoleObj.insertPlainText('Theres No Compiled to run!')
            #self.consoleObj.clear(), self.consoleObj.insertPlainText("""
#Please Use the \'Compile\' button to Compile the codes into Executable then Run me!\n
#--> COMPILE
#------> CODES to EXE
#--> RUN
#------> RUN COMPILED EXE
#""")


    def _compileNow(self):
        """
        Run 'Build' or 'Build + EXE' ;)
        """



        toRun = self.compiledName
        RunPath = self.compiledPath
        interpreter = self.pythonpath
        python = open(interpreter,'r+')
        swideinterpreter = python.read() #dont forget to close it ;)

        source = self.swideEditor.text()
        cachebuild = 'swideBuild.py'
        with open(cachebuild,'w+') as cacheFile:
            cacheFile.write(str(source))
            cacheFile.close()

        if self.consoleOnly.value() == 0:   #Build Only
            if 'python' not in self.pythonpath:
                self.InfoObjBox.appendHtml('<font color=\'white\'><br><b>[Error] Path isn\'t setup properly!</b></font><br>')
            if len(self.pythonpath) < 3:
                self.InfoObjBox.appendHtml('<font color=\'white\'><br><b>[Error] Path isn\'t setup properly!</b></font><br>')

            else:
                self.consoleObj.clear()
                self.consoleObj.insertPlainText('Interpreter Started...\n')
                self.proc = QtCore.QProcess()
                compileMe = "{python} {cache}".format(python=swideinterpreter, cache=cachebuild)
                python.close()
                self.proc.start(compileMe)
                self.proc.setProcessChannelMode(QtCore.QProcess.MergedChannels);
                QtCore.QObject.connect(self.proc, QtCore.SIGNAL("readyReadStandardOutput()"), self.swideOutput)
                QtCore.QObject.connect(self.proc, QtCore.SIGNAL("readyReadStandardError()"), self.swideOutput)


        if self.consoleOnly.value() == 1:   #Build with Compile
            setupOpen = open('Settings/swidefiles/setup.swide','r+')
            setupRead = setupOpen.read()
            self.consoleObj.setEnabled(1)
            if 'python' not in self.pythonpath:
                self.InfoObjBox.appendHtml('<font color=\'white\'><br><b>[Error] Path isn\'t setup properly!</b></font><br>')
            if len(self.pythonpath) < 3:
                self.InfoObjBox.appendHtml('<font color=\'white\'><br><b>[Error] Path isn\'t setup properly!</b></font><br>')

            else:
                setupFile = '0'
                if setupRead == '0': #default
                    setupOpen.close()
                    default = open('Settings/swidefiles/setup/default.swide','r+').read()
                    toSetup = open('swideSetup.py','w+')
                    setupFinal = toSetup.write(default)
                    toSetup.close()
                    setupFile = 'swideSetup.py'

                if setupRead == '1':
                    setupOpen.close()
                    default = open('Settings/swidefiles/setup/custom.swide','r+').read()
                    toSetup = open('swideSetup.py','w+')
                    setupFinal = toSetup.write(default)
                    toSetup.close()
                    setupFile = 'swideSetup.py'
                write2Build = open('swideBuild.py','w+')
                finalSource = write2Build.write(str(self.swideEditor.text()))
                write2Build.close()
                self.consoleObj.clear()
                self.consoleObj.insertPlainText("""
Make sure that you have Py2Exe Installed and the right Py2Exe Setup File!
Now Compiling...\n""")
                self.proc = QtCore.QProcess()
                compileMe = "{python} {setup} py2exe".format(python=swideinterpreter, setup=setupFile)
                python.close()
                self.proc.start(compileMe)
                self.proc.setProcessChannelMode(QtCore.QProcess.MergedChannels);
                QtCore.QObject.connect(self.proc, QtCore.SIGNAL("readyReadStandardOutput()"), self.swideOutput)
                QtCore.QObject.connect(self.proc, QtCore.SIGNAL("readyReadStandardError()"), self.swideOutput)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    sawaIDE = QtGui.QWidget()
    ui = Ui_sawaIDE()
    ui.setupUi(sawaIDE)
    ui._initializeSwide()
    sawaIDE.show()
    sys.exit(app.exec_())

