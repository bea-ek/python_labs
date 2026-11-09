def linear_search(nums, x) -> int:
    """Возвращает индекс первого вхождения x или -1."""
    for i in range(len(nums)):
        if nums[i] == x:
            return i
    return -1

def binary_search(sorted_nums, x) -> int:
    """Ищет x  в отсортированном списке.
    Для неотсортированного списка результат не определен."""
    lo=0
    hi=len(sorted_nums)-1
    while lo<=hi:
        mid = (lo+hi)//2
        if x < sorted_nums[mid]:
            hi = mid -1
        elif x > sorted_nums[mid]:
            lo = mid+1
        else: 
            while mid > 0 and sorted_nums[mid]==sorted_nums[mid-1]:
                mid -= 1
            return mid
    return -1

def two_sum_brute(nums, target):
    """Ищет пару индексов таких чисел, сумма которых равна target."""
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j]==target:
                return (i,j)
    return None
                


def two_sum_fast(nums, target):
    """Ищет пару индексов таких чисел, сумма которых равна target за один проход со словарём."""
    seen = {}
    for i,x in enumerate(nums):
        if target-x in seen:
            return (seen[target-x],i)
        else:
            seen[x] = seen.get(x,0) or i
    return None

