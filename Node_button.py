'''
author : seo eun song, kim kang min
email  : ekwjd6307@naver.com ,kangmin_kim@mofac-alfred.com
'''

import sys, collections
from PySide.QtCore import *
from PySide.QtGui import *
import nukescripts
import button_gui
reload(button_gui)

class Seo(QDialog, button_gui.Ui_Dialog):
    def __init__(self, parent=QApplication.desktop()):
        super(Seo, self).__init__(parent)
        self.setupUi(self)
        
        self.readnode_listView.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.list_setting.setSelectionMode(QAbstractItemView.ExtendedSelection)

        readList = []
        listList = ['RotoPaint','FrameHold','Transform','Tracker','Reformat','ColorCorrect','HueCorrect']

        allReads = nuke.allNodes('Read')
        for read in allReads:
            readList.append(read['name'].getValue())
        readList.sort(key=lambda x: int(x[4:]))

        model  = QStandardItemModel(self.readnode_listView)
        for r in readList:
            item = QStandardItem(r)
            model.appendRow(item)

        mod  = QStandardItemModel(self.list_setting)
        for l in listList:
            set = QStandardItem(l)
            mod.appendRow(set)
        self.list_setting.setModel(mod)          

        self.readnode_listView.setModel(model)     
        self.exec_button.clicked.connect(self.createSettingNode)
        self.del_button.clicked.connect(self.deleteSettingNode)


    def createSettingNode(self):
        nukescripts.clear_selection_recursive()
        read_node = []
        node_created = []
        create_dic = {}
        self.extendList = []

        selectedReadNode = self.readnode_listView.selectedIndexes()
        for readnode in selectedReadNode:
            nodename = readnode.data()
            read_node.append(nodename)

        selectedSettingNode = self.list_setting.selectedIndexes()
        for snode in selectedSettingNode:      
        # FrameHold, RotoPaint 를 0FrameHold, 3RotoPaint 와 같이 스트링을 만들어 node_created 리스트에 append     
            node_created.append("{0}_{1}".format(snode.row(), snode.data()))
       
        # node_created  비교 후 정렬
        node_created.sort(key=lambda x: int(x[0:1]))   

        # create_dic를 orderedDict 형태로 바꾼뒤 키, 밸류 값을 집어넣을것     
        for num, data in enumerate(read_node, 0):    
            create_dic[data] = node_created
            create_dic = collections.OrderedDict(sorted(create_dic.items(), key=lambda x: x[0]))

        for key, value in create_dic.items():
            readNode = nuke.toNode(key)

            createdNode = [eval('nuke.nodes.%s()' %x[2:]) for x in create_dic[key]] 
            self.extendList.extend(createdNode)

            for num, data in enumerate(createdNode, 0):
                if num == 0:
                    createdNode[num].setInput(0, readNode)
                else: 
                    createdNode[num].setInput(0, createdNode[num-1])
   

    def deleteSettingNode(self):
        for deleteNode in self.extendList:
            nuke.delete(deleteNode)


                    
def main():
    window = Seo()
    window.show()

main()