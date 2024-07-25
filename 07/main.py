import numpy as np

# Počet náhodných bodů
num_samples = 1000000

# Generování náhodných bodů v jednotkovém čtverci
x = np.random.uniform(-1, 1, num_samples)
y = np.random.uniform(-1, 1, num_samples)

# Určení bodů uvnitř jednotkového kruhu
inside_circle = x**2 + y**2 <= 1

# Výpočet přibližné hodnoty pi
pi_estimate = 4 * np.sum(inside_circle) / num_samples

print(f"Odhadovaná hodnota pi: {pi_estimate}")
