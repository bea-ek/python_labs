import argparse
from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.csv_xlsx import csv_to_xlsx

def main():
    parser = argparse.ArgumentParser(description="Конвертеры данных")
    sub = parser.add_subparsers(dest="cmd")

    p1 = sub.add_parser("json2csv",help= "Конвертация json файла в csv")
    p1.add_argument("--in", dest="input", required=True)
    p1.add_argument("--out", dest="output", required=True)

    p2 = sub.add_parser("csv2json",help= "Конвертация csv файла в json")
    p2.add_argument("--in", dest="input", required=True)
    p2.add_argument("--out", dest="output", required=True)

    p3 = sub.add_parser("csv2xlsx",help= "Конвертация csv файла в xlsx")
    p3.add_argument("--in", dest="input", required=True)
    p3.add_argument("--out", dest="output", required=True)

    args = parser.parse_args()

    if args.cmd == "json2csv":
        json_to_csv(args.input,args.output)
    if args.cmd == "csv2json":
        csv_to_json(args.input,args.output)
    if args.cmd == "csv2xlsx":
        csv_to_xlsx(args.input,args.output)
    
main()


#Тесты
# python3 -m src.lab06.cli_convert json2csv --in data/samples/lab05/people.json --out data/out/lab06/people_from_json.csv
# python3 -m src.lab06.cli_convert csv2json --in data/samples/lab05/people.csv --out data/out/lab06/people_from_csv.json
# python3 -m src.lab06.cli_convert csv2xlsx --in data/samples/lab05/people.csv --out data/out/lab06/people_from_csv.xlsx