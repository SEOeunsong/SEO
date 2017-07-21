from PySide.QtCore import *
from PySide.QtGui import *
import nukescripts
import collections
import button_gui
reload(button_gui)


class Seo(QDialog, button_gui.Ui_Dialog):
  
    def __init__(self, parent=QApplication.desktop()):
        super(Seo, self).__init__(parent)
        self.setupUi(self)
        
        self.readnode_listView.setSelectionMode(QAbstractItemView.ExtendedSelection)
        readList = []
        allReads = nuke.allNodes('Read')
        for read in allReads:
            readList.append(read['name'].getValue())
        readList.sort()    

        model  = QStandardItemModel(self.readnode_listView)

        for r in readList:
            item = QStandardItem(r)
            model.appendRow(item)

        self.readnode_listView.setModel(model)     
        self.exec_button.clicked.connect(self.listReadOnClick)
        self.exec_button.clicked.connect(self.listSettingOnClick)
        self.exec_button.clicked.connect(self.createSettingNode)

        self.list_setting.setSelectionMode(QAbstractItemView.ExtendedSelection)
        listList = ['RotoPaint','FrameHold','Transform','Tracker','Reformat','ColorCorrect','HueCorrect']
        listList.sort()  

        mod  = QStandardItemModel(self.list_setting)

        for l in listList:
            set = QStandardItem(l)
            mod.appendRow(set)

        self.list_setting.setModel(mod)          

        '''   
        from collections import defaultdict   
        f=defaultdict(list)
        for k,v in d:
            f[k].append[v]
        print f    
        '''

    def listReadOnClick(self):      
        self.nodeList = []     #ReadNodes  data
        nukescripts.clear_selection_recursive()
        selectedReadNode = self.readnode_listView.selectedIndexes()
        for readnode in selectedReadNode:
            nodename = readnode.data()
            self.nodeList.append(nodename)
            #nuke.toNode(nodename).setSelected(True)    
        #self.nodeDic={k:v for v, k in nodeList}   : invert count // dict(enumerate(nodeList))       
                                                   # not only index/key but also index number print
  

    def listSettingOnClick(self):    #Setting Nodes      밸류로 받아서 딕셔너리에 리스트형식으로 넣기
        self.selectedSettingList = []
        self.nodeDic={}

        selectedSettingNode = self.list_setting.selectedIndexes()
        for snode in selectedSettingNode:       
            valueSettingNode = snode.data() 
            self.selectedSettingList.append(valueSettingNode)     # list   values

        for node in self.nodeList:
            self.nodeDic[node] = self.selectedSettingList


       #finalDic.setdefault(key, []).append(date)        
       #v = dict.values(self.dic)[index]

        
    def createSettingNode(self):
        #orderDic = collections.OrderedDict(self.nodeDic) #순서대로 
        #dicKey = self.nodeDic.keys()                                
        #dicValue = self.nodeDic.values()
                                       
        #selectValue = self.selectedSettingList  #setting nodes -> selected value

        #for value in dicValue:
           #makeNode = nuke.createNode(dicKey[])(inputs=[dicKey])
        for key, value in self.nodeDic.items():
            [eval('nuke.nodes.%s()' %x) for x in self.nodeDic[key]]
        
        '''
        for v in self.nodeDic.items():
            makeNode = nuke.createNode("{}".format(v))            

        selectnode = self.readnode_listView.selectedIndexes()[0].data()
        selRead = nuke.toNode(selectnode).setSelected(True) 
    
        b = nuke.selectedNode()
        
        rotoP = nuke.nodes.RotoPaint()
        rotoP.setInput(0,b)
        frameH=nuke.nodes.FrameHold(inputs=[rotoP])     #   = nuke.nodes.dicValue(inputs=[dicKey]))
        transF = nuke.nodes.Transform(inputs=[frameH])
        tracker = nuke.nodes.Tracker(inputs=[transF])
                             
        reFormat = nuke.nodes.Reformat()
        reFormat.setInput(0,b)
        tf= nuke.nodes.Transform(inputs=[reFormat])
        cc = nuke.nodes.ColorCorrect(inputs=[tf])
        hc = nuke.nodes.HueCorrect(inputs=[cc])  
        '''       
                                        
def main():
    window = Seo()
    window.show()

main()


'''
node_list = list(data.values())
      print node_list
'''