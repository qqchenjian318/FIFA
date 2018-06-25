from DataCenter import DataCenter
from DrawCenter import DrawCenter
from GuiClass import GuiClass

base_path = 'http://cp.360.cn/jczq/?menu'
match_path = 'http://odds.cp.360.cn/jczqdatax/asiaload?cids=&ctype=&match='
# path = match_path + mactch_num
# dataCenter = DataCenter()
# dataCenter.load_menu(base_path,match_path)
# app = DrawCenter()
# app.drawSimple()
app = GuiClass()
app.createWidgets()