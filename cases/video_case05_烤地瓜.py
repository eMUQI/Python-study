class SweetPotato:

    def __init__(self):
        
        self.cookedString = "生"
        self.cookedLevel = 0
    
    def __str__(self):
        return "地瓜状态:%s(%d)"%(self.cookedString,self.cookedLevel)

    def cook(self,cooktime):
        self.cookedLevel += cooktime

        if self.cookedLevel>=0 and self.cookedLevel<3:
            self.cookedString = "生的"
        elif self.cookedLevel>=3 and self.cookedLevel<5:
            self.cookedString= "半生不熟"
        elif self.cookedLevel>=5 and self.cookedLevel<8:
            self.cookedString = "熟了"
        elif self.cookedLevel>=8:
            self.cookedString = "烤糊了"
            

digua = SweetPotato()
digua.cook(1)
print(digua)
digua.cook(1)
print(digua)
digua.cook(1)
print(digua)
digua.cook(1)
print(digua)
digua.cook(1)
print(digua)
digua.cook(1)
print(digua)
digua.cook(1)
print(digua)
digua.cook(1)
print(digua)
digua.cook(1)
print(digua)
digua.cook(1)
print(digua)
            
