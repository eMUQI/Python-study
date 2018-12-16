class ShortInput(Exception):
    def __init__(self,length,atleast):
        self.length = length
        self.atleast = atleast

def main():
    try:
        s = input('请输入-->')
        if len(s) < 3:
            raise ShortInput(len(s),3)
    except ShortInput as result:
        print("ShortInput:输入的长度是%d,长度至少应是%d"%(result.length,result.atleast))
    else:
        print("无事发生")

main()
