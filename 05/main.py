import math
import time
from scipy.optimize import bisect, newton

# Funkce 1: Kvadratická funkce s jedním kořenem


def func1(x):
    return x**2 - 4*x + 4

# Funkce 2: Exponenciální funkce s kořenem


def func2(x):
    return math.exp(x) - 2

# Funkce 3: Sinusová funkce s kořenem


def func3(x):
    return math.sin(x)

# Uzavřená metoda - metoda bisekce


def closed_method(func, a, b, tol=1e-6):
    start_time = time.time()
    root = bisect(func, a, b, xtol=tol)
    end_time = time.time()
    return root, end_time - start_time

# Otevřená metoda - Newtonova metoda


def open_method(func, x0, tol=1e-6):
    start_time = time.time()
    root = newton(func, x0, tol=tol)
    end_time = time.time()
    return root, end_time - start_time

# Nastavení počátečních intervalů pro každou funkci


interval_func1 = (0, 5)
interval_func2 = (-1, 1)
interval_func3 = (0, math.pi)

# Testování uzavřené metody
print("Uzavřená metoda (metoda půlení intervalu):")
for i, func in enumerate([func1, func2, func3], 1):
    try:
        root, time_taken = closed_method(func, *globals()[f"interval_func{i}"])
        print(f"Kořen funkce {i}: {root}, časová náročnost: {time_taken}s")
    except ValueError as e:
        print(f"Funkce {i}: {e}")

# Testování otevřené metody
print("\nOtevřená metoda (Newtonova metoda):")
for i, func in enumerate([func1, func2, func3], 1):
    root, time_taken = open_method(func, 1)
    print(f"Kořen funkce {i}: {root}, časová náročnost: {time_taken}s")
