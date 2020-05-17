#This is my way into python programming and back-end stuff. 
import sort
import leetcode_easy

the_list = [20, 35, -15, 7, 55, 1, -22]

 
my_pivot = sort.partition(the_list, 0, len(the_list)-1)
sorted_list = sort.quick_sort(the_list, 0, len(the_list)-1)
print(sorted_list)

