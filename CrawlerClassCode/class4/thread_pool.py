from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor

def fn(name):
    for i in range(1000):
        print(name,i)

if __name__ == '__main__':

    with ThreadPoolExecutor(1000000) as t:
        for i in range(10):
            t.submit(fn,name=f"线程{i}")
    print("end")