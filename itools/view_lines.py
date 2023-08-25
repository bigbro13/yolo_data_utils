import os

# file = '/data/YOLOV5/VOCdevkit/small9/train.txt'
# with open(file, 'r') as f:
#     content = f.readlines()
#     print(len(content))



lst_jpg = os.listdir('/data/data/SJZ/CHM/CHM_4/CHM_s/train_data')
print(len(lst_jpg))
l=[]
for i in lst_jpg:
    if i.endswith('.jpg'):
        l.append(i)
print(len(l))
