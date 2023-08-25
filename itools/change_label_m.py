import os
import argparse

def parse_txt(file):
    with open(file, 'r') as f:
        lines = f.readlines()
    if lines:
        os.remove(file)
        for line in lines:
            class_id, x_center, y_center, width, height = map(float, line.strip().split())
            if class_id in [0.0, 1.0,4.0,5.0,6.0,7.0,8.0,9.0]:
                cls_id = class_id
                if class_id == 0.0:
                    cls_id = 0
                if class_id == 1.0:
                    cls_id = 2
                if class_id == 4.0:
                    cls_id = 15
                if class_id == 5.0:
                    cls_id = 14
                if class_id == 6.0:
                    cls_id = 16
                if class_id == 7.0:
                    cls_id = 12
                if class_id == 8.0:
                    cls_id = 3  
                with open(file, "a") as f1:
                    f1.write(str(int(cls_id)) + ' ' + str(x_center) + ' ' + str(y_center) + ' ' + str(
                        width) + ' ' + str(height) + '\n')
            else:
                continue


def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file_dir', type=str, required=True, help='images_path')  # 图片及标签的存放位置（绝对路径）
    opt = parser.parse_args()
    return opt

if __name__ == '__main__':
    opt = parse_opt()
    file_dir = opt.file_dir
    ll = []

    for file in os.listdir(file_dir):
        if file.endswith('txt'):
            ll.append(os.path.join(file_dir, file))
    print(len(ll))
    for i in ll:
        parse_txt(i)
