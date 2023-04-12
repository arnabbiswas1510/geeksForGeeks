"""
https://practice.geeksforgeeks.org/batch/dsa-4/track/DSASP-Arrays/problem/divide-and-subtract-game2253
"""

#TODO Revisit
def divideAndSubtractGame(N):
    # code here
    if N==1:
        return "Arya"
    elif N==0:
        return "Jon"
    #here i took list upto 7 because if i do the operations that are done in
    #following for loop will not supported by numbers 6,7. will give the wrong answer("Jon")
    #because in the at some point they will reach "li[1]" which is 0
    #and because of that count+=1 will not done propely
    #and our if condition will not satisfied properly
    li=[1,0,1,1,1,1,0,0]
    move=[2,3,4,5]
    for i in range(8,N+1):
        count=0
        for j in move:
            if i-j>=0:
                if li[i-j]==1:
                    count+=1
                if li[i//j]==1:
                    count+=1
        if count==8:
            li.append(0)
        else:
            li.append(1)
    #print(li)
    return "Jon" if li[N]==1 else "Arya"

print(divideAndSubtractGame(6))
