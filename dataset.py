import csv
import time

def find_min_max():
    with open('dataset.csv') as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        max_sale = max(rows, key=lambda row: float(row['Global_Sales']))
        min_sale = min(rows, key=lambda row: float(row['Global_Sales']))
    return max_sale, min_sale

if __name__ == '__main__':
    start_time = time.time()
    max_sale, min_sale = find_min_max()
    print(f"Max sale: {max_sale['Global_Sales']} (Game: {max_sale['Name']})")
    print(f"Min sale: {min_sale['Global_Sales']} (Game: {min_sale['Name']})")
    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.3f} seconds")
