def format_record(rec: tuple[str,str,float]) -> str:
    '''отформатированная строка вида:
    Иванов И.И., гр. BIVT-25, GPA 4.60
    
    Raises:
        ValueError: 'кортеж должен состоять из 3 элементов (ФИО, группа, GPA)'
                    'введено неполное ФИО'
                    'введено слишком много слов для ФИО'
                    'группа не может быть пустой'
                    'GPA должно быть числом от 0.0 до 5.0 включительно'
        
        TypeError:  'введен не кортеж'
                    'ФИО должно быть стокой'
                    'группа должна быть строкой'
                    'GPA должно быть вещественным числом'
                    
    '''
    
    if not isinstance(rec,tuple):
        raise TypeError('введен не кортеж')
    if len(rec)!=3:
        raise ValueError('кортеж должен состоять из 3 элементов (ФИО, группа, GPA)')
            
    if not isinstance(rec[0],str):
        raise TypeError('ФИО должно быть стокой')
    if not isinstance(rec[1],str):
        raise TypeError('группа должна быть строкой')
    if not isinstance(rec[2],float):
        raise TypeError('GPA должно быть вещественным числом')

    if len(rec[0].split())<2:
        raise ValueError('введено неполное ФИО')
    if len(rec[0].split())>3:
        raise ValueError('введено слишком много слов для ФИО')
    if not rec[1]:
        raise ValueError('группа не может быть пустой')    
    if float(rec[2])>5.0 or float(rec[2])<0.0:
        raise ValueError('GPA должно быть числом от 0.0 до 5.0 включительно')
    
    name =  [x.capitalize() for x in rec[0].split()]
    for i in range(1,len(name)):
        name[i]=name[i][0]+'.'
    return f'{name[0]} {''.join(name[1:])}, гр. {rec[1]}, GPA {float(rec[2]):.2f}'


#тесты
print(f'''
("Иванов Иван Иванович", "BIVT-25", 4.6) -> {format_record(("Иванов Иван Иванович", "BIVT-25", 4.6))}
("Петров Пётр", "IKBO-12", 5.0) -> {format_record(("Петров Пётр", "IKBO-12", 5.0))}
("Петров Пётр Петрович", "IKBO-12", 5.0) -> {format_record(("Петров Пётр Петрович", "IKBO-12", 5.0))}
("  сидорова  анна   сергеевна ", "ABB-01", 3.999) -> {format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999))}
''')
print(f'("Иван", "БИВТ-2", 3.0) -> {format_record(("Иван", "БИВТ-2", 3.0))}')