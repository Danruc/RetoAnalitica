def readFile():
    file = open("avocado.csv","r")
    df=[]
    while True:
        line = file.readline().strip()
        if (len(line)==0):
            break
        else:
            newLine = line.split(",")
            df.append(newLine)
        file.close()

dataframe = readFile()
print(len(dataframe))
print(dataframe[14][1])



