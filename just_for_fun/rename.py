import os

print(os.listdir())
listdirfuck = os.listdir()
if "rename.py" in listdirfuck:
    listdirfuck.remove("rename.py")
for dir in listdirfuck:
    oldname = dir
    breakdir = dir.split("-")
    print(dir)
    print(breakdir)

    if int(breakdir[0]) > 9:
        pass
    else:
        breakdir[0] = "0"+breakdir[0]

    breakbreakdir = breakdir[1].split(".")

    if int(breakbreakdir[0]) > 9:
        pass
    else:
        breakbreakdir[0] = "0"+breakbreakdir[0]

    newname = breakdir[0]+"-"+breakbreakdir[0]+"."+breakbreakdir[1]
    print(newname)
    os.rename(oldname,newname)
