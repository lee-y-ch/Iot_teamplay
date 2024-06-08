from ultralytics import YOLO

model = YOLO("yolov8m.pt")

model.train(data = './dataset/YOLODataset/dataset.yaml', epochs=5)