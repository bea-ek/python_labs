from src.lab04.io_text_csv import read_text, write_csv
from src.lib.text import normalize,tokenize,count_freq,top_n
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--in", nargs="+", help="Список файлов для обработки", dest= "input_files", default="data/lab04/input.txt")
parser.add_argument("--out", nargs="1", help="файл для вывода", dest = "output_file", default="data/lab04/report.csv")
parser.add_argument("--encoding", nargs="1", help="кодировка")
parser.add_argument('--per_file', default='data/lab04/report_per_file.csv')
parser.add_argument('--total', default='data/lab04/report_total.csv')
args = parser.parse_args()

flag = len(args.input_files)>1
per_sorted_freqs = []
all_sorted_freqs = {}
for file in sorted(args.input_files):
    text = read_text(file,encoding="utf8")

    normal_text = normalize(text)
    tokens = tokenize(normal_text)
    freqs = count_freq(tokens)
    sorted_freqs = top_n(freqs,len(freqs))
    
    if flag:
        for x in sorted_freqs:
            per_sorted_freqs.append((file, x[0],x[1]))
            if all_sorted_freqs.get(x[0],0):
                all_sorted_freqs[x[0]]+=x[1]
            else:
                all_sorted_freqs[x[0]]=x[1]
if flag:
    write_csv(per_sorted_freqs, args.per_file, ("file","word","count"))
    write_csv(all_sorted_freqs, args.total, ("word","count"))
else:
    write_csv(sorted_freqs, args.output_file, ("word","count"))
    
        

print(f'''
Всего слов (различных): {len(sorted_freqs)}
Уникальных слов: {len([i for i in sorted_freqs if i[1]==1])}
Топ-5:''')
for val in sorted_freqs[:5]:
        print(f'{val[0]}: {val[1]}')
