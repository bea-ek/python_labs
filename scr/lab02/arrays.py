def min_max(nums: list[float| int]) -> tuple[float|int, float|int]:
    '''кортеж из минимального и максимального элементов списка
    min_max([1,2,3,4]) -> (1,4)
    '''
    
    if not nums:
        raise ValueError("The list is empty.")
    return min(nums), max(nums)


def unique_sorted(nums: list[float | int]) -> list[float | int]:
    if not nums:
        raise ValueError("The list is empty.")
    return sorted(list(set(nums)))

    
def flatten(mat: list[list | tuple]) -> list:
    res=[]
    for row in mat:
        if type(row) not in [list, tuple]:
            raise TypeError("Row is not list or tuple")
        res.extend(row)
    return res

print(flatten([[1,2,3],1]))
