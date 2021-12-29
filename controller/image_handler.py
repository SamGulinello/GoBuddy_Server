import torch
import pandas

# Load the Object Detection Model
model = torch.hub.load('yolov5', 'custom', path='data/model/best.pt', source='local')

def perform_detection(filePath):
    
    # Perform the Object Recognition
    results = model(filePath)

    return results

def get_class(data):
    # Get class name from image data
    imgDict = data.pandas().xyxy[0].to_dict()
    objectName = imgDict['name'][0]

    return objectName