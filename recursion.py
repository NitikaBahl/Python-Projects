def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
def ntimes(n):
    if n==0:
        return 0
    else:
        print(n)
        ntimes(n-1)
  
def fibonacci(n):
    if n <=1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
def sum_of_list(lst):
    if not lst:
        return 0
    else:
        return lst[0] + sum_of_list(lst[1:])
    
if __name__=="__main__":
    #print(factorial(5))
    #print(fibonacci(10))
    #print(sum_of_list([1,2,3,4,5]))
    print(ntimes(5))