"""

"""


def applyToEach(l,f):
    print('inside id is: ', id(l))
    for i in range(len(l)):
        l[i]=f(l[i])

l=[-1,-2,-3.4]
print('outside id is: ', id(l))

applyToEach(l,abs)
print(l)
