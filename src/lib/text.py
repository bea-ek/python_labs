import re

def normalize(text: str, *, casefold: bool = True, yo2e : bool = True) -> str:
    r'''нормализует строку:
        если casefold = True, приводит к сложенному регистру, иначе - к нижнему
        если yo2e = True, заменяет ё на е,
        убирает невидимые управляющие символы и линие пробелы
        
        normalize("ПрИвЕт\nМИр\t") → "привет мир"
    '''
    
    if casefold:
        text = text.casefold()
    else:
        text = text.lower()
    if yo2e:
        text = text.replace('ё', 'е')
    text = ' '.join(text.split())
    return text


def tokenize(text:str) -> list[str]:
    '''разбивает на «слова» по небуквенно-цифровым разделителям.'''
    
    return re.findall(r"\w+(?:-\w+)*", text)


def count_freq(tokens: list[str]) -> dict[str,int]:
    '''считает частоты в словарь {слово: количество}'''
    
    count_fr = {}
    for i in set(tokens):
        count_fr[i] = tokens.count(i)
    return count_fr


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    '''Выводит тоx n слов по частоте обращения '''

    return sorted(freq.items(), key = lambda x: (-x[1],x[0]))[:n]
        
    
if __name__ == '__main__' :
    # normalize
    assert normalize("ПрИвЕт\nМИр\t") == "привет мир"
    assert normalize("ёжик, Ёлка") == "ежик, елка"

    # tokenize
    assert tokenize("привет, мир!") == ["привет", "мир"]
    assert tokenize("по-настоящему круто") == ["по-настоящему", "круто"]
    assert tokenize("2025 год") == ["2025", "год"]

    # count_freq + top_n
    freq = count_freq(["a","b","a","c","b","a"])
    assert freq == {"a":3, "b":2, "c":1}
    assert top_n(freq, 2) == [("a",3), ("b",2)]

    # тай-брейк по слову при равной частоте
    freq2 = count_freq(["bb","aa","bb","aa","cc"])
    assert top_n(freq2, 2) == [("aa",2), ("bb",2)]
    
    
    #Все тест-кейсы

    print(fr'''
    normalize

    "ПрИвЕт\nМИр\t" -> {normalize("ПрИвЕт\nМИр\t")}
    "ёжик, Ёлка" -> {normalize("ёжик, Ёлка")}
    "Hello\r\nWorld" -> {normalize("Hello\r\nWorld")}
    "  двойные   пробелы  " -> {normalize("  двойные   пробелы  ")}
    ''')

    print(fr'''
    tokenize

    "привет мир" -> {tokenize("привет мир")}
    "hello,world!!!" -> {tokenize("hello,world!!!")}
    "по-настоящему круто" -> {tokenize("по-настоящему круто")}
    "2025 год" -> {tokenize("2025 год")}
    "emoji 😀 не слово" -> {tokenize("emoji 😀 не слово")}
    ''')

    print(fr'''
    count_freq + top_n

    Токены ["a","b","a","c","b","a"] -> частоты {count_freq(["a", "b", "a", "c", "b", "a"])};
    top_n(..., n=2) -> {top_n(count_freq(["a", "b", "a", "c", "b", "a"]), 2)}

    При равенстве частот: токены ["bb","aa","bb","aa","cc"] -> {count_freq(["bb", "aa", "bb", "aa", "cc"])};
    top_n(..., n=2) → {top_n(count_freq(["bb", "aa", "bb", "aa", "cc"]), 2)}
    ''')