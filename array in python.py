import numpy as np

def reverse(a):
    return " ".join(map(str,reversed(a)))


if __name__=="__main__":
    a=[1,7,3,5,9,2]
    rev_a=reverse(a)
    print("Reverse of the array is: ", rev_a)
    print("Minimum value in the array is: ", min(a))
    print("Maximum value in the array is: ", max(a))
    print("Sum of the array is: ", sum(a))
    print("Sum of min and max of the array is: ", min(a)+max(a))
    print("Average of the array is: ", sum(a)/len(a))
    print("Median of the array is: ", np.median(a))
    print("Standard Deviation of the array is: ", np.std(a))
    print("Variance of the array is: ", np.var(a))
    print("Range of the array is: ", max(a)-min(a))
    print("Sorted array is: ", sorted(a))
    print("Sorted array in descending order is: ", sorted(a,reverse=True))
    print("Array with duplicates removed is: ", list(set(a)))
    print("Array with duplicates removed and sorted is: ", sorted(list(set(a))))
    print("Array with duplicates removed and sorted in descending order is: ", sorted(list(set(a)),reverse=True))
    
          
