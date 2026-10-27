import argparse
from pathlib import Path
from src.lab04.io_text_csv import read_text
from src.lib.text import normalize,tokenize,count_freq,top_n

def main():
    parser = argparse.ArgumentParser(description="CLI-утилиты лабораторной №6")
    subparsers = parser.add_subparsers(dest="command")

    # подкоманда cat
    cat_parser = subparsers.add_parser("cat")
    cat_parser.add_argument("--input", required=True)
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    # подкоманда stats
    stats_parser = subparsers.add_parser("stats")
    stats_parser.add_argument("--input", required=True)
    stats_parser.add_argument("--top", type=int, default=5, help="Количество позиций в топе")

    args = parser.parse_args()

    if args.command == "cat":
        text= read_text(args.input).split("\n")
        if args.n:
            for i,line in enumerate(text):
                print(f"{i+1}: {line}")
        else:
            for line in text:
                print(line)

    elif args.command == "stats":
        text= read_text(args.input)
        normal_text = normalize(text)
        tokens = tokenize(normal_text)
        words_cnt = count_freq(tokens)
        top_words = top_n(words_cnt,args.top)
        
        max_len = max([len(val[0]) for val in top_words] + [len('слово')])
        head = f'{"слово":<{max_len}} | частота'

        print(head)
        print('-' * len(head))
        for top in top_words:
            print(f'{top[0]:<{max_len}} | {top[1]}')
        print('...')
        
            
        
main()