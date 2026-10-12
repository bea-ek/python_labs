from src.lib.text import normalize, tokenize, count_freq, top_n
import sys 

text = sys.stdin.read()
if text.strip() == '':
    raise ValueError('Не был введен текст')

if_beautiful = 0 # Переменная, определяющая красивый (табличный) вывод


normal_text = normalize(text)
tokens = tokenize(normal_text)
words_cnt = count_freq(tokens)
top_words = top_n(words_cnt)


print(f'''
Всего слов: {len(tokens)}
Уникальных слов: {len(words_cnt)}
Топ-5:''')

if not if_beautiful: 
    for val in top_words:
        print(f'{val[0]}: {val[1]}')
        
else: 
    max_len = max([len(val[0]) for val in top_words] + [len('слово')])
    head = f'{"слово":<{max_len}} | частота'

    print(head)
    print('-' * len(head))
    for top in top_words:
        print(f'{top[0]:<{max_len}} | {top[1]}')
    print('...')