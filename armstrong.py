def armstrong(n):
    ''' sum of cubes of digits of a number is equal to the number itself '''
    temp=0
    for i in n:
        temp+=int(i)**len(n)
    if temp==int(n):
        return 1
    else:
        return 0
    
if __name__=="__main__":
    n=int(input())
    result=armstrong(str(n))
    if result==1:
        print("Armstrong: Yes")
    else:
        print("Armstrong: No")