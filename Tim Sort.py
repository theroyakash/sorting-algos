'''
Tim sort is the most practical sorting algorithm you probably never heard of.
It's not faster that n log(n) [It can't happen] but for the real world data it always
outperforms n log(n) sorting algorithms in runtime.

Let's see how it can be done.

'''

'''
In a nutshell, the main routine marches over the array once, left to right,
alternately identifying the next run, then merging it into the previous
runs "intelligently".  Everything else is complication for speed, and some
hard-won measure of memory efficiency.

'''

# Python3 program to perform TimSort. 
RUN = 32
	
# This function sorts array from left index to 
# to right index which is of size atmost RUN 
def insertionSort(array, left, right): 

	for i in range(left + 1, right+1): 
	
		temporary_var = array[i] 
		j = i - 1
		while array[j] > temporary_var and j >= left: 
		
			array[j+1] = array[j] 
			j -= 1
		
		array[j+1] = temporary_var 
	
# merge function merges the sorted runs 
def merge(array, l, m, r): 

	# original array is broken in two parts 
	# left and right array 
	len1, len2 = m - l + 1, r - m 
	left, right = [], [] 
	for i in range(0, len1): 
		left.append(array[l + i]) 
	for i in range(0, len2): 
		right.append(array[m + 1 + i]) 
	
	i, j, k = 0, 0, l 
	# after comparing, we merge those two array 
	# in larger sub array 
	while i < len1 and j < len2: 
	
		if left[i] <= right[j]: 
			array[k] = left[i] 
			i += 1
		
		else: 
			array[k] = right[j] 
			j += 1
		
		k += 1
	
	# copy remaining elements of left, if any 
	while i < len1: 
	
		array[k] = left[i] 
		k += 1
		i += 1
	
	# copy remaining element of right, if any 
	while j < len2: 
		array[k] = right[j] 
		k += 1
		j += 1
	
# iterative Timsort function to sort the 
# array[0...n-1] (similar to merge sort) 

# Tim Sort
def timSort(array, n): 

	# Sort individual subarrays of size RUN 
	for i in range(0, n, RUN): 
		insertionSort(array, i, min((i+31), (n-1))) 
	
	# start merging from size RUN (or 32). It will merge 
	# to form size 64, then 128, 256 and so on .... 
	size = RUN 
	while size < n: 
	
		# pick starting point of left sub array. We 
		# are going to merge array[left..left+size-1] 
		# and array[left+size, left+2*size-1] 
		# After every merge, we increase left by 2*size 
		for left in range(0, n, 2*size): 
		
			# find ending point of left sub array 
			# mid+1 is starting point of right sub array 
			mid = left + size - 1
			right = min((left + 2*size - 1), (n-1)) 
	
			# merge sub array array[left.....mid] & 
			# array[mid+1....right] 
			merge(array, left, mid, right) 
		
		size = 2*size 
		
# utility function to print the Array 
def printArray(array, n): 

	for i in range(0, n): 
		print(array[i], end = " ") 
	print() 

	
# Driver program to test above function 
if __name__ == "__main__": 

	array = [5, 21, 7, 23, 19] 
	n = len(array) 
	print("Given Array is") 
	printArray(array, n) 
	
	timSort(array, n) 
	
	print("After Sorting Array is") 
	printArray(array, n)