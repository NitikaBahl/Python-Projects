from collections import Counter

def frequency_1(arr):
    counter=Counter(arr)
    for words in counter:
        if counter[words]==1:
            return words
    return None

if __name__=="__main__":
    arr=[1,1,2,2,3,4,4,4]
    result=frequency_1(arr)
    if result is not None:
        print("Digit with 1 frequency: ",result)
    else:
        print("no digit with frequency = 1")