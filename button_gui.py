# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'button20170717.ui'
#
# Created: Wed Jul 19 17:19:44 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(539, 602)
        self.read_gb = QtGui.QGroupBox(Dialog)
        self.read_gb.setGeometry(QtCore.QRect(10, 20, 141, 231))
        self.read_gb.setObjectName("read_gb")
        self.readnode_listView = QtGui.QListView(self.read_gb)
        self.readnode_listView.setGeometry(QtCore.QRect(10, 20, 121, 192))
        self.readnode_listView.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.readnode_listView.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.readnode_listView.setFlow(QtGui.QListView.TopToBottom)
        self.readnode_listView.setObjectName("readnode_listView")
        self.setting_nd = QtGui.QGroupBox(Dialog)
        self.setting_nd.setGeometry(QtCore.QRect(170, 20, 141, 231))
        self.setting_nd.setObjectName("setting_nd")
        self.list_setting = QtGui.QListView(self.setting_nd)
        self.list_setting.setGeometry(QtCore.QRect(10, 20, 121, 192))
        self.list_setting.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.list_setting.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.list_setting.setFlow(QtGui.QListView.TopToBottom)
        self.list_setting.setObjectName("list_setting")
        self.exec_button = QtGui.QPushButton(Dialog)
        self.exec_button.setGeometry(QtCore.QRect(320, 190, 71, 23))
        self.exec_button.setObjectName("exec_button")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.read_gb.setTitle(QtGui.QApplication.translate("Dialog", "Read Nodes", None, QtGui.QApplication.UnicodeUTF8))
        self.setting_nd.setTitle(QtGui.QApplication.translate("Dialog", "Setting Nodes", None, QtGui.QApplication.UnicodeUTF8))
        self.exec_button.setText(QtGui.QApplication.translate("Dialog", "execute", None, QtGui.QApplication.UnicodeUTF8))

