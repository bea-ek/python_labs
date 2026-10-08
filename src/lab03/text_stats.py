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
    '''считает частоты '''
    count = {}
    for i in set(tokens):
        count[i] = tokens.count(i)
    return count
    
if __name__ == '__main__' :
    assert normalize("ПрИвЕт\nМИр\t") == "привет мир"
    assert normalize("ёжик, Ёлка") == "ежик, елка"
    assert normalize("Hello\r\nWorld") == "hello world"
    assert normalize("  двойные   пробелы  ") == "двойные пробелы"
    
    assert tokenize("привет, мир!") == ["привет", "мир"]
    assert tokenize("по-настоящему круто") == ["по-настоящему", "круто"]
    assert tokenize("2025 год") == ["2025", "год"]
    
    print(count_freq([2132,'fsdf',2132]))