import csv
from pathlib import Path
from src.lab04.io_text_csv import ensure_parent_dir
from openpyxl import Workbook
import csv




def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    '''
    Конвертирует CSV в XLSX.
    
    Args:
        csv_path: Путь к csv файлу из которого читаем
        xlsx_path: Путь к xlsx файлу куда пишем
        
    Returns: 
        None

    Raises:
        FileNotFoundError: 
            Указанный CSV файл не найден
        ValueError:
            Указанный файл не формата CSV
            CSV файл пустой
    '''
    c_p = Path(csv_path)
    x_p = Path(xlsx_path)
    
    if not c_p.exists():
        raise FileNotFoundError(f"Указанный CSV файл не найден: {c_p}")
    
    if c_p.suffix.lower() != '.csv':
        raise ValueError(f"Указанный файл не формата CSV: {c_p}")
    
    wb = Workbook()
    ws = wb.active
    if ws is None:
        ws = wb.create_sheet("Sheet1")
    ws.title = "Sheet1"

    with open(c_p, encoding="utf-8") as c_f:
        for row in list(csv.reader(c_f)):
            ws.append(row) 
            
    for col in ws.columns:
        max_len = 0
        letter = col[0].column_letter

        for cell in col:
            if cell.value and len(str(cell.value)) > max_len:
                max_len = len(str(cell.value))

        ws.column_dimensions[letter].width = max(max_len, 8)

    ensure_parent_dir(x_p)      
    wb.save(x_p)

# csv_to_xlsx(
#     "data/lab05/samples/cities.csv",
#     "data/lab05/out/cities.xlsx",
# )

csv_to_xlsx(
    "data/lab05/samples/students.csv",
    "data/lab05/out/students.xlsx",
)