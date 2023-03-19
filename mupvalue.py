from multiprocessing import Process, Value

def func(counter):
    with counter.get_lock():
        counter.value += 1

if __name__ == '__main__':
    counter = Value('i', 0)
    processes = [Process(target=func, args=(counter,)) for i in range(100)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    print(f'Progress: {counter.value}/10')




