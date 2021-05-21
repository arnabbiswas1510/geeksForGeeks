def mergeSorted(arr1, arr2):
    sorted=[None]*(len(arr1)+len(arr2))
    i = j = k = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            sorted[k] = arr1[i]
            i+=1
        else:
            sorted[k] = arr2[j]
            j+=1
        k+=1

    while i < len(arr1):
        sorted[k] = arr1[i]
        i+=1
        k+=1

    while j < len(arr2):
        sorted[k] = arr2[j]
        j += 1
        k += 1

    return sorted

print(mergeSorted([1,3,4,7,9],[2,3,5,8]))
