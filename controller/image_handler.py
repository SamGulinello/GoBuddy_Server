import torch
import pandas

# Load the Object Detection Model
model = torch.hub.load('yolov5', 'custom', path='yolov5/runs/train/exp11/weights/best.pt', source='local')

def image_handler(filePath):
    
    # Perform the Object Recognition
    results = model(filePath)

    return results