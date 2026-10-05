""" MA3.py

Student:
Mail:
Reviewed by:
Date reviewed:

"""
import random
import matplotlib.pyplot as plt
import math as m
import concurrent.futures as future
from statistics import mean 
from time import perf_counter as pc

# Exc1
def approximate_pi(n):
    I = 0
    x_in = []
    y_in = []
    x_ut = []
    y_ut = []

    for _ in range(n):
         x = random.uniform(-1,1)
         y = random.uniform(-1,1)
         if x**2 + y**2 <= 1:
              I += 1
              x_in.append(x)
              y_in.append(y)
         else:
              x_ut.append(x)
              y_ut.append(y)

    plt.scatter(x_ut, y_ut, color = "red")
    plt.scatter(x_in, y_in, color = "Blue")
    plt.savefig(F"pi är ungefär för {n}")

    pi_approx = 4 * (I/n)

    return pi_approx

# Exc2, approximation
def sphere_volume(n, d): 
    points = ([random.uniform(-1, 1) for _ in range(d)] for _ in range(n))

    inside = sum(1 for p in points if sum(map(lambda x: x**2, p)) <= 1)

    return (inside / n) * (2 ** d)


#Exc2, real value
def hypersphere_exact(n, d):

    return (m.pi ** (d / 2)) / m.gamma(d / 2 + 1)

#Exc3: numba version
def sphere_volume_numba(n:int, d:int)->float:
    inside = 0
    for _ in range(n):
        sum_sq = 0.0
        for _ in range(d):
            sum_sq += random.uniform(-1, 1)**2
        if sum_sq <= 1.0:
            inside += 1
            
    return (inside / n) * (2**d)

#Exc4: parallel code - parallelize actual computations by splitting data
def sphere_volume_parallel(n, d, np=10):
    chunk_size = n // np
    args_n = [chunk_size] * np
    args_d = [d] * np
    with future.ProcessPoolExecutor(max_workers=np) as executor:

        volumes = list(executor.map(sphere_volume, args_n, args_d))

    return mean(volumes)
    
def main():
    # Exc1
    dots = [1000, 10000, 100000]
    for n in dots:
        approximate_pi(n)

    # Exc2
    n = 100000
    d = 2
    sphere_volume(n, d)
    print(f"Actual volume of {d} dimentional sphere = {hypersphere_exact(n,d)}")

    n = 100000
    d = 11
    sphere_volume(n, d)
    print(f"Actual volume of {d} dimentional sphere = {hypersphere_exact(n,d)}")

    # Exc3
    n = 1000000
    d = 11
    start = pc()
    sphere_volume(n, d)
    stop = pc()
    print(f"Exc3: Sequential time of {d} and {n}: {stop-start}")
    print("What is numba time?")

    # Exc4
    n = 1000000
    d = 11
    start = pc()
    sphere_volume(n, d)
    stop = pc()
    print(f"Exc4: Sequential time of {d} and {n}: {stop-start}")
    print("What is parallel time?")

    
    

if __name__ == '__main__':
	main()
