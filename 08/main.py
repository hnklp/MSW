import numpy as np


# Definice funkce a její analytické derivace
def f(x):
    return np.sin(x)


def f_prime_analytic(x):
    return np.cos(x)


# Numerické derivace se statickým krokem
def central_difference(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)


# Numerická derivace s adaptabilním krokem
def adaptive_difference(f, x, tol=1e-5):
    h = 0.1
    error = float('inf')

    while error > tol:
        central_diff1 = central_difference(f, x, h)
        central_diff2 = central_difference(f, x, h / 2)

        # Odhad chyby
        error = abs(central_diff1 - central_diff2)

        h /= 2.0  # Zmenšení kroku

    return central_diff2  # Vrácení nejlepšího odhadu


# Bod, ve kterém budeme derivovat
x = np.pi / 4 # 45 stupňů
h = 0.1  # Statický krok

# Analytická derivace
analytic_result = f_prime_analytic(x)

# Numerická derivace s pevným krokem
fixed_step_result = central_difference(f, x, h)

# Numerická derivace s adaptabilním krokem
adaptive_result = adaptive_difference(f, x)

# Výstup výsledků
print(f"Analytická derivace: {analytic_result}")
print(f"Numerická derivace s pevným krokem: {fixed_step_result}")
print(f"Numerická derivace s adaptabilním krokem: {adaptive_result}")
