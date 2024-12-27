def count_digit(n):
    return len(n)

def reverse(n):
    return n[::-1]

def palindrome(n):
    temp=0
    if n==reverse(n):
        temp=1
    else:
        temp=0
    return temp


if __name__=="__main__":
    n = input("Enter a number: ")
    print("Number of digits:", count_digit(n))
    print("Reverse of the number:", reverse(n))

    if palindrome(n)==1:
        print("Palindrome: Yes")
    else:
        print("Palindrome: No")