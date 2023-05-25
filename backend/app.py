from flask import Flask, jsonify, request, flash
from flask_cors import CORS, cross_origin
from p2 import knn_h, knn_r, crear_insertar
from base64 import encodebytes, b64encode
from PIL import Image
import json
import os
import io
import time

# configuration
UPLOAD_FOLDER = './uploads/'
QUERY_FOLDER = './query/'
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'

cors = CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

@app.route('/')
def home():
    return '¡Bienvenido Profesor!'

def get_response_image(image_path):
    with open(image_path, "rb") as image_file:
        base64_image = b64encode(image_file.read()).decode('utf-8')
    return base64_image

@app.route('/queryImages', methods=['POST'])
@cross_origin()
def query_images():
    query = request.files['file']
    k = request.args.get('k')

    query.save(os.path.join(app.config['QUERY_FOLDER'], query.filename))

    start = int(round(time.time() * 1000))
    result = knn_r("query/" + query.filename, int(k))
    end = int(round(time.time() * 1000))

    encoded_images = []
    #knn_r: con r tree
    #knn_h: secuencial

    for re in result:
        encoded_images.append({'id': re['id'], 'image': get_response_image('uploads/' + re['name'])})

    return jsonify({'images': result, 'encoded-images': encoded_images, 'execTime': end-start})

@app.route('/uploadImages', methods=['POST'])
@cross_origin()
def index_images():
    os.system("rm -rf ./uploads/* && rm -rf ./query/* && rm rtree.dat rtree.idx nombres.txt names.txt")
    print(request.files)
    images = request.files.getlist('files')
    nombres = open('names.txt', 'w');
    for file in images:
        print('image name:', file.filename)
        nombres.write(file.filename)
        nombres.write('\n')
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    nombres.close()
    
    start = int(round(time.time() * 1000))
    crear_insertar()
    end = int(round(time.time() * 1000))

    return jsonify({'execTime': end-start})

@app.route('/reset', methods=['GET'])
@cross_origin()
def reset():
    os.system("rm -rf ./uploads/* && rm -rf ./query/* && rm rtree.dat rtree.idx nombres.txt names.txt")
    return ':)'

if __name__ == '__main__':
    app.run(host="0.0.0.0")

