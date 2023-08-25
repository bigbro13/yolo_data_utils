import cv2
import torch
from pathlib import Path

# 定义模型路径
model_weights = '/mnt/projects/data/SJZ/CHM/CHM_2/CHM_s/runs/train/CHM_2_s8/weights/RP44010020000002_side_719.pt'

# 加载自定义的YOLOv5模型
model = torch.hub.load('ultralytics/yolov5', 'RP44010020000002_side_719.pt', path=model_weights)
# 打开视频流（0代表摄像头，或者传入视频文件路径）
video_stream = cv2.VideoCapture('rtsp://192.168.52.242/media/video1')

frame_count = 0
while True:
    ret, frame = video_stream.read()

    if not ret:
        break

    frame_count += 1

    # 仅在第5帧时进行目标检测
    if frame_count == 5:
        # 对帧进行目标检测
        results = model(frame)

        # 处理检测结果并绘制边界框
        processed_frame = results.imgs[0]

        # 显示结果
        cv2.imshow('Custom YOLOv5 Object Detection', processed_frame)

        frame_count = 0  # 重置帧计数

    # 退出循环（按下'q'键）
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_stream.release()
cv2.destroyAllWindows()

