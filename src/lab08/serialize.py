from src.lab08.models import student_to_dict,student_from_dict
import json
from pathlib import Path
from src.lab04.io_text_csv import ensure_parent_dir

def students_to_json(students, path):
    '''
    Запись списка студентов в .json файл.
    '''
    data = [student_to_dict(s) for s in students]
    if Path(path).suffix.lower() != '.json':
        raise ValueError(f"Указанный файл не формата JSON: {path}")
    ensure_parent_dir(path)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    
def students_from_json(path: str):
    '''
    Преобразование .json файла в список студентов.
    Политика обработки битых записей: strict. Первая битая запись
    вызывает ValueError/TypeError с номером записи и причиной.
    '''
    j_p = Path(path)
    
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
    
    students=[]
    for i,item in enumerate(data,1):
        try:
            students.append(student_from_dict(item))
        except ValueError as e:
            raise ValueError (f'ошибка в записи под indx {i}: {e}') from e
        except TypeError as e:
            raise TypeError (f'ошибка в записи под indx {i}: {e}') from e
    return students

if __name__=="__main__":
    input_file = 'data/samples/lab08/students_input.json'
    output_file = 'data/out/lab08/students_output.json'
    bad_file = 'data/samples/lab08/students_bad.json'

    # 1. туда и обратно
    print (f'чтение из {input_file}, сохранение в {output_file}')
    students_list = students_from_json(input_file)
    students_to_json(students_list,output_file)

    # 2. битый
    students_from_json(bad_file)
    
# python3 -m src.lab08.serialize