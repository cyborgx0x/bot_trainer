source_dir = "images"
val_dir = "val"
train_dir = "train"
import os
import subprocess
os.makedirs(val_dir, exist_ok=True)
os.makedirs(train_dir, exist_ok=True)
train_split = 0.8
image_files = [f for f in os.listdir(source_dir) if f.endswith('.jpg') or f.endswith('.jpeg') or f.endswith('.png')]

num_train = int(len(image_files) * train_split)
train_image_files = image_files[:num_train]
val_image_files = image_files[num_train:]

with open("train.txt", "w") as f:
    for i in train_image_files:
        f.write(f"train\{i}\n")
        os.system(f'copy "images\{i}" "train\{i}"')
    f.close()

with open("val.txt", "w") as f:
    for i in val_image_files:
        print(i)
        f.write(f"val\{i}\n")
        os.system(f'copy "images\{i}" "val\{i}"')

    f.close()