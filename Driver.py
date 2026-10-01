from PIL import Image
import numpy as np
import os
from Processor import FindBestImage
from Processor import PrecomputeSampleAverages

# Loading the images:


target_cols=3000
target_rows=3000
sample_rows=10
sample_cols=10

target_image=Image.open("target.png").resize((target_cols, target_rows)).convert("RGB") # MODIFY TARGET SIZE!

samples=[]

samples_folder='/var/home/andrei/Desktop/Programare/Python/ImageMosaic/SamplesFolder'

sample_count=len(os.listdir(samples_folder))

for i in os.listdir(samples_folder):
    samples.append(Image.open( f"{samples_folder}/{i}").resize(size=(sample_cols, sample_rows ) ).convert("RGB") )
    # MODIFY SAMPLE SIZE!

# target_image.show()

necc_rows=int(target_rows/sample_rows) # How many rows of images do we need to choose
necc_cols=int(target_cols/sample_cols) # How many columns of images do we need to choose

print(f'O sa avem nevoie de {(target_rows*target_cols)/(sample_cols*sample_rows) :0.0f} de imagini!')
print(f'Avem {sample_count} sample-uri!')

current_image=Image.new('RGB',(target_cols,target_rows))
#current_image.show()

sample_averages = PrecomputeSampleAverages(samples)

for r in range(necc_rows):
    for c in range(necc_cols):
        box=(c*sample_cols, r*sample_rows, (c+1)*sample_cols, (r+1)*sample_rows)
        target_crop=target_image.crop(box)
        index=FindBestImage(target_crop, sample_averages)
        current_image.paste(samples[index],box)

current_image.save("result.png")
print("Gata!")
current_image.show()