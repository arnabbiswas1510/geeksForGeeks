"""
https://practice.geeksforgeeks.org/batch/dsa-4/track/DSASP-Arrays/article/NzE5OA%3D%3D
Naive approach is to use a Map to keep track of frequency count and then iterate through the map to print the count
But this can be optimized as below since the array is sorted
Also check out printf style string formatting. Need not cast ints as str, hence more concise
"""


def frequenciesInASortedArray(arr):
    cnt=1
    for i in range(1,len(arr)):
        if arr[i-1] != arr[i]:
            print("%s : %s" % (arr[i-1],cnt))
            cnt=1
        else:
            cnt+=1
    print("%s : %s" % (arr[i],cnt))

frequenciesInASortedArray([1, 1, 1, 2, 3, 3, 5, 5, 8, 8, 8, 9, 9, 10])
frequenciesInASortedArray([2, 2, 6, 6, 7, 7, 7, 11])
