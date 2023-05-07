def selection_sort(arr):
    """
    Sorts an array of integers in ascending order using the Selection Sort algorithm.

    :param arr: an array of integers
    :return: None (the array is sorted in place)
    """
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first element		 
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Example usage
A = [64, 25, 12, 22, 11]
selection_sort(A)
print("Sorted array:", " ".join(str(x) for x in A))
