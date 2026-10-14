from src.lab04.io_text_csv import read_text, write_csv
from src.lib.text import normalize,tokenize,count_freq,top_n
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--in", nargs="+", help="Список файлов для обработки", dest= "input_files", default=  ["data/lab04/input.txt"])
parser.add_argument("--out", help="файл для вывода", dest = "output_file", default="data/lab04/report.csv")
parser.add_argument("--encoding", help="кодировка",default="utf8")
parser.add_argument('--per-file', default='data/lab04/report_per_file.csv', dest = "per_file")
parser.add_argument('--total', default='data/lab04/report_total.csv')
args = parser.parse_args()



flag = len(args.input_files)>1
per_sorted_freqs = []
all_sorted_freqs = {}
for file in sorted(args.input_files):
    text = read_text(file,encoding=args.encoding)

    normal_text = normalize(text)
    tokens = tokenize(normal_text)
    freqs = count_freq(tokens)
    sorted_freqs = top_n(freqs,len(freqs))
    
    if flag:
        just_file = file[file.rfind("/")+1:]
        for x in sorted_freqs:
            per_sorted_freqs.append((just_file, x[0],x[1]))
            all_sorted_freqs[x[0]] = all_sorted_freqs.get(x[0], 0) + x[1]
if flag:
    per_sorted_freqs = sorted(per_sorted_freqs, key = lambda x: (x[0],-x[2],x[1]))
    all_sorted_freqs = top_n(all_sorted_freqs,len(all_sorted_freqs))
    
    write_csv(per_sorted_freqs, args.per_file, ("file","word","count"))
    write_csv(all_sorted_freqs, args.total, ("word","count"))
    print(f'Всего слов : {sum([i[1] for i in all_sorted_freqs])}\nУникальных слов: {len(all_sorted_freqs)}\nТоп-5:')
    for val in all_sorted_freqs[:5]:
        print(f'{val[0]}: {val[1]}')
else:
    write_csv(sorted_freqs, args.output_file, ("word","count"))
    print(f'Всего слов : {sum([i[1] for i in sorted_freqs])}\nУникальных слов: {len(sorted_freqs)}\nТоп-5:')
    for val in sorted_freqs[:5]:
        print(f'{val[0]}: {val[1]}')
    
    



# python3 -m src.lab04.text_report --in data/lab04/a.txt data/lab04/b.txt --per-file data/lab04/report_per_file.csv --total data/lab04/report_total.csv