def pyramid(n):
    for i in range(1,n+1):
        print(" " * (n-i) + "*" * (2*i-1))

def inverted_pyramid(n):
    for i in range(n, 0, -1):
        print(" " * (n - i) + "*" * (2 * i - 1)) 

def right_triangle(n):
    for i in range(1,n+1):
        print("*" * i)

def decreasing_stars(n):
    for i in range(n,0,-1):
        print("*" * i) 

def daimond_pattern(n):
    for i in range(1,n+1):
        print(" " * (n-i) + "*" * (2*i-1))

    for i in range (n-1,0,-1):
        print(" " * (n-i) + "*" * (2*i-1))

if __name__=="__main__":
    
    print("1. Pyramid")
    print("2. Inverted Pyramid")
    print("3. Right Triangle")
    print("4. Decreasing Stars")
    print("5. Diamond Pattern")
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

    else:
        print("Invalid choice")  