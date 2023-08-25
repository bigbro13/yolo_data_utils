import os

def parse_txt(file):
    with open(file, 'r') as f:
        lines = f.readlines()
    if lines:
        os.remove(file)
        for line in lines:
            class_id, x_center, y_center, width, height = map(float, line.strip().split())
            with open(file, "a") as f1:
                f1.write(str(int((class_id))) + ' ' + str(x_center) + ' ' + str(y_center) + ' ' + str(
                    width * 1.12) + ' ' + str(height * 1.12)+'\n')


if __name__ == '__main__':
    file_dir = '/mnt/projects/yolov5-6.1/img_data/small_data_pro'
    ll = []

    for file in os.listdir(file_dir):
        if file.endswith('txt') and (
                file.startswith('blk_') or file.startswith("bigger_") or file.startswith('labels_')):
            ll.append(os.path.join(file_dir, file))
    print(len(ll))
    for i in ll:
        parse_txt(i)
