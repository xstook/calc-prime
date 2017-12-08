#!/usr/bin/env python3

# Author: Michael Santoro
# Start Date: December 5, 2017

import time
import math
import argparse
import multiprocessing as mp
from multiprocessing import Process, Queue, Pool


def is_prime(n):
    """Return 'True' if 'n' is a prime number. False otherwise."""
    if n == 1:
        return None #False # 1 is not prime

    # If it's even and not 2, then it's not prime
    if n == 2:
        return n #True
    if n > 2 and n % 2 == 0:
        return None #False
    
    max_divisor = math.floor(math.sqrt(n))
    for d in range(3, 1 + max_divisor, 2):
        if n % d == 0:
            return None #False

    return n #True




def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--start", help="Specify the starting number.")
    parser.add_argument("-p", "--processes", type=int, help="Specify the number of processes to use. If not specified, max amount will be used.")
    parser.add_argument("-b", "--benchmark", help="Benchmark mode.", action="store_true")
    args = parser.parse_args()
    



    if args.benchmark:
        start_time = time.time()
        for n in range(10000001):
            if is_prime(n) is not None:
                print("\rLargest prime found is " + "{:,}".format(n) + "  ", end="")
        print("Time taken in seconds: " + str(time.time() - start_time))
        print("Score: " + str(1 / (time.time() - start_time) * 1000))



    else:

        processes_count = mp.cpu_count()
        if args.processes is not None:
            processes_count = args.processes

        print("=== Calculating Primes ===")
        print("Utilizing " + str(processes_count) + " parallel processes.")

        process_pool = Pool(processes=processes_count)

        start_time = time.time()
        start_number = 2
        if args.start is not None:
            start_number = int(args.start.replace(",",""))
        while(True):
            process_results = [process_pool.apply_async(is_prime, args=(n,)) for n in range(start_number, start_number + processes_count)]
            start_number = start_number + processes_count

            for p in process_results:
                prime = p.get()
                if prime is not None:
                    print("\rLargest prime found is " + "{:,}".format(prime) + "  ", end='')
                #print(p.get())


        time_elapsed = time.time() - start_time
        print(str(time_elapsed) + " taken")







if __name__ == "__main__":
    main()
