import csv
from pathlib import Path
from src.lab08.models import STUDENT_FIELDS, student_from_dict, validate_student
from src.lab04.io_text_csv import ensure_parent_dir

HEADER = STUDENT_FIELDS


def ensure_storage(path):
    '''
    Создание .csv файла с заголовком для хранения записей о студентах.
    '''
    p = Path(path)
    if p.suffix != '.csv': raise ValueError('Файл должен быть в .csv формате')
    ensure_parent_dir(p)
    p.write_text(','.join(STUDENT_FIELDS), encoding='utf-8')


def load_students(path):
    '''
    Проверка каждой записи и создание массива с записями о студентах.
    '''
    c_p = Path(path)
    
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
    students=[]
    for i,item in enumerate(data,1):
        try:
            students.append(student_from_dict(item))
        except ValueError as e:
            raise ValueError (f'ошибка в записи под indx {i}: {e}') from e
        except TypeError as e:
            raise TypeError (f'ошибка в записи под indx {i}: {e}') from e
    return students


# print(load_students("data/samples/lab09/students_input.csv"))

def save_students(path, students):
    '''
    Создание .csv файла с записями из списка "students".
    '''
    c_p = Path(path)
    if not isinstance(students, dict):
        raise TypeError(f'ожидается словарь, получено {type(rec)}')
    for i in students:
        validate_student(i)
            
    ensure_storage(c_p)
            
    with open(c_p, 'w', newline="", encoding="utf-8") as c_f:
            writer = csv.DictWriter(c_f, restval="")
            writer.writerows(students)


def list_students(path: str | Path, sort_by=None) -> list[dict]:
    '''
    Сортировка записей по параметру sort_by (sort_by ∈ {None, "fio", "gpa"}).
    '''
    if sort_by not in {None, "fio", "gpa"}: raise ValueError(f'"{sort_by}" не является параметром для сортировки')
    students_to_sort = load_students(Path(path))
    return sorted(students_to_sort, key=sort_by)


def add_student(path: str | Path, student: dict) -> None:
    '''
    Добавление студента в конец записи.
    '''
    validate_student(student)
    students_from_file = load_students(Path(path))
    students_from_file.append(student)
    save_students(path, students_from_file)


def find_students(path, substr):
    '''
    Поиск записей, в которые входит аргумент "substr" (без учёта регистра).
    '''
    rows = load_students(path)
    return [r for r in rows if substr.casefold() in r["fio"].casefold()]



def remove_student(path, fio):
    '''
    Удаление записей со значением fio, совпадающим с заданным параметром.
    Вывод количества таких записей.
    '''
    rows = load_students(path)
    # TODO: удалить ВСЕ вхождения и вернуть их количество
    k=0
    for i, r in enumerate(rows):
        if r["fio"] == fio:
            rows.pop(i)
            k+=1
    save_students(path,fio)
    return k


def update_student(path, fio, **fields):
    '''
    Обновление параметров первого студента с заданным "fio".
    '''
    # TODO: реализовать обновление с валидацией результата
    pass