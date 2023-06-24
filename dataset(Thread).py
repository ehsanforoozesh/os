import pandas as pd
import concurrent.futures
import time

def find_min_max(file):
    df = pd.read_csv(file)
    max_sale = df.loc[df['Global_Sales'].idxmax()]
    min_sale = df.loc[df['Global_Sales'].idxmin()]
    return max_sale, min_sale

if __name__ == '__main__':
    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future1 = executor.submit(find_min_max, 'dataset.csv')
        future2 = executor.submit(find_min_max, 'dataset.csv')
        max_sale1, min_sale1 = future1.result()
        max_sale2, min_sale2 = future2.result()
    print(f"Max sale 1: {max_sale1['Global_Sales']} (Game: {max_sale1['Name']})")
    print(f"Min sale 1: {min_sale1['Global_Sales']} (Game: {min_sale1['Name']})")
    print(f"Max sale 2: {max_sale2['Global_Sales']} (Game: {max_sale2['Name']})")
    print(f"Min sale 2: {min_sale2['Global_Sales']} (Game: {min_sale2['Name']})")
    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.3f} seconds")