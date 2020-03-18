#I will try to implement a couple of sort algorithm to get used to python core constructs

def bubbleSort(anUnssortedArray) -> list:
    for lastUnsortedIndex in range(len(anUnssortedArray)-1, -1, -1):
        for j in range(lastUnsortedIndex):
            if anUnssortedArray[j] > anUnssortedArray[j+1]:
                swap(anUnssortedArray, j, j+1)

    return anUnssortedArray



def selectionSort(anUnssortedArray) -> list:
    for lastUnsortedIndex in range(len(anUnssortedArray)-1, -1, -1):
        largestElm = 0
        for i in range(lastUnsortedIndex+1):
            if anUnssortedArray[i] > anUnssortedArray[largestElm]:
                largestElm = i
        swap(anUnssortedArray, largestElm, lastUnsortedIndex)
    
    return anUnssortedArray





def insertionSort(anUnssortedArray) -> list:
    for firstUnorderedIndex in range(1, len(anUnssortedArray)):
        newElm = anUnssortedArray[firstUnorderedIndex]
        i = firstUnorderedIndex-1
        while i >= 0 and anUnssortedArray[i] > newElm:
            anUnssortedArray[i+1] = anUnssortedArray[i]
            i -= 1

        anUnssortedArray[i+1] = newElm

    return anUnssortedArray

def mergeSort():
    pass

def merge():
    pass

def swap(data: list, indexI, indexJ):
    data[indexI], data[indexJ] = data[indexJ] , data[indexI]




def maxSubArray(theArray: [int]) -> int:
    numero = 0
    largest = numero
    for num in range(len(theArray)):
        numero += theArray[num]
        if numero < 0:
            numero = 0
        if numero > largest:
            largest = numero
        
    return largest, numero


