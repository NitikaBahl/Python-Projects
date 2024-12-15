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
