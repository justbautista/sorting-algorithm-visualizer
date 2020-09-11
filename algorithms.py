import time

def bubble_sort(data, drawData):
    for _ in range(len(data)-1):
        for j in range(len(data)-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                drawData(data, ['green' if x == j or x == j+1 else 'red' for x in range(len(data))])
                time.sleep(0.1)

    drawData(data, ['green' for x in range(len(data))])

def merge_sort(data, drawData):
    merge_algo(data, 0, len(data)-1, drawData)

def merge_algo(data, left, right, drawData):
    if left < right:
        middle = (left + right) // 2
        merge_algo(data, left, middle, drawData)
        merge_algo(data, middle+1, right, drawData)
        merge(data, left, middle, right, drawData)

def merge(data, left, middle, right, drawData):
    drawData(data, getColor(len(data), left, middle, right))
    time.sleep(0.1)

    leftPart = data[left:middle+1]
    rightPart = data[middle+1:right+1]

    i = j = 0

    for k in range(left, right+1):
        if i < len(leftPart) and j < len(rightPart):
            if leftPart[i] <= rightPart[j]:
                data[k] = leftPart[i]
                i+=1
            else:
                data[k] = rightPart[j]
                j+=1
        elif i < len(leftPart):
            data[k] = leftPart[i]
            i+=1
        else:
            data[k] = rightPart[j]
            j+=1
    
    drawData(data, ["green" if x >= left and x <= right else "black" for x in range(len(data))])
    time.sleep(0.1)

def getColor(length, left, middle, right):
    colorArray = []

    for i in range(length):
        if left <= i and i <= right:
            if left <= i and i <= middle:
                colorArray.append("yellow")
            else:
                colorArray.append("blue")
        else:
            colorArray.append("black")

    return colorArray





