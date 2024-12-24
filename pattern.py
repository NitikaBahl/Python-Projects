def pyramid(n):
    for i in range(1,n+1):
        print(" " * (n-i) + "*" * (2 * i - 1))

def inverted_pyramid(n):
    for i in range(n, 0, -1):
        print(" " * (n - i) + "*" * (2 * i - 1)) 

def right_triangle(n):
    for i in range(1, n+1):
        print("*" * i)

def decreasing_stars(n):
    for i in range(n, 0, -1):
        print("*" * i)

def increasing_series(n):
    for i in range(1,n+1):
        for j in range(0,i):
            print(i,end=" ")
        print()

def decreasing_series(n):
    for i in range(n,1,-1):
        for j in range(1,i):
            print(j,end=" ") 
        print()

def daimond_pattern(n):
    for i in range(1,n+1):
        print(" " * (n-i) + "*" * (2*i-1))

    for i in range (n-1,0,-1):
        print(" " * (n-i) + "*" * (2*i-1))

def valley(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end=" ")
        for j in range(1,2*(n-i)+1):
            print(" ",end=" ")
        for j in range(i,0,-1):
            print(j,end=" ")
        print()


def binary_triangle(n):
    for i in range(n,0,-1):
        for j in range(i):
            if (i+j)%2==0:
                print("0",end=" ")
            else:
                print("1",end=" ")
        print()

def pattern(n):
    d=0
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(d,end=" ")
            d+=1
        print()

def increasingAlphabet(n):
    for i in range (n):
        for j in range(i+1):
            print(chr(65+i),end=" ")
        print()

def decreasingAlphabet(n):
    for i in range (n):
        for j in range(n,0,-1):
            print(chr(65+i),end=" ")
        print()

def alphabet_pyramid(n):
    for i in range(1,n+1):
        print(" " * (n-i),end="")
        for j in range(1,i+1):
            print(chr(64+j),end="")
        for j in range(n-(n-i)-1,0,-1):
            print(chr(64+j),end="")
        print()  

def alphabet_pattern(n):
    for i in range(n):
        for j in range(n-i,n):
            print(chr(64+j),end=" ")
        print()

def valley2(n):
    for i in range(1,n+1):
        print("*"*i)
        for j in range(1,2*(n-i)+1):
            print(" ",end=" ")
        print("*",end=" ")
        print()

def valley3(n):
    for i in range(n):
        for j in range(n-i):
            print("*",end="")
        for j in range(2*i):
            print(" ",end="")
        for j in range(n-i):
            print("*",end="")
        print()

    for i in range(n-1):
        for j in range(i+1):
            print("*",end="")
        for j in range(2*(n-i)-2):
            print(" ",end="")
        for j in range(i+1):
            print("*",end="")
        
        print() 
    
def box(n):
    for i in range(n): 
        for j in range(n):
            if i==1 or i==n-1 or j==1 or j==n-1:
                print("*",end=" ")
            else:
                print(" ")
                
            print()

if __name__=="__main__":
    
    print("1. Pyramid")
    print("2. Inverted Pyramid")
    print("3. Right Triangle")
    print("4. Decreasing Stars")
    print("5. Diamond Pattern")
    print("6. Increasing Series")
    print("7. Decreasing Series")
    print("8. valley")
    print("9. Binary Triangle")
    print("10. pattern")
    print("11. Increasing Alphabet")
    print("12. Decreasing Alphabet")
    print("13. Alphabet Pyramid")
    print("14. Alphabet Pattern")
    print("15. valley2")
    print("16. valley3")
    print("17. box")
    print("Your choice? ")

    choice=int(input())
    n=int(input("enter n: "))

    if choice==1:
        pyramid(n)

    elif choice==2:
        inverted_pyramid(n)

    elif choice==3:
        right_triangle(n)

    elif choice==4:
        decreasing_stars(n)

    elif choice==5:
        daimond_pattern(n)

    elif choice==6:
        increasing_series(n)

    elif choice==7:
        decreasing_series(n)

    elif choice==8:
        valley(n)
    
    elif choice==9:
        binary_triangle(n)
    
    elif choice==10:
        pattern(n)

    elif choice==11:
        increasingAlphabet(n)

    elif choice==12:
        decreasingAlphabet(n)

    elif choice==13:
        alphabet_pyramid(n)

    elif choice==14:
        alphabet_pattern(n)

    elif choice==15:
        valley2(n)

    elif choice==16:
        valley3(n)
    
    elif choice==17:
        box(n)

    else:
        print("Invalid choice")  