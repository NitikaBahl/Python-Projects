def max_water(l1):
    max_area=0
    n=len(l1)

    for i in range(n):
        max_area=max(max_area, min(l1[i],l1[n-1])*(n-i-1))
    return max_area
    
if __name__=="__main__":
    l1=[1,8,6,2,5,4,3,8,3]
    print(max_water(l1))