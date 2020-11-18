from PIL import Image
from tensorflow.keras.models import model_from_json
import numpy

def predict_number(model,weights,data):
    
    # Loading model
    json_file = open(model, 'r')
    loaded_model_json = json_file.read()
    model = model_from_json(loaded_model_json)
    # Loading weights
    model.load_weights(weights)
    # Loading images
    img = Image.open(data)
    # Resizing image to the same shape of the images dataset used in the traning model
    img = img.resize((28,28),Image.ANTIALIAS)
    # Convert PIL image to numpy array
    img_convert = list(img.getdata())
    img = numpy.array(img_convert).reshape(img.width,img.height,4)
    # Adding one dimension to the img array. (The input image is (1,width,height,number of rgb channels))
    img = img[:,:,0]
    img = img.reshape(1,img.shape[0],img.shape[1],1)
    # Using the neural network to get the one hot encoding output
    predict = model.predict(img)
    # Getting tha max value in the predict arrays
    number_prediction = predict.argmax()
    
    return number_prediction