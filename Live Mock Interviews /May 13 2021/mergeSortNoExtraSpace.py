"""
Rememeber the variables:m,n,i,j
You need to solve this on paper and write logic from the paper
"""
def mergeSortNoExtraSpace(arr1, arr2):
    m = len(arr1)
    n = len(arr2)
    # Iterate through all
    # elements of ar2[] starting from
    # the last element
    for i in range(n-1,-1,-1): #Iterate reverse on arr2
        # Iterate through all
        # elements of ar2[] starting from
        # the last element
        last = arr1[m-1]
        j=m-2 #remember this since you will push everything down in arr1
        while j>=0 and arr1[j] > arr2[i]: #Push arr1 elements 1 down, remember j>=0
            arr1[j+1] = arr1[j]
            j-=1
        # If there was a greater element
        if j != m-2 or last > arr2[i]: #Solve the problem on paper to remember this logic
            arr1[j+1]=arr2[i]
            arr2[i]=last

arr1=[1,3,4,7,9]
arr2=[2,3,5,8]
mergeSortNoExtraSpace(arr1,arr2)
print('arr1 = ', str(arr1))
print('arr2 = ', str(arr2))