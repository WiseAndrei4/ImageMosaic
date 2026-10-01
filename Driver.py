from PIL import Image
import numpy as np
import os
from Processor import FindBestImage

# Loading the images:


target_cols=3000
target_rows=3000
sample_rows=60
sample_cols=60

target_image=Image.open("target.png").resize((target_rows, target_cols)).convert("RGB") # MODIFY TARGET SIZE!

target_image=np.array(target_image)

samples=np.array([])
samples_folder='/var/home/andrei/Desktop/Programare/Python/ImageMosaic/SamplesFolder'
for i in os.listdir(samples_folder):
    samples=np.append(samples, np.array( Image.open( f"{samples_folder}/{i}").resize(size=(sample_rows, sample_cols ) ).convert("RGB") ) )
    # MODIFY SAMPLE SIZE!

# target_image.show()

necc_rows=int(target_rows/sample_rows) # How many rows of images do we need to choose
necc_cols=int(target_cols/sample_cols) # How many columns of images do we need to choose

print(f'O sa avem nevoie de {target_rows*target_cols/sample_cols/sample_rows :0.0f} de imagini!')

current_image=Image.new('RGB',(target_rows,target_cols))
#current_image.show()

print(samples.size)

for i in range(necc_rows):
    for j in range(necc_cols):
        index=FindBestImage(target_image[i*sample_rows:(i+1)*sample_rows][j*sample_cols:(j+1)*sample_cols], samples)
