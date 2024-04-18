import cv2
import time
from ultralytics import YOLO  # ultralyticsのYOLOライブラリをインポート

# カメラの初期化
cap = cv2.VideoCapture(0)

# YOLOモデルの読み込み
model = YOLO('./models/yolov8n.pt')  # YOLOv8のモデルファイルを指定

while True:
    # フレームの取得
    ret, frame = cap.read()

    # モデルによる予測
    results = model(frame)

    # 検出された物体のバウンディングボックスとラベルを描画
    print(results)
    for result in results:
        x1, y1, x2, y2, confidence, class_id = result['xmin'], result['ymin'], result['xmax'], result['ymax'], result['confidence'], result['class_id']
        if confidence > 0.5:  # 信頼度が50%を超えるものだけを表示
            cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
            label = f"{model.names[class_id]}: {confidence:.2f}"
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    # 結果を表示
    cv2.imshow('YOLO Object Detection', frame)

    # qを押したら終了
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    time.sleep(1)

cap.release()
cv2.destroyAllWindows()
