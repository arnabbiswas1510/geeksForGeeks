"""
https://practice.geeksforgeeks.org/batch/dsa-4/track/DSASP-Arrays/article/NzQ3Ng%3D%3D
Remember the below tricks in this problem
"""

MAX=10000
def maximumAppearingElement(l,r):
    arr=[0]*MAX
    actualMax=-1
    for i in range(len(l)):
        arr[l[i]]+=1
        arr[r[i]]-=1
        actualMax=max(r[i],actualMax) #Use this to limit iteration in line 14
    prefixSum=[0]
    maxAppearing=ind=-1
    for i in range(actualMax):
        prefixSum.append(arr[i]+prefixSum[i]) #Remember to compute prefixSum and perform subsequent steps in the
        # same loop to optimize performance
        if maxAppearing < prefixSum[i+1]:
            maxAppearing=prefixSum[i+1]
            ind=i #remember that you need to return index finally
    return ind

l=[1, 4, 9, 13, 21]
r=[15, 8, 12, 20, 30]
print(maximumAppearingElement(l,r))
