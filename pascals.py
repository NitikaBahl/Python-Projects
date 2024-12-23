def pascal(n):
    for i in range(n):
        for j in range(i+1):
            print(j, end=" ")
            print()
            return
        print("Invalid input")
        return
    print("Invalid input")
        

if __name__ == "__main__":
    n = input("Enter the number of rows: ")
    triangle = pascal(n)
    for row in triangle:
        print(*row) 