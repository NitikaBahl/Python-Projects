def pascal(n):
    triangle = [] 
    for i in range(n):
        row = [1]  
        if i > 0:  
            for j in range(len(triangle[-1]) - 1):
                row.append(triangle[-1][j] + triangle[-1][j + 1])
            row.append(1)  
        triangle.append(row)  
    return triangle

if __name__ == "__main__":
    n = input("Enter the number of rows: ")
    triangle = pascal(n)
    for row in triangle:
        print(*row) 