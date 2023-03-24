"""
https://practice.geeksforgeeks.org/batch/dsa-4/track/DSASP-Arrays/article/NzE5Ng%3D%3D
"""


def leadersInArray(arr):
    print(arr[len(arr)-1], end=", ")
    maxSoFar=arr[len(arr)-1]
    for i in range(len(arr)-1,0,-1):
        if(arr[i])>maxSoFar:
            print(arr[i], end=", ")
            maxSoFar=arr[i]


leadersInArray([6, 17, 4, 3, 5, 2])
print(end="\n")
leadersInArray([1, 2, 3, 4, 5, 2])
