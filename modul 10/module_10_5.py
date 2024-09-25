import multiprocessing
from datetime import datetime


def read_info(name):
    all_data = []
    with open(name, 'r') as f:
        while True:
            line = f.readline().rstrip('\n')
            if not line:
                break
            all_data.append(line)


files = [f'./file {num}.txt' for num in range(1, 5)]

# Линейный вызов

start_time = datetime.now()
for file_name in files:
    read_info(file_name)
end_time = datetime.now()
print(end_time - start_time)

# Многопроцессный

if __name__ == '__main__':
    start_time = datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, files)
    end_time = datetime.now()
    print(end_time - start_time)
