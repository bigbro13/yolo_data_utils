import os
import argparse


def rename(images_path, add_via):
    images = os.listdir(images_path)
    for image in images:
        if image.endswith('PNG'):
            os.rename(os.path.join(images_path, image),
                      os.path.join(images_path, add_via + image.replace('PNG', 'jpg')))
        if image.endswith('jpg'):
            os.rename(os.path.join(images_path, image),
                      os.path.join(images_path, add_via + image))
        if image.endswith('txt'):
            os.rename(os.path.join(images_path, image), os.path.join(images_path, add_via + image))


def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--images_path', type=str, required=True, help='images_path')  # 图片及标签的存放位置（绝对路径）
    parser.add_argument('--add_via', type=str, required=True, help='val percent')  #
    opt = parser.parse_args()
    return opt


if __name__ == '__main__':
    opt = parse_opt()
    rename(opt.images_path, opt.add_via)
