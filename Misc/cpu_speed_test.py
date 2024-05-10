
from multiprocessing import Pool, cpu_count
from datetime import datetime

def stress_test(args):
    cpu, value = args
    start_time = datetime.now()
    for i in range(value):
        value = value * i
    print(f"cpu: {cpu} time: {datetime.now() - start_time}")


if __name__ == '__main__':

    start_time = datetime.now()
    cpu_count = cpu_count()
    with Pool(cpu_count) as mp_pool:
        mp_pool.map(stress_test, [(cpu, 100000000) for cpu in range(cpu_count)])
        
    print(f"total: {datetime.now() - start_time}")

