import csv
import json
from pathlib import Path
from src.lab04.io_text_csv import ensure_parent_dir


def json_to_csv(json_path: str, csv_path: str) -> None:
    '''Записывает значения

    Args:
        json_path: Путь к json файлу из которого читаем
        csv_path: Путь к csv файлу куда пишем

    Returns: 
        None

    Raises:
        FileNotFoundError: 
            Указанный JSON файл не найден
        ValueError:
            Указанный файл не формата JSON
            Пустой JSON или неподдерживаемая структура
            Файл JSON пустой или имеет неправильный формат
            Все элементы списка JSON должны быть словарями
    '''
    j_p = Path(json_path)
    c_p = Path(csv_path)
    
    if not j_p.exists():
        raise FileNotFoundError(f"файл не найден: {j_p}")
    if j_p.suffix.lower() != '.json':
        raise ValueError(f"Указанный файл не формата JSON: {j_p}")
    

    with j_p.open('r', encoding='utf-8') as j_f:
        try:
            data = json.load(j_f)
        except json.JSONDecodeError as e:
            raise ValueError(f"Файл содержит некорректный JSON: {e.lineno}, {e.msg}")
        if not isinstance(data,list) or len(data) == 0:
            raise ValueError("Файл JSON пустой или имеет неправильный формат")
        if not all(isinstance(x, dict) for x in data):
            raise ValueError("Все элементы списка JSON должны быть словарями")
        
    ensure_parent_dir(c_p)
    # порядок колонок определяется их первым появлением в JSON
    headers = []
    for item in data:
        for key in item.keys():
            if key not in headers:
                headers.append(key)
            
    with open(c_p, 'w', newline="", encoding="utf-8") as c_f:
            #restval - заполняет отсутствующие поля пустыми строками
            writer = csv.DictWriter(c_f, fieldnames=headers, restval="")
            writer.writeheader()
            writer.writerows(data)
        
   
def csv_to_json(csv_path: str, json_path: str) -> None:
    '''Записывает значения

    Args:
        csv_path: Путь к csv файлу из которого читаем
        json_path: Путь к json файлу куда пишем
        
    Returns: 
        None

    Raises:
        FileNotFoundError: 
            Указанный CSV файл не найден
        ValueError:
            Указанный файл не формата CSV
            CSV файл пустой
    '''
    
    j_p = Path(json_path)
    c_p = Path(csv_path)
    
    if not c_p.exists():
        raise FileNotFoundError(f"Указанный CSV файл не найден: {c_p}")
    
    if c_p.suffix.lower() != '.csv':
        raise ValueError(f"Указанный файл не формата CSV: {c_p}")
    

    with open(c_p, 'r', encoding='utf-8') as c_f:
        reader = csv.DictReader(c_f)
        if reader.fieldnames is None:
            raise ValueError("CSV файл пустой")
        data = list(reader)
    if not data:
        raise ValueError("Файл CSV не содержит данных")

    ensure_parent_dir(j_p)
            
    with j_p.open('w', encoding="utf-8") as j_f:
        json.dump(data, j_f, ensure_ascii=False, indent=2)
        

# csv_to_json("data/lab05/samples/pets.csv","data/lab05/samples/pets.json")

# json_to_csv(
#     "data/lab05/samples/people.json",
#     "data/lab05/out/people_from_json.csv",
# )

# csv_to_json(
#     "data/lab05/samples/people.csv",
#     "data/lab05/out/people_from_csv.json",
# )

## Мои тесты
json_to_csv(
    "data/lab05/samples/pets.json",
    "data/lab05/out/pets_from_json.csv",
)

csv_to_json(
    "data/lab05/samples/pets.csv",
    "data/lab05/out/pets_from_csv.json",
)
