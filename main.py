#This is my way into python programming and back-end stuff. 
import sort
import leetcode_easy

theArray = [20, 35, -15, 7, 55, 1, -22]
theList = [-2,1,-3,4,-1,2,1,-5,4]
'''        
sortedArray = sort.insertionSort(theArray)
print(sortedArray)
'''

maxSubArray = leetcode_easy.maxSubArray(theArray)
maxSubList = leetcode_easy.maxSubArray(theList)

print(maxSubArray)
print(maxSubList)

