import random
from src.lab04.io_text_csv import write_csv
from src.lab07.sorting import bubble_sort,insertion_sort,selection_sort
from src.lab07.search import linear_search, binary_search, two_sum_brute, two_sum_fast

def check_sorting(fn, trials=100):
    all = []
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        original = list(nums)
        result = fn(nums)
        assert result == sorted(nums), f"{fn.__name__} ошиблась на {nums}: {result}"
        assert nums == original, f"{fn.__name__} изменила исходный список"
    # создание файлов для bench
    #     all.append(nums)
    # write_csv(all,"data/samples/lab07/numbers2sort_{n}.csv")
    print(f"OK: {fn.__name__}, {trials} проверок")
    return trials
        

def check_search(trials=100):
    for _ in range((trials+1)//2):
        # поиск любого существующего числа
        n = random.randint(1, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        need = random.choice(nums)
        assert linear_search(nums,need) == nums.index(need), (f"linear_search: {need} in {nums}")
        nums.sort()
        assert binary_search(nums, need) == nums.index(need), (f"binary_search: {need} in {nums}")   
             
        
    for _ in range((trials//2+1)//2):
        # поиск несуществующего числа
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        need = random.choice((random.randint(-200,-100),random.randint(100,200)))
        assert linear_search(nums, need) == -1, (f"linear_search: {need} in {nums}")
        nums.sort()
        assert binary_search(nums, need) == -1, (f"binary_search: {need} in {nums}")             
        
    for _ in range(trials//4):
        # поиск числа на границе
        n = random.randint(1, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        need = nums[random.choice((0,-1))]
        assert linear_search(nums, need) == nums.index(need), (f"linear_search: {need} in {nums}")
        nums.sort()
        assert binary_search(nums, need) == nums.index(need), (f"binary_search: {need} in {nums}")        
    
    print(f"OK: linear_search, binary_search, {trials} проверок")
    return trials


def check_two_sum(trials=100):
    for _ in range((trials+1)//2):
        n = random.randint(2, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        a,b = random.sample(nums,2)
        i,j = two_sum_fast(nums,a+b)
        assert nums[i]+nums[j] == a+b, (f"two_sum_fast: {a}+{b}={a+b} in {nums}") 
        i,j = two_sum_brute(nums,a+b)
        assert nums[i]+nums[j] == a+b, (f"two_sum_brute: {a}+{b}={a+b} in {nums}")
        
    for _ in range(trials//2):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        a = random.randint(100,200)
        b = random.randint(100,200)
        assert two_sum_fast(nums,a+b) == None, (f"two_sum_fast: {a}+{b}={a+b} in {nums}") 
        assert two_sum_brute(nums,a+b) == None, (f"two_sum_brute: {a}+{b}={a+b} in {nums}")
         
    print(f"OK: two_sum_fast,two_sum_brute, {trials} проверок")
    return trials


if __name__== "__main__":
    random.seed(42)
    n=0
    
    for fn in (bubble_sort, insertion_sort, selection_sort):
        n+=check_sorting(fn)
    
    n+=check_search()
    
    n+=check_two_sum()
    
    print(f"OK, {n} проверок")