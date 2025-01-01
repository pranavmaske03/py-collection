import multiprocessing
import os
import time

def Fun(No):
    Sum = 0
    print("PID is : ",os.getpid())
    for i in range(No):
        Sum = Sum + (No*No*No)

    return Sum

def main():
    starttime = time.time()
    Arr = [10000000,20000000,30000000,40000000,50000000,6000000,70000000,80000000,90000000,100000000,120000000,130000000]
    Result = []

    p = multiprocessing.Pool()
    Result = p.map(Fun,Arr)
    p.close()
    p.join()

    print(Result)
    endtime = time.time()
    print("Time requred for execution : ",endtime-starttime)
if __name__ == "__main__":
    main()