import csv

 
def readMyFile(filename):
    d={}
    header = []
    values = []
    time = []
    emotion = []
 
    with open(filename) as csvDataFile:
        csvReader = csv.DictReader(csvDataFile)
        for row in csvReader:
            for column, value in row.iteritems():
                d.setdefault(column, []).append(value)

            
            
    
    header = d.keys()
    values = d.values()
    time = values[1]
    emotion = values[0]
    print(time)
    print(len(time))

    print(emotion)
    print(len(emotion))
    print("This is the end of the file") 
    return time, emotion
 
 
time,emotion = readMyFile('dataAudio.csv')
time2,emotion2 = readMyFile('dataVisual.csv')
writeArr = []

for i in range(0,len(time)): 
    emoM = (float(emotion[i])+float(emotion2[i]))/2
    tempArr = [time[i],emoM]
    writeArr.append(tempArr)


myFile = open('dataset.csv', 'w')
print(writeArr)

with myFile:
    writer = csv.writer(myFile,lineterminator='\n')
    writer.writerow(["time","emotion"])
    writer.writerows(writeArr)

