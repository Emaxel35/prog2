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
from numba import njit

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
    plt.figure()
    plt.scatter(x_ut, y_ut, color = "red")
    plt.scatter(x_in, y_in, color = "Blue")
    plt.savefig(F"pi är ungefär för {n}")
    plt.close()

    pi_approx = 4 * (I/n)

    return pi_approx

# Exc2, approximation
def sphere_volume(n, d):
    I = 0
    for _ in range(n):
        x_val = [random.uniform(-1,1) for _ in range(d)]
        x_kvad = list(map(lambda x: x**2, x_val))
        if sum(x_kvad) <= 1:
               I += 1
        volym = (I/n) * (2**d)
    return volym


#Exc2, real value
def hypersphere_exact(n, d):

    return (m.pi ** (d / 2)) / m.gamma(d / 2 + 1)

#Exc3: numba version
@njit
def sphere_volume_numba(n:int, d:int)->float:
    I = 0
    for _ in range(n):
        x_val = [random.uniform(-1,1) for _ in range(d)]
        x_kvad = list(map(lambda x: x**2, x_val))
        if sum(x_kvad) <= 1:
               I += 1
        volym = (I/n) * (2**d)   
    return volym

#Exc4: parallel code - parallelize actual computations by splitting data
def sphere_volume_parallel(n, d, np=10):
     
     ln = [int(n/np) for _ in range(np)]
     ld = [d for _ in range(np)]

     with future.ProcessPoolExecutor(max_workers=np) as exe:
          resultat = list(exe.map(sphere_volume, ln, ld))
     return mean(resultat)
    
def main():
    # Exc1
    dots = [1000, 10000, 100000]
    for n in dots:
        approximate_pi(n)

    # Exc2
    n = 100000
    d = 2
    print(f"approx volume of {d} dimentional sphere = {sphere_volume(n, d)}")
    print(f"Actual volume of {d} dimentional sphere = {hypersphere_exact(n,d)}")

    n = 100000
    d = 11
    print(f"approx volume of {d} dimentional sphere = {sphere_volume(n, d)}")
    print(f"Actual volume of {d} dimentional sphere = {hypersphere_exact(n,d)}")
    

    # Exc3
    n = 1000000
    d = 11
    
    for x in range(1, 4):
        start = pc()
        sphere_volume(n, d)
        stop = pc()
        print(f"Exc3: Run {x} Sequential time of {d} and {n}: {stop-start}")

    print("What is numba time?")
    for x in range(1, 4):
        start = pc()
        sphere_volume_numba(n, d)
        stop = pc()
        print(f"Exc3: Run {x} Numba time of {d} and {n}: {stop-start}")

    
    # Exc4
    n = 1000000
    d = 11
    start = pc()
    sphere_volume(n, d)
    stop = pc()
    print(f"Exc4: Sequential time of {d} and {n}: {stop-start}")
    print("What is parallel time?")
    start = pc()
    sphere_volume_parallel(n,d,2)
    stop = pc()
    print(f"Exc4: Parallel time of {d} and {n}: {stop-start}")

    
    

if __name__ == '__main__':
	main()
