from typing import List

def selection_sort(arr: List[int]) -> None:
    """
    Sorts a list of integers in ascending order using the Selection Sort algorithm.

    :param arr: a list of integers to be sorted in place
    """
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Example usage
if __name__ == "__main__":
    A = [64, 25, 12, 22, 11]
    selection_sort(A)
    print("Sorted array:", " ".join(str(x) for x in A))

"""
Example usage:
A = [64, 25, 12, 22, 11]
selection_sort(A)
print("Sorted array:", " ".join(str(x) for x in A))
""" 
