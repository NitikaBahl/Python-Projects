def tribonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    
    tribonacci_list = [0] * (n + 1)
    tribonacci_list[0] = 0
    tribonacci_list[1] = 1
    tribonacci_list[2] = 1
    
    for i in range(3, n + 1):
        tribonacci_list[i] = tribonacci_list[i - 1] + tribonacci_list[i - 2] + tribonacci_list[i - 3]
    
    return tribonacci_list[n]
if __name__=="__main__":
    n=int(input("Enter a number: "))
    result = tribonacci(n)
    print("tribonacci number at index {} is {}".format(n,result))