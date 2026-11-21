from datetime import date

STUDENT_FIELDS = ("fio", "birthdate", "group", "gpa")


def make_student(fio, birthdate, group, gpa):
    '''
    Создание записи после проверки корректности данных,
    при некорректности - TypeError или ValueError.
    '''
    values = {"fio":fio,"birthdate":birthdate,"group":group, "gpa": gpa}
    for k in values:
        if k=="gpa":
            continue
        if not isinstance(values[k],str):
            raise TypeError(f'{k} должно быть строкой, получено {type(fio)}')
        if not values[k].strip():
            raise ValueError(f"{k} не должно быть пустым")
    if not isinstance(gpa,float):
        raise TypeError(f'GPA должно быть вещественным числом, получено {type(gpa)}')

    if len(fio.split())<2:
        raise ValueError('введено неполное ФИО')
    if len(fio.split())>3:
        raise ValueError('введено слишком много слов для ФИО')
    
    try:
        born = date.fromisoformat(birthdate)
    except ValueError:
        raise ValueError(f'birthdate: некорректная дата {birthdate}, требуется формат YYYY-MM-DD')
    if born > date.today():
        raise ValueError(f'{birthdate} дата из будущего')

    if float(gpa)>5.0 or float(gpa)<0.0:
        raise ValueError('GPA должно быть числом от 0.0 до 5.0 включительно')

    return values


def validate_student(rec):
    '''
    Валидация записи о студенте.
    '''
    if not isinstance(rec, dict):
        raise TypeError(f'ожидается словарь, получено {type(rec)}')
    expected = set(STUDENT_FIELDS)
    given = set(rec)
    if expected != given:
        missing = expected - given
        extra = given-expected
        raise ValueError(f'неверный набор ключей: не хватает {missing}, лишние {extra}')
    make_student(**rec)

def student_age(rec, today=None):
    '''
    Вычисление возраста студента, по умолчанию, на сегодня.
    При желании посчитать на другой день - задать явно через параметр today.
    '''
    today = today or date.today()
    born = date.fromisoformat(rec['birthdate'])
    had_birthday = (today.month, today.day) >= (born.month, born.day)
    if had_birthday == True:
        return today.year - born.year
    return today.year - born.year - 1
    

def student_to_dict(rec):
    '''
    Создание копии студента при успешной валидации.
    '''
    validate_student(rec)
    return dict(rec)



def student_from_dict(d: dict) -> dict:
    '''
    Десериализация данных из словаря только по нужным параметрам.
    '''
    missing = [k for k in STUDENT_FIELDS if k not in d]
    if missing:
        raise ValueError(f'отсутствуют ключи: {missing}')
    rec = make_student(d['fio'], d['birthdate'], d['group'], float(d['gpa']))
    validate_student(rec)
    return rec

def format_student(rec):
    '''Форматирует запись студента в читаемую строку с инициалами и возрастом.'''
    parts = rec['fio'].split()
    second_name = parts[0]
    initials = ''.join(p[0].upper() + '.' for p in parts[1:])
    group = rec['group']
    age = student_age(rec)
    gpa = f"{rec['gpa']:.2f}"
    return f"{second_name} {initials} ({group}), {age} лет, GPA {gpa}"




if __name__ == '__main__':
    # 1. создание корректного студента
    student = make_student('Болдашова Екатерина Алексеевна', '2008-11-06', 'БИВТ-26-6-4', 5.0)
    print('Создан студент:', student)

    # 2. Форматирование
    print('Форматирование:', format_student(student))

    # 4. Проверка даты рождения
    age = student_age(student) 
    print('Возраст студента:', age)
# python3 -m src.lab08.models