# I will try to implement a couple of sort algorithm to get used to python core constructs

# This is an implementation of the bubbleSort algorithm.

def bubble_sort(anArray: list) -> list:
    for lastUnsortedIndex in range(len(anArray)-1, -1, -1):
        for j in range(lastUnsortedIndex):
            if anArray[j] > anArray[j+1]:
                swap(anArray, j, j+1)

    return anArray

# This is an implementation of the selectionSort algorithm.

def selection_sort(anArray: list) -> list:
    for lastUnsortedIndex in range(len(anArray)-1, -1, -1):
        largestElm = 0
        for i in range(lastUnsortedIndex+1):
            if anArray[i] > anArray[largestElm]:
                largestElm = i
        swap(anArray, largestElm, lastUnsortedIndex)
    
    return anArray


# This is an implementation of the insertionSort algorithm.

def insertion_sort(anArray: list) -> list:
    for firstUnorderedIndex in range(1, len(anArray)):
        newElm = anArray[firstUnorderedIndex]
        i = firstUnorderedIndex-1
        while i >= 0 and anArray[i] > newElm:
            anArray[i+1] = anArray[i]
            i -= 1

        anArray[i+1] = newElm

    return anArray

# This is an implementation of the merge_sort algorithm.

def merge_sort(arr: list)-> list: 
    if len(arr) >1: 
        mid = len(arr)//2 # Finding the mid of the array
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves 
  
        merge_sort(L) # Sorting the first half 
        merge_sort(R) # Sorting the second half 
  
        i = j = k = 0
          
        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
          
        # Checking if any element was left 
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1

            return arr
    

# This is an implementation of the quick_sort.

def quick_sort(anArray: list, start: int, end: int) -> int:
    my_pivot: int = partition(anArray, start, end) 

    if my_pivot-1 > start: 
        quick_sort(anArray, start, my_pivot-1)

    if my_pivot+1 < end: 
        quick_sort(anArray, my_pivot+1, end)

    return anArray
    

# partition gets the pivot for the quicksort function.

def partition(data: list, start: int, end: int) -> int:
    pivot: int = data[end]
    
    for i in range(start, end, 1):  # this should be the equivalent of for(i=start; i < end; i++)
        if data[i] < pivot:
            swap(data, i, start)
            start += 1
        
    swap(data, start, end)

    return start


# Swap function for some of the sort algorithms above

def swap(data: list, indexI, indexJ):
    data[indexI], data[indexJ] = data[indexJ] , data[indexI]


