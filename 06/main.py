import wave
import numpy as np
import random


def get_seed_from_wav(file_path):
    # Otevřít wav soubor
    with wave.open(file_path, 'rb') as wav_file:
        # Přečíst data
        frames = wav_file.readframes(wav_file.getnframes())
        # Převést data na numpy pole
        wave_data = np.frombuffer(frames, dtype=np.int16)
        # Vytvořit seed ze součtu absolutních hodnot
        seed = int(np.sum(np.abs(wave_data)))
        return seed


def random_number_generator(seed, n, min_val, max_val):
    # Nastavit seed
    random.seed(seed)
    # Generovat n náhodných celých čísel v zadaném rozsahu
    return [random.randint(min_val, max_val) for _ in range(n)]


# Cesta k vašemu wav souboru
wav1 = 'smrt.wav'
wav2 = 'jubilejni_den.wav'

# Získat seed z wav souboru
seed1 = get_seed_from_wav(wav1)
seed2 = get_seed_from_wav(wav2)
seed_f = seed1 + seed2 / np.pi * seed2 / seed1 / random.randint(10, 50)
print(f'Seed: {seed_f}')

# Generovat 10 náhodných celých čísel v rozsahu od -1000 do 1000 pomocí tohoto seedu
random_numbers = random_number_generator(seed_f, 5, random.randint(4566637, 998878667), random.randint(99876545678, 456784567845678))
print(f'Random Numbers: {random_numbers}')
