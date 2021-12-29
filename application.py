# Import Necessary Libraries
from flask import Flask, request, render_template
import os

from controller.image_handler import perform_detection, get_class
from controller.db_handler import mongoDB

# Create Necessary Objects
application = Flask(__name__)
db = mongoDB()

# Base Endpoint
@application.route('/', methods=['POST', 'GET'])
def hello_world():
    return render_template('home.html')

# Image Detection Endpoint
@application.route('/image', methods=['POST', 'GET'])
def object_detect():
    if request.method == 'POST':

        # Get Image From Web Request
        data = request.files
        file = data['photo']
        filePath = 'static/' + file.filename
        file.save(os.path.join(filePath))

        # Perform Object Detection
        results = perform_detection(filePath)

        # Get object class
        obj = get_class(results)
        print("OBJECT-> " + obj)
        id =  db.get_id(obj)

        return render_template('results.html', ImgPath = db.get_imgPath(id), Title = db.get_title(id), Description = db.get_description(id))
    
    else:
         return 'Please access endpoint with POST'

if __name__ == "__main__":
    application.run(host="localhost", port=8000, debug=True)


    