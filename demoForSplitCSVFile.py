

fo = open("D:\WORK\BootCamp\Python\LearnPython\DemoFile.csv", "r")
for line in fo:
    data=line.split(",")
    #print(data)
    if(data[2].find("Soltero")):
        print(line)




