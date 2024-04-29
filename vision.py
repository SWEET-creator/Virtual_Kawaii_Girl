from ultralytics import YOLO
import torch
import cv2
from ultralytics.yolo.data.augment import LetterBox
from ultralytics.yolo.utils.plotting import Annotator, colors
from ultralytics.yolo.utils import ops
from copy import deepcopy
import numpy as np
import matplotlib.pyplot as plt

model = YOLO("./vision/models/yolov8n.pt")
cap = cv2.VideoCapture(0)
labels = []

def preprocess(img, size=640):
        img = LetterBox(size, True)(image=img)
        img = img.transpose((2, 0, 1))[::-1]  # HWC to CHW, BGR to RGB
        img = np.ascontiguousarray(img)  # contiguous
        img = torch.from_numpy(img)
        img = img.float()  # uint8 to fp16/32
        img /= 255  # 0 - 255 to 0.0 - 1.0
        return img.unsqueeze(0)

def postprocess(preds, img, orig_img):
    preds = ops.non_max_suppression(preds,
                                    0.25,
                                    0.8,
                                    agnostic=False,
                                    max_det=100)

    for i, pred in enumerate(preds):
        shape = orig_img.shape
        pred[:, :4] = ops.scale_boxes(img.shape[2:], pred[:, :4], shape).round()

    return preds

def drow_bbox(pred, names, annotator):
    labels = []
    for *xyxy, conf, cls in reversed(pred):
        c = int(cls)  # integer class
        label =  f'{names[c]} {conf:.2f}'
        labels.append(names[c])

        annotator.box_label(xyxy, label, color=colors(c, True))
    return labels

def get_labels():
    global labels
    return labels

def main():
    global labels
    while True:
        ret, img = cap.read()
        origin = deepcopy(img)
        annotator = Annotator(origin,line_width=1,example=str(model.model.names))
        img = preprocess(img)
        preds = model.model(img, augment=False)
        preds = postprocess(preds,img,origin)
        labels = drow_bbox(preds[0], model.model.names, annotator)
        cv2.imshow("test",origin)
        cv2.waitKey(1)

        # qを押したら終了
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


if __name__ == "__main__":
    main()