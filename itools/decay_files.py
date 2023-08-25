import os
import random
import argparse
import shutil
import threading

# via_list = ['ha']


def decay(files, save_path):
    for decayed_num in files:
        shutil.copy(decayed_num, save_path)
        if decayed_num.endswith('.jpg'):
            name = decayed_num.replace('.jpg', '.txt')
        else:
            name = decayed_num.replace('.PNG', '.txt')
        if name.endswith('.txt') and os.path.exists(name):
            shutil.copy(name, save_path)


def multi_thread_copy_files(images_path, save_path, num_threads, max_num,crease_num):
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    # 获取文件夹下面所有的文件
    total_images = []
    # 添加需要移动的文件名
    thread_images = []
    # 为了计算每个类别图片是否达到5000
    d = {}
    for i in os.listdir(images_path):
        if i.endswith('.jpg') or i.endswith('.PNG'):
            total_images.append(i)

    num_percent = int(len(total_images) * percent)
    print(num_percent)
    # 随机抽取一部分数据
    decayed_nums = random.sample(total_images, num_percent)
    # 添加数据到多线程移动的列表
    for image in decayed_nums:
        for i in via_list:
            if image.startswith(i):
                if d.get(i, 1) <= max_num:
                    d[i] = d.get(i, 1) + 1
                    thread_images.append(os.path.join(images_path, image))
                else:
                    continue

        for j in decay_via:
            if image.startswith(j):
                if d.get(j, 1) <= crease_num:
                    d[j] = d.get(j, 1) + 1
                    thread_images.append(os.path.join(images_path, image))
                else:
                    continue


    print([k for k in d.items()])
    num_files = len(thread_images)
    print(num_files)
    file_per_thread = num_files // num_threads + (1 if num_files % num_threads > 0 else 0)

    threads = []
    for i in range(num_threads):
        start = i * file_per_thread
        end = (i + 1) * file_per_thread if i < num_threads - 1 else num_files
        t = threading.Thread(target=decay, args=(thread_images[start:end], save_path))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()


def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--save_path', type=str, default=r'C:\Users\Admin\Desktop\22\img',
                        help='save path')  # 训练及验证标签存放位置
    parser.add_argument('--images_path', type=str, default=r'C:\Users\Admin\Desktop\22\obj_train_data',
                        help='images_path')  # 图片的存放位置（绝对路径）
    parser.add_argument('--percent', type=float, default=0.7, help='percent')  # 训练的数据的比列
    parser.add_argument('--max_num', type=int, default=2000, help='max num of every label')  # 所有类别的最大图片数量
    parser.add_argument('--crease_num',type=int, default=1200, help='max num of every label')
    opt = parser.parse_args()
    return opt


if __name__ == '__main__':
    opt = parse_opt()
    percent = opt.percent
    images_path = opt.images_path
    save_path = opt.save_path
    max_num = opt.max_num
    crease_num = opt.crease_num
    num_threads = 8
    via_list = []
    via_total = ["new_lamb"]
    # via_total = ["A_", "AL", "auto1", "good", "guo", "res_", "resi", "auto2",
    #             "PLON", "PLOFF", "SON", "SOFF", "SR", "VV", "AV","V_","labels_off","labels_on"]
    # decay_via = ['PLON','PLOFF']
    # via_total = ['lamoff', 'lampon', "power","sr", "switchoff","switchon", "res","a_", "v2", 'p_','s_','v1']
    # decay_via = ['labels_off','bigger_']
    # 石家庄化学实验二
    #via_total = ['beaker_s', 'glass_rod']
    decay_via = []
    for x in via_total:
        if x not in decay_via:
            via_list.append(x)
    print(via_list)
    multi_thread_copy_files(images_path, save_path, num_threads, max_num, crease_num)
