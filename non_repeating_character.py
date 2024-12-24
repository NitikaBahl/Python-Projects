from collections import Counter

def non_repeting_character(string):
    char_count = Counter(string)
    for index,char in enumerate(string):
        if char_count[char] == 1:
            return index
    return -1
    
if __name__=="__main__":
    string = input("ENTER A STRING: ")
    print(non_repeting_character(string))