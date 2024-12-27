def prime_numbers_upto(n):
    ''' returns all prime numbers upto n '''
    prime_numbers=[]
    for i in range(2,n+1):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            prime_numbers.append(i)
    return prime_numbers

if __name__=="__main__":
    n=int(input("Enter a number: "))
    print("prime numbers are: ",prime_numbers_upto(n))
