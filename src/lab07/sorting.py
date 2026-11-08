def bubble_sort(nums) -> list:
    nums = list(nums)
    n = len(nums)
    for i in range(n-1):
        flag=True
        for j in range(n-i-1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
                flag=False
        if flag:
            break
    return nums

def insertion_sort(nums) -> list:
    nums = list(nums)
    for i in range(1,len(nums)):
        key = nums[i]
        j=i-1
        while j>=0 and nums[j]>key:
            nums[j+1]=nums[j]
            j-=1
        nums[j+1]=key
    return nums

def selection_sort(nums) -> list:
    nums = list(nums)
    for i in range(len(nums)):
        m=i
        for j in range(i+1,len(nums)):
            if nums[j]<nums[m]:
                m = j
        nums[i],nums[m] = nums[m],nums[i]
    return nums

