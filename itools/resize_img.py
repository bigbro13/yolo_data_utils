import os
import cv2
import argparse
import shutil

def resize_img(img_path):
    img = cv2.imread(img_path)
    height, width = img.shape[:2]
    dec_width = height * scale
    dec = int((width - dec_width) / 2)
    if dec>=0:
        dec_img = img[0:height, dec:width - dec]
        cv2.imwrite(dst_dir + '/' + os.path.split(img_path)[1], dec_img)
    else:
        cv2.imwrite(dst_dir + '/' + os.path.split(img_path)[1], img)
        dec = 0
    return width, dec


def parse_txt(file, x, dec):
    if dec == 0:
        shutil.copy(file,dst_dir + '/' + os.path.split(file)[1])
    else:
        with open(file, 'r') as f:
            lines = f.readlines()
        if lines:
            # os.remove(file)
            for line in lines:
                class_id, x_center, y_center, width, height = map(float, line.strip().split())
                with open(dst_dir + '/' + os.path.split(file)[1], "a") as f1:
                    f1.write(str(int(class_id)) + ' ' + str(round(((x_center * x - dec) / (x - 2 * dec)), 6)) + ' ' + str(
                        round(y_center, 6)) + ' ' + str(round((width * x / (x - 2 * dec)), 6))
                             + ' ' + str(round(height, 6)) + '\n')


def opt_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--images_path', type=str, default=r'',
                        help='images_path')  # 图片的存放位置（绝对路径）
    parser.add_argument('--save_path', type=str, default=r'',
                        help='save path')  # 训练及验证标签存放位置
    opt = parser.parse_args()
    return opt


if __name__ == '__main__':
    scale = 1920 / 1080
    opt = opt_parse()
    file_path = opt.images_path
    dst_dir = opt.save_path
    if not os.path.exists(dst_dir):
        os.mkdir(dst_dir)
    ll = []
    # 获取文件夹
    for P, file_dirs, files in os.walk(file_path):
        for file in files:
            if file.endswith('jpg'):
                ll.append(os.path.join(P, file))
    print(len(ll))
    for i in ll:
        x, dec = resize_img(i)
  
        txt = i.replace('jpg', 'txt')

        if os.path.exists(txt):
            parse_txt(txt, x, dec)
