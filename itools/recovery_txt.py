import os
import shutil

if __name__ == '__main__':
    src_dir = '/data/YOLOV5/VOCdevkit/small9/new_lines/black_wire/obj_train_data'
    std_dir = '/mnt/projects/yolov5-6.1/img_data/small_data_pro'
    n = 0
    ll = []

    for file in os.listdir(std_dir):
        if file.endswith('txt') and (
                file.startswith('blk_') or file.startswith("bigger_") or file.startswith('labels_')):
            ll.append(file)

    for i in os.listdir(src_dir):
        if i in ll:
            n+=1
            shutil.copy(os.path.join(src_dir, i), os.path.join(std_dir, i))
    print(n)