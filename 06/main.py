import wave
import struct
import numpy as np


def audio_random(seed_audio_file):
    # Načtení zvukového souboru
    with wave.open(seed_audio_file, 'rb') as audio:
        frames = audio.readframes(-1)
        samples = struct.unpack('h' * audio.getnframes(), frames)

    # Konverze na numpy pole
    samples_array = np.array(samples)

    # Normalizace hodnot na interval <-1, 1>
    normalized_samples = samples_array / np.max(np.abs(samples_array))

    # Použití hodnot jako základ pro generování pseudonáhodných čísel
    for sample in normalized_samples:
        yield int(sample * (2 ** 32 - 1))  # Přizpůsobení hodnot na rozsah pseudonáhodných čísel


# Použití generátoru
audio_file = "smrt.wav"  # Název vašeho zvukového souboru
random_generator = audio_random(audio_file)

# Generování náhodných čísel
for _ in range(10):
    print(next(random_generator))
