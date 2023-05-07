def bubblesort(array): 
    n = len(array) 
    for i in range(n): 
        for j in range(0, n-i-1):  
            if array[j] > array[j+1] : 
                array[j], array[j+1] = array[j+1], array[j] 

# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90] 
bubblesort(arr) 
print("Sorted array is:", arr)
