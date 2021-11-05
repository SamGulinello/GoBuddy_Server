# Import Necessary Libraries
from flask import Flask, request, render_template
import torch
import base64
import os


# Creat Necessary Objects
application = Flask(__name__)
model = torch.hub.load('yolov5', 'custom', path='yolov5/runs/train/exp11/weights/best.pt', source='local')

@application.route('/', methods=['POST', 'GET'])
def hello_world():
    return render_template('home.html')

@application.route('/image', methods=['POST', 'GET'])
def object_detect():
    if request.method == 'POST':
        # Get Image From Web Request
        data = request.files
        file = data['photo']
        filePath = 'static/' + file.filename
        file.save(os.path.join(filePath))
        
        # Perform the Object Recognition
        results = model(filePath)
        results.save('static/')

        return render_template('results.html', file = file.filename)
    
    else:
         return 'Please access endpoint with POST'

if __name__ == "__main__":
    application.run(host="localhost", port=8000, debug=True)


    