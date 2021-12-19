import math
import csv
import matplotlib.pyplot as plt
import os

POINT = int(input('point:'))
M1 = int(input('Start point of window'))
M2 = int(input('End point of window'))

#dir for error corrected data
if not os.path.exists('correctedData'):
    os.makedirs('correctedData/data')
#os.mkdir('correctedData')

# finding data files
files = os.listdir('data')
for i,file in enumerate(files):
    files[i] = 'data/' + files[i]


fig, axs = plt.subplots(2)
fig1, axs1 = plt.subplots(2)

def read(fileName):
    with open(fileName, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')

        data = []

        col0 = []
        col1 = []
        for row in reader:
            # split data
            row = row[0].split(',')

            col0.append(float(row[0]))
            col1.append(float(row[1]))

        data.append(col0)
        data.append(col1)

    return data

def findAvg(refdata, data):
    M = [M1, M2]

    w = 0
    for i in range(M[0], M[1]):
        w += data[1][i] - refdata[1][i]

    avg = w/(M[0] - M[1])

    return avg

def doThing():
    REFERENCE = read(files[0])
    avgs = []
    newSets = []

    for file in files:
        if file != files[0]:
            data = read(file)

            avg = findAvg(REFERENCE, data)
            avgs.append(avg)

            newData = []
            for i in data[1]:
                newData.append(i + avg)

            newSets.append(newData)

            toSaveData = data
            toSaveData[1] = newData
            saveNewData(toSaveData, 'correctedData/' + file)

            axs[0].plot(data[0], newData, label = file)

        else:
            data = read(file)
            axs[0].plot(data[0], data[1], label = file)


    print(avgs)
    return newSets

def findstuff(newSets):
    point = POINT
    qqs = [[],[]]

    data = read(files[0])
    qqs[0].append(data[1][point])
    for i in newSets:
        qqs[0].append(i[point])

    # error for no correction
    for file in files:
        data = read(file)
        qqs[1].append(data[1][point])

    print('Corrected values:', qqs[0])
    print('Uncorrected values:', qqs[1])

    axs[1].plot(qqs[0], label = 'with correction')
    axs[1].plot(qqs[1], label = 'no correction')
    axs1[0].plot(qqs[1])

def saveNewData(data, fileName):
    with open(fileName, 'w', newline='') as dataFile:
        writer = csv.writer(dataFile)

        for ii in range(len(data[0])):
            row = []
            for jj in range(len(data)):
                row.append(data[jj][ii])

            writer.writerow(row)


findstuff(doThing())
axs[1].legend()
#axs[0].legend()

plt.show()
