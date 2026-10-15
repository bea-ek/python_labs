import csv
from pathlib import Path
from typing import Iterable, Sequence
import sys

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    '''Считывает текст по указанному пути

    Args:
        path: Путь к файлу в формате строки или Path
        encoding: Тип кодировки файла (пример: encoding="cp1251"), по умолчанию utf-8

    Returns:
        Содержимое файла в виде строки
    '''
    
    try:
        with open(path, "r", encoding=encoding) as f:
            text = f.read()
            return text
    except FileNotFoundError:
        print(f"файл не найден: {path}", file=sys.stderr)
        sys.exit(1)
    except UnicodeDecodeError:
        print(f"кодировка не подходит: {path}", file=sys.stderr)
        sys.exit(1)
        
    

def ensure_parent_dir(path: str | Path) -> None:
    '''Проверяет наличие родительских папок, если их нет, то создает их
    Args:
        path: Путь к файлу в формате строки или Path

    Returns:
        None
    '''
    
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    
    
def write_csv(rows: Iterable[Sequence], path: str | Path,
              header: tuple[str, ...] | None = None) -> None:
    '''Записывает частоты слов в csv файл
        Args:
            rows: Итерируемый объект строк, которые нужно внести в файл
            path: Путь к файлу записи
            header: Заголовок файла
    
        Returns:
            None
    
        Raises:
            ValueError: Строки разной длинны
    '''
    
    rows = list(rows)
    if rows:
        etalon = len(rows[0])
        for r in rows:
            if len(r) != etalon:
                raise ValueError('Строки разной длинны')
    ensure_parent_dir(path)
    with open(path, 'w', newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)


if __name__ == "__main__":
    txt = read_text("data/lab04/input.txt") # должен вернуть строку
    print(txt)
    write_csv([("word","count"),("test",3)], "data/lab04/check.csv")  # создаст CSV
