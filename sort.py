#I will try to implement a couple of sort algorithm to get used to python core constructs

#This is an implementation of the bubblesort algorithm.

def bubbleSort(anUnssortedArray) -> list:
    for lastUnsortedIndex in range(len(anUnssortedArray)-1, -1, -1):
        for j in range(lastUnsortedIndex):
            if anUnssortedArray[j] > anUnssortedArray[j+1]:
                swap(anUnssortedArray, j, j+1)

    return anUnssortedArray

#This is an implementation of the selectionsort algorithm.

def selectionSort(anUnssortedArray) -> list:
    for lastUnsortedIndex in range(len(anUnssortedArray)-1, -1, -1):
        largestElm = 0
        for i in range(lastUnsortedIndex+1):
            if anUnssortedArray[i] > anUnssortedArray[largestElm]:
                largestElm = i
        swap(anUnssortedArray, largestElm, lastUnsortedIndex)
    
    return anUnssortedArray


#This is an implementation of the insertionsort algorithm.

def insertionSort(anUnssortedArray) -> list:
    for firstUnorderedIndex in range(1, len(anUnssortedArray)):
        newElm = anUnssortedArray[firstUnorderedIndex]
        i = firstUnorderedIndex-1
        while i >= 0 and anUnssortedArray[i] > newElm:
            anUnssortedArray[i+1] = anUnssortedArray[i]
            i -= 1

        anUnssortedArray[i+1] = newElm

    return anUnssortedArray

#This is an implementation of the insertionsort algorithm.

def mergeSort():
    pass

#merge function needed for the implementation of quicksort.

def merge():
    pass

#Swap function for some of the sort algorithms above

def swap(data: list, indexI, indexJ):
    data[indexI], data[indexJ] = data[indexJ] , data[indexI]
