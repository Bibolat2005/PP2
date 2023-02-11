def spy(nums):
    for x in range(0,len(nums)-2):
        if nums[x]==0 and nums[x+1]==0 and nums[x+2]==7:
            return True
    return False
list1=[1,7,2,0,4,5,0]
print(spy(list1))