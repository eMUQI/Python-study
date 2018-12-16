try:
    9/0
    open("sad")
    #print(num)
    print("-----1")

except (NameError,FileNotFoundError):
    print("error")

except Exception as e:
    print("other error")
    print(e)

else:
    print("无异常才会输出 了")

finally:
    print("finally")
