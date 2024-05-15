import time
import numpy as np
import sympy as sp
from scipy.integrate import quad

# Vektorová operace: Skalární součin dvou vektorů
def dot_product_python(a, b):
    return sum(x * y for x, y in zip(a, b))

def dot_product_numpy(a, b):
    return np.dot(a, b)

# Symbolická manipulace: Derivace funkce
def derivative_python(f, x, h=1e-5):
    return (f(x + h) - f(x - h)) / (2 * h)

# Numerická integrace: Výpočet určitého integrálu
def trapezoidal_rule_python(f, a, b, n):
    h = (b - a) / n
    integral = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        integral += f(a + i * h)
    return integral * h

# Základní operace s čísly: Výpočet n-tého Fibonacciho čísla
def fibonacci_python(n):
    if n <= 1:
        return n
    else:
        a, b = 0, 1
        for _ in range(n-1):
            a, b = b, a + b
        return b

# Řešení soustavy lineárních rovnic
def gauss_elimination_python(A, b):
    n = len(b)
    for i in range(n):
        max_row = max(range(i, n), key=lambda r: abs(A[r][i]))
        A[i], A[max_row] = A[max_row], A[i]
        b[i], b[max_row] = b[max_row], b[i]

        for j in range(i+1, n):
            factor = A[j][i] / A[i][i]
            b[j] -= factor * b[i]
            for k in range(i, n):
                A[j][k] -= factor * A[i][k]

    x = [0 for _ in range(n)]
    for i in range(n-1, -1, -1):
        x[i] = (b[i] - sum(A[i][j] * x[j] for j in range(i+1, n))) / A[i][i]
    return x

# Úlohy k řešení
tasks = [
    ("Vektorová operace: Skalární součin dvou vektorů", dot_product_python, dot_product_numpy),
    ("Symbolická manipulace: Derivace funkce", derivative_python, sp.diff),
    ("Numerická integrace: Výpočet určitého integrálu", trapezoidal_rule_python, quad),
    ("Základní operace s čísly: Výpočet n-tého Fibonacciho čísla", fibonacci_python, None),
    ("Řešení soustavy lineárních rovnic", gauss_elimination_python, None),
]

# Spuštění a měření časů
for task, python_func, library_func in tasks:
    print("\nÚloha:", task)
    if library_func:
        if task.startswith("Symbolická manipulace") or task.startswith("Numerická integrace"):
            x = sp.symbols('x')
            f = x**2 + 2*x + 1
            start_time = time.time()
            result = library_func(f, -1, 1)  # Pro integraci zvolte vhodné meze
            end_time = time.time()
        else:
            a = np.array([1, 2, 3])
            b = np.array([4, 5, 6])
            start_time = time.time()
            result = library_func(a, b)
            end_time = time.time()
    else:
        if task.startswith("Řešení soustavy lineárních rovnic"):
            A = [[2, -1, 0], [-1, 2, -1], [0, -1, 2]]
            b = [1, 0, 1]
            start_time = time.time()
            result = python_func(A, b)
            end_time = time.time()
        else:
            start_time = time.time()
            result = python_func(30)  # Pro Fibonacci: n = 30
            end_time = time.time()
    print("Čas:", end_time - start_time)
