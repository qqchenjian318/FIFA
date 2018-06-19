from DataCenter import DataCenter

base_path = 'http://cp.360.cn/jczq/?menu'
match_path = 'http://odds.cp.360.cn/jczqdatax/asiaload?cids=&ctype=&match='
# path = match_path + mactch_num
dataCenter = DataCenter()
dataCenter.load_menu(base_path,match_path)