from ultralytics import YOLO


model = YOLO("yolov8x.pt")  # load a pretrained model (recommended for training)

# Use the model
model.train(data="config.yaml", epochs=20)  # train the model