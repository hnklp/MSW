import time
import numpy as np
import sympy as sp
from scipy import integrate

# Úlohy:
# 1. Výpočet faktoriálu
# 2. Výpočet sinusové funkce
# 3. Numerická integrace
# 4. Řešení symbolické rovnice
# 5. Maticové násobení

def standard_python_factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def numpy_factorial(n):
    return np.prod(np.arange(1, n+1))

def standard_python_sin(x):
    return sum([(-1)**i * x**(2*i+1) / np.prod(np.arange(1, 2*i+2)) for i in range(10)])

def numpy_sin(x):
    return np.sin(x)

def standard_python_integration():
    return sum([i**2 for i in range(10000)])

def scipy_integration():
    return integrate.quad(lambda x: x**2, 0, 10000)[0]

def standard_python_solve_equation():
    x = sp.Symbol('x')
    equation = x**2 - 4
    return sp.solve(equation, x)

def sympy_solve_equation():
    x = sp.Symbol('x')
    equation = x**2 - 4
    return sp.solve(equation, x)

def standard_python_matrix_multiplication(a, b):
    result = [[0] * len(b[0]) for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]
    return result

def numpy_matrix_multiplication(a, b):
    return np.dot(a, b)

start_time = time.perf_counter()
result1 = standard_python_factorial(10)
end_time = time.perf_counter()
print("Výpočet faktoriálu v čistém Pythonu:", result1, "Čas:", end_time - start_time, "sekund")

start_time = time.perf_counter()
result2 = numpy_factorial(10)
end_time = time.perf_counter()
print("Výpočet faktoriálu pomocí NumPy:", result2, "Čas:", end_time - start_time, "sekund")

start_time = time.perf_counter()
result3 = standard_python_sin(np.pi/4)
end_time = time.perf_counter()
print("Výpočet sinusové funkce v čistém Pythonu:", result3, "Čas:", end_time - start_time, "sekund")

start_time = time.perf_counter()
result4 = numpy_sin(np.pi/4)
end_time = time.perf_counter()
print("Výpočet sinusové funkce pomocí NumPy:", result4, "Čas:", end_time - start_time, "sekund")

start_time = time.perf_counter()
result5 = standard_python_integration()
end_time = time.perf_counter()
print("Numerická integrace v čistém Pythonu:", result5, "Čas:", end_time - start_time, "sekund")

start_time = time.perf_counter()
result6 = scipy_integration()
end_time = time.perf_counter()
print("Numerická integrace pomocí SciPy:", result6, "Čas:", end_time - start_time, "sekund")

start_time = time.perf_counter()
result7 = standard_python_solve_equation()
end_time = time.perf_counter()
print("Řešení symbolické rovnice v čistém Pythonu:", result7, "Čas:", end_time - start_time, "sekund")

start_time = time.perf_counter()
result8 = sympy_solve_equation()
end_time = time.perf_counter()
print("Řešení symbolické rovnice pomocí SymPy:", result8, "Čas:", end_time - start_time, "sekund")

# Pro maticové násobení vytvoříme náhodné matice
a = np.random.rand(100, 100)
b = np.random.rand(100, 100)

start_time = time.perf_counter()
result9 = standard_python_matrix_multiplication(a, b)
end_time = time.perf_counter()
print("Maticové násobení v čistém Pythonu: Prvních 5x5 elementů")
for row in result9[:5]:
    print(row[:5])
print("Čas:", end_time - start_time, "sekund")

start_time = time.perf_counter()
result10 = numpy_matrix_multiplication(a, b)
end_time = time.perf_counter()
print("Maticové násobení pomocí NumPy: Prvních 5x5 elementů")
print(result10[:5, :5])
print("Čas:", end_time - start_time, "sekund")