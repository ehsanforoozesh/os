import time
import threading
import numpy as np

#Clean the data that we extracted in Part 1.
df = pd.read_csv('data.csv')
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)
df['Price'] = df['Price'].str.replace('$', '').astype(float)

#Perform basic statistical analysis on the data.
mean_price = df['Price'].mean()
median_price = df['Price'].median()
mode_price = df['Price'].mode()[0]
std_price = df['Price'].std()
var_price = df['Price'].var()

#Write a Python program without multithreading to perform some complex data analysis.
def complex_analysis():
    # Simulating a long computation time
    time.sleep(5)
    return np.random.rand(1000000)

start_time = time.time()
result = complex_analysis()
end_time = time.time()
print(f"Without multithreading: {end_time - start_time} seconds")

#Write a Python program with multithreading to perform the same complex data analysis.
def complex_analysis_thread():
    # Simulating a long computation time
    time.sleep(5)
    return np.random.rand(1000000)

start_time = time.time()
threads = []
for i in range(10):
    t = threading.Thread(target=complex_analysis_thread)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

end_time = time.time()
print(f"With multithreading: {end_time - start_time} seconds")

#Compare the execution time of both programs and analyze the results.