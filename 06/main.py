import wave
import numpy as np
import random

#Získání semínka z WAV souboru
def get_seed_from_wav(file_path):
    with wave.open(file_path, 'rb') as wav_file:
        frames = wav_file.readframes(wav_file.getnframes())
        wave_data = np.frombuffer(frames, dtype=np.int16)
        seed = int(np.sum(np.abs(wave_data)))
        return seed

#Generátor náhodných čísel
def random_number_generator(seed, n, min_val, max_val):
    random.seed(seed)
    return [random.randint(min_val, max_val) for _ in range(n)]


#Nastavení názvu souboru pro generování a požadovaný počet čísel
wav1 = 'smrt.wav'
wav2 = 'jubilejni_den.wav'
pocet_cisel = 5

#Generace finálního semínka
seed1 = get_seed_from_wav(wav1)
seed2 = get_seed_from_wav(wav2)
seed_f = seed1 + seed2 / np.pi * seed2 / seed1 / random.randint(10, 785410)
print(f'Semínko: {seed_f}')

#Generace náhodných čísel a jejich vypsání
random_numbers = random_number_generator(seed_f, pocet_cisel, random.randint(4566637, 998878667), random.randint(99876545678, 456784567845678))
print(f'Náhodná čísla: {random_numbers}')
