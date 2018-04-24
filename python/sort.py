from common import swap

""" Functions Map """
def sortingAlgorithms():
    return [
        ('Bubble Sort',    'bubbleSort'),
        ('Selection Sort', 'selectionSort'),
        ('Insertion Sort', 'insertionSort'),
        ('Merge Sort',     'mergeSort'),
        ('Quick Sort',     'quickSort'),
        ('Head Sort',      'headSort')
    ]

""" Bubble Sort """
def bubbleSort(array):
    for i in range(len(array)-1,0,-1):
        for j in range(i):
            if array[j] > array[j+1]:
                swap(array,j,j+1)

""" Selection Sort """
def selectionSort(array):
    for i in range(len(array)-1,0,-1):
        min = 0
        for j in range(1,i+1):
            if array[j] > array[min]:
                min = j
        if min != i:
            swap(array,min,i)

""" Insertion Sort """
def insertionSort(array):
    for i in range(len(array)):
        index = array[i]
        j = i
        while (j > 0) and (array[j-1] > index):
            array[j] = array[j-1]
            j -= 1
        array[j] = index

""" Merge Sort """
def mergeSort(array):
    if len(array) > 1:
        mid = len(array) // 2
        lefthalf = array[:mid]
        righthalf = array[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = j = k = 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                array[k] = lefthalf[i]
                i += 1
            else:
                array[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            array[k] = lefthalf[i]
            i = i+1
            k = k+1

        while j < len(righthalf):
            array[k] = righthalf[j]
            j = j+1
            k = k+1

""" Quick Sort """
def quickSort(array):
    quickSortHelper(array, 0, len(array)-1)

def quickSortHelper(array, first, last):
    if first < last:
        splitpoint = partition(array, first, last)
        quickSortHelper(array, first, splitpoint-1)
        quickSortHelper(array, splitpoint+1, last)

def partition(array, first, last):
    pivotValue = array[first]
    leftMark = first+1
    rightMark = last
    done = False

    while not done:
        while leftMark <= rightMark and array[leftMark] <= pivotValue:
            leftMark += 1

        while array[rightMark] >= pivotValue and rightMark >= leftMark:
            rightMark -= 1

        if rightMark < leftMark:
            done = True
        else:
            swap(array, leftMark, rightMark)

    swap(array, first, rightMark)

    return rightMark

""" Heap Sort """
def headSort(array):
    length = len(array)-1
    leastParent = length/2

    for i in range (leastParent, -1, -1):
        moveDown(array, i, length)

    for i in range(length, 0, -1):
        if array[0] > array[i]:
            swap(array, 0, i)
            moveDown(array, 0, i-1)

def moveDown(array, first, last):
    largest = 2*first+1

    while largest <= last:
        if (largest < last) and (array[largest] < array[largest+1]):
            largest += 1
        if array[largest] > array[first]:
            swap(array, largest, first)
            first = largest
            largest = 2*first+1
        else:
            return
