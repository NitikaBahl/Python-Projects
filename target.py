def target_element(nums,target):
    nums.sort()
    
    if target in nums:
        index=nums.index(target)
        return index,nums[index]
    else:
        return "Element not found"

if __name__ == "__main__":
    nums=[1,2,3,4,5,6,7,8,9]
    target=5
    print(target_element(nums,target))