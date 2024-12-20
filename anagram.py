from collections import Counter

def anagram(s1,s2):
    s1=s1.replace(" ","").lower()
    s2=s2.replace(" ","").lower()

    return Counter(s1) == Counter(s2)


if __name__=="__main__":
    print(anagram("listen", "silent")) 
    print(anagram("hello", "world"))  

    s="hello guys how are you all"
    print(Counter(s))

    lst=[1,2,3,1,2,3,6,4,3,4,]
    counter=Counter(lst)
    print(counter)
    print(counter.most_common(3))