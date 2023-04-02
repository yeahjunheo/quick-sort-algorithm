# Just a basic function to swap elements
def Swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

# Sort out elements to the left or right of a pivot point 
def Partition(a, start, end):
    
    # Arbitrarily set the pivot as the last element of the list
    pivot = a[end]
    
    # Set the pivot index as the start as a tracer
    pIndex = start
    
    # A for-loop to compare all elements in list a while comparing with the pivot. 
    for i in range(start, end):
        if a[i] <= pivot:
            Swap(a, i, pIndex)
            pIndex += 1
    
    # Swap the pIndex element with the pivot to complete partitioning
    Swap(a, end, pIndex)

    return pIndex

def QuickSort(a, start, end):
    
    # Determines when to stop, aka when the list has one element
    if start >= end:
        return
    
    # Get the pivot index after partitioning to start the next iteration of quicksort
    pivot = Partition(a, start, end)
    
    # Recurrsion of quicksort
    QuickSort(a, start, pivot - 1)
    QuickSort(a, pivot + 1, end)
    
    
if __name__ == "__main__":
    a = [9, -3, 5, 2, 6, 8, -6, 1, 3]
    
    QuickSort(a, 0, len(a) - 1)
    
    print(a)