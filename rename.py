import os

path = r'C:\Users\zhouhan\Desktop\new_images'
num = 26
for file in os.listdir(path):
    filename = str(num).zfill(5)
    os.rename(os.path.join(path, file), os.path.join(path, str(num).zfill(5) + ".jpg"))
    num += 1
