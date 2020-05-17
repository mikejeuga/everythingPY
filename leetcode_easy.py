'''
Just looking at some of the easy Leetcode question to prepare for interview preparation
'''

#Max Sub Array 

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
    