from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
import numpy as np
from PIL import Image
from io import BytesIO
import base64
import re
from functions import predict_number

app = Flask(__name__)


@app.route('/')
def Home_get():
    return render_template("home.html")

@app.route('/teste/',methods = ['POST','GET'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def Predict_post():
    

    image_b64 = request.get_json()['imageBase64']
    image_data = re.sub('^data:image/.+;base64,', '', image_b64)
    im = Image.open(BytesIO(base64.b64decode(image_data )))
    predict = predict_number('neuralnetwork_model.json','model_weights.h5',im)

    return jsonify({'predict':int(predict)})

if __name__ == "__main__":
    app.run(threaded=True, port=5000)
