from PIL import Image
import numpy as np
from PIL import ImageChops


def PrecomputeSampleAverages(samples):
    """
    Calculeaza culoarea medie (R, G, B) pentru fiecare sample.
    Returneaza o matrice NumPy de dimensiune (sample_count, 3).
    """
    averages = []
    for img in samples:
        arr = np.array(img, dtype=np.float32)
        avg_color = arr.mean(axis=(0, 1))  # Medie pe inaltime si latime
        averages.append(avg_color)
    return np.array(averages)

def FindBestImage(target, sample_averages):
    target_arr=np.array(target, dtype=np.float32)
    target_avg=target_arr.mean(axis=(0,1))

    dist=np.sum((sample_averages-target_avg)**2,axis=1)

    return np.argmin(dist)