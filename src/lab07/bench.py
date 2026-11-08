import csv
import timeit
from src.lab04.io_text_csv import write_csv
from src.lab07.sorting import *
 
def read_numbers(path):
    with open(path, encoding="utf-8") as f:
        return [int(row["value"]) for row in csv.DictReader(f)]
 
 
def bench_sorts(n):
    data = read_numbers(f"data/samples/lab07/numbers_{n}.csv")
    rows = []
    t = timeit.timeit(lambda: sorted(data), number=1)
    rows.append(("sort", n, "sorted", t))
    t = timeit.timeit(lambda: bubble_sort(data), number=1)
    rows.append(("sort", n, "sorted", t))
    t = timeit.timeit(lambda: insertion_sort(data), number=1)
    rows.append(("sort", n, "sorted", t))
    t = timeit.timeit(lambda: selection_sort(data), number=1)
    rows.append(("sort", n, "sorted", t))
    # TODO: на 10**5 — с ограничением ???
    return rows

# if __name__=="__main__":
    