import numpy as np

def majority(arr):
    n=len(arr)
    majority=n//2
    count=np.bincount(arr)
    for elemnet , count in enumerate(count):
        if count>majority:
            return elemnet
    return None

if __name__=="__main__":
    arr=np.array([1,1,2,1,3,2,1,1,3]) 
    result=majority(arr)

    if result is not None:
        print("Majority element is: ", result)
    else:
        print("No majority element")