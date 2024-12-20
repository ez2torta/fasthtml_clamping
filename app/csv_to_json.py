import csv
import json

def csv_to_json(csv_file_path, json_file_path):
    # Leer el archivo CSV y convertir a lista de diccionarios
    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data = [row for row in csv_reader]
    
    # Guardar los datos como JSON
    with open(json_file_path, mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)

# Ejemplo de uso
csv_to_json('./csv_files/productos.csv', './json_files/productos.json')
