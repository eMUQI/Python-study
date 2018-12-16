class Home:
    def __init__(self,new_area,new_info,new_addr):
        self.area = new_area
        self.info = new_info
        self.addr = new_addr
        self.left_area = new_area
    def __str__(self):
        return "房子的面积是：%d，可用面积是%d，户型是：%s，地址是%s"%(self.area,self.left_area,self.info,self.addr)

    def add_item(self,item):
        self.left_area -= item.area
class Bed:
    def __init__(self,new_name,new_area):
        self.name = new_name
        self.area = new_area
    
    def __str__(self):
        return "%s占用面积%d"%(self.name,self.area)


fangzi = Home(180,"n室n厅",'xx市 xx xx xxx')
print(fangzi)

bed1 = Bed("大床",4)
print(bed1)

fangzi.add_item(bed1)
print(fangzi)
