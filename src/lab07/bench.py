import csv
import timeit
import random
from src.lab04.io_text_csv import write_csv
from src.lab07.sorting import *
from src.lab07.search import *
 
def read_numbers(path):
    "считывает данные из csv"
    with open(path, encoding="utf-8") as f:
        return [row for row in csv.reader(f)]
 
def make_samples_sort():
    "создает csv файлы для проверок"
    for n in (1_000,10_000,100_000):
        all = []
        for _ in range(100):
            nums = [random.randint(-100, 100) for _ in range(n)]
            all.append(nums)
        write_csv(all,f"data/samples/lab07/numbers2sort_{n}.csv")
    
    
def bench_sorts(n):
    """Запускает бенчмарки для сортировок и собирает данные в список с кортежами"""
    data = read_numbers(f"data/samples/lab07/numbers2sort_{n}.csv")
    rows = []
    for fn in (sorted, bubble_sort,insertion_sort,selection_sort):
        if n <100_000:
            t = timeit.timeit(lambda: fn(data), number=1)
            rows.append(("sort", n, fn.__name__, f"{t:.6f}"))
        else:
            rows.append(("search", 10_000, fn.__name__, ">60"))
    return rows

def bench_search():
    """Запускает бенчмарки для поиска и собирает данные в список с кортежами"""
    targets=[]
    data = [random.randint(-100_000, 100_000) for i in range(100_000)]
    targets = [random.choice(data) for _ in range(10_000)]
    
    
    rows=[]

    t = timeit.timeit(lambda: [data.index(t) for t in targets], number=1)
    rows.append(("search", 10_000, "index", f"{t:.6f}"))
    

    time_ls = timeit.timeit(lambda: [linear_search(data,t) for t in targets],  number =1)
    rows.append(("search", 10_000, "linear_search", f"{time_ls:.6f}"))

    time_sbb=timeit.timeit(lambda: sorted(data), number=1)
    rows.append(("search", 10_000, "sort_before_binary", f"{time_sbb:.6f}"))
    sorted_data= sorted(data)

    time_bs = timeit.timeit(lambda: [binary_search(sorted_data,t) for t in targets],  number =1)
    rows.append(("search", 10_000, "binary_search", f"{time_bs:.6f}"))

    for n in [1_000,10_000]:
        data_ts = [random.randint(-1_000_000,1_000_000) for _ in range(n)]
        a, b = random.sample(data_ts, 2)
        target = a+b

        time_tsb = timeit.timeit(lambda: two_sum_brute(data_ts,target), number=1)
        rows.append(("search", n, "two_sum_brute", f"{time_tsb:.6f}"))

        time_tsf = timeit.timeit(lambda: two_sum_fast(data_ts,target), number=1)
        rows.append(("search", n, "two_sum_fast", f"{time_tsf:.6f}"))

    return rows

def main():
    header = ("task", "n", "func", "seconds")
    rows=[]
    for i in (1_000,10_000):
        rows.extend(bench_sorts(i))
    rows.extend(bench_search())

    write_csv(rows, 'data/out/lab07/bench_result.csv', header)

    print("Результаты бенчмарка")
    print(f"{'Task':<12} | {'N':<8} | {'Func':<20} | {'Seconds':<12}")
    print('-'*60)
    for t, n, f, s in rows:
        print(f"{t:<12} | {n:<8} | {f:<20} | {s:<12}")
    print('-'*60)
    print("Результаты сохранены в data/lab07/bench_result.csv")


if __name__ == "__main__":
    main()
    
#python3 -m src.lab07.bench
