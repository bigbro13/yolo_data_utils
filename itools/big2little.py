import os
import cv2


def parse_txt(file, little_path):
    img_name = file.replace('.txt', '.jpg')
    with open(file, 'r') as f:
        lines = f.readlines()

    image = cv2.imread(img_name)
    print(os.path.split(img_name)[-1])
    for line in lines:
        class_id, x_center, y_center, width, height = map(float, line.strip().split())
        left = int((x_center - width / 2) * image.shape[1])
        top = int((y_center - height / 2) * image.shape[0])
        right = int((x_center + width / 2) * image.shape[1])
        bottom = int((y_center + height / 2) * image.shape[0])
        object_image = image[top-5:bottom+5, left-5:right+5]
        cv2.imwrite(f'{little_path}/' + os.path.split(img_name)[-1], object_image)


def big2little(big_path, little_path):
    big_file_list = os.listdir(big_path)
    txt_files = []

    for big_txt in big_file_list:
        if big_txt.endswith('.txt'):
            txt_files.append(os.path.join(big_path, big_txt))

    for txt_file in txt_files:
        parse_txt(txt_file, little_path)


if __name__ == '__main__':
    big_path = '/data/YOLOV5/VOCdevkit/big10/labels_off/obj_train_data'
    little_path = '/data/YOLOV5/VOCdevkit/small9/new_lines'
    big2little(big_path, little_path)
