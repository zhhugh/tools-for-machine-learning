import os
folder_path = r'C:\Users\zhouhan\Desktop\tmp\people\labels'
save_path = r'C:\Users\zhouhan\Desktop\tmp\people\label_change'
filenames = os.listdir(folder_path)
labels = []
for filename in filenames:
    with open(os.path.join(folder_path, filename), 'r') as f:
        label = []
        for line in f.readlines():
            line = line.split(' ')
            if line[0] == '0':
                line[0] = '1'
            else:
                line[0] = '0'
            label.append(line)
        labels.append((filename, label))

if not os.path.exists(save_path):
    os.mkdir(save_path)

for label in labels:
    with open(os.path.join(save_path, label[0]), 'a+') as f:
        for line in label[1]:
            f.write(" ".join(line))




