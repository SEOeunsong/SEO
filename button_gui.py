# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'button20170717.ui'
#
# Created: Fri Jul 28 16:14:46 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(311, 287)
        self.read_gb = QtGui.QGroupBox(Dialog)
        self.read_gb.setGeometry(QtCore.QRect(10, 20, 131, 231))
        self.read_gb.setObjectName("read_gb")
        self.readnode_listView = QtGui.QListView(self.read_gb)
        self.readnode_listView.setGeometry(QtCore.QRect(10, 20, 111, 192))
        self.readnode_listView.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.readnode_listView.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.readnode_listView.setFlow(QtGui.QListView.TopToBottom)
        self.readnode_listView.setObjectName("readnode_listView")
        self.setting_nd = QtGui.QGroupBox(Dialog)
        self.setting_nd.setGeometry(QtCore.QRect(170, 20, 131, 231))
        self.setting_nd.setObjectName("setting_nd")
        self.list_setting = QtGui.QListView(self.setting_nd)
        self.list_setting.setGeometry(QtCore.QRect(10, 20, 111, 192))
        self.list_setting.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.list_setting.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.list_setting.setFlow(QtGui.QListView.TopToBottom)
        self.list_setting.setObjectName("list_setting")
        self.up_btn = QtGui.QPushButton(self.setting_nd)
        self.up_btn.setGeometry(QtCore.QRect(30, 200, 31, 23))
        self.up_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/up_arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.up_btn.setIcon(icon)
        self.up_btn.setObjectName("up_btn")
        self.down_btn = QtGui.QPushButton(self.setting_nd)
        self.down_btn.setGeometry(QtCore.QRect(70, 200, 31, 23))
        self.down_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/down_arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.down_btn.setIcon(icon1)
        self.down_btn.setObjectName("down_btn")
        self.exec_button = QtGui.QPushButton(Dialog)
        self.exec_button.setGeometry(QtCore.QRect(80, 260, 71, 23))
        self.exec_button.setObjectName("exec_button")
        self.del_button = QtGui.QPushButton(Dialog)
        self.del_button.setGeometry(QtCore.QRect(160, 260, 71, 23))
        self.del_button.setObjectName("del_button")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.read_gb.setTitle(QtGui.QApplication.translate("Dialog", "Read Nodes", None, QtGui.QApplication.UnicodeUTF8))
        self.setting_nd.setTitle(QtGui.QApplication.translate("Dialog", "Setting Nodes", None, QtGui.QApplication.UnicodeUTF8))
        self.exec_button.setText(QtGui.QApplication.translate("Dialog", "create", None, QtGui.QApplication.UnicodeUTF8))
        self.del_button.setText(QtGui.QApplication.translate("Dialog", "delete", None, QtGui.QApplication.UnicodeUTF8))

