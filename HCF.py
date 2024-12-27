def HCF(a,b):
    if b==0:
        return a
    else:
        return HCF(b,a%b)
    
def LCM(a,b):
    return a*b//HCF(a,b)
    
if __name__=="__main__":
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print("HCF of",a,"and",b,"is",HCF(a,b))
    print("LCM of",a,"and",b,"is",LCM(a,b))