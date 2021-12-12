# Import Necessary Libraries
from flask import Flask, request, render_template
import os

from controller.image_handler import image_handler

# Creat Necessary Objects
application = Flask(__name__)

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

        # Perform Object Detection
        results = image_handler(filePath)
        results.save('static/')

        return render_template('results.html', file = file.filename)
    
    else:
         return 'Please access endpoint with POST'

if __name__ == "__main__":
    application.run(host="localhost", port=8000, debug=True)


    