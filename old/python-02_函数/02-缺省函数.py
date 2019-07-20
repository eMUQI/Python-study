def test(a,b=22,c=33):                   #缺省参数因当放在末尾
    result = a + b + c
    print("%d+%d+%d=%d"%(a,b,c,result))

test(11)
test(1,2)
test(12,c=44)
#test(11,,3) error!
