import csv
import json
from pathlib import Path
from typing import Iterable, Sequence
import sys


def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл в CSV.
    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.
    Кодировка UTF-8. Порядок колонок — по алфавиту.
    """
    try:
        with open(json_path, "r", encoding="utf-8") as j_f:
            data = json.load(j_f)
    except FileNotFoundError:
        print(f"файл не найден: {json_path}", file=sys.stderr)
        sys.exit(1)
    except UnicodeDecodeError:
        print(f"кодировка не подходит: {json_path}", file=sys.stderr)
        sys.exit(1)
    except json.decoder.JSONDecodeError as e:
        print("Битый json: {e.msg}, {e.lineno}", file = sys.stderr)
        sys.exit(1)

        
json_to_csv("data/lab05/people.json","data/lab05/cities.csv")    
 
def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Преобразует CSV в JSON (список словарей).
    Заголовок обязателен, значения сохраняются как строки.
    json.dump(..., ensure_ascii=False, indent=2)
    """
    with open(csv_path, "w", encoding = "utf-8") as c_f:
        rows = csv.DictReader(c_f)
        