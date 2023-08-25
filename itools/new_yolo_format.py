import os
import random
import argparse
import shutil


def to_label(save_path, images_path):
    total_images = []
    for i in os.listdir(images_path):
        if i.endswith('.jpg') or i.endswith('.PNG'):
            total_images.append(os.path.join(images_path, i))

    num = len(total_images)
    train_num = int(float(num * train_percent))
    val_num = int(float(num * val_percent))
    trainval_num = train_num + val_num
    print(train_num)
    print(val_num)
    trainval = random.sample(total_images, trainval_num)
    train_list = random.sample(trainval, train_num)
    val_list = random.sample(trainval, val_num)

    if not os.path.exists(save_path):
        os.mkdir(save_path)
    train_txt = open(os.path.join(save_path, 'train.txt'), 'w')
    val_txt = open(os.path.join(save_path, 'val.txt'), 'w')
    for train in train_list:
        train_txt.write(os.path.join(images_path, train) + '\n')
    train_txt.close()
    for val in val_list:
        val_txt.write(os.path.join(images_path, val) + '\n')
    val_txt.close()


def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--save_path', type=str, default='../labels/', help='save path')  # 训练及验证标签存放位置
    parser.add_argument('--images_path', type=str, required=True, help='images_path')  # 图片的存放位置（绝对路径）
    parser.add_argument('--train_percent',type=float, default=0.7, help='train percent')  # 训练的数据的比列
    parser.add_argument('--val_percent', type=float, default=0.3, help='val percent')  # 验证的数据的比列
    opt = parser.parse_args()
    return opt


if __name__ == '__main__':
    opt = parse_opt()
    train_percent = opt.train_percent
    val_percent = opt.val_percent
    to_label(opt.save_path, opt.images_path)
