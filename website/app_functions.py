import graphlib
import pickle, os, random
import numpy as np
from keras.models import load_model
from sklearn.metrics import top_k_accuracy_score
import keras
# from efficientnet.tfkeras import EfficientNetB0, preprocess_input
from sklearn.preprocessing import StandardScaler
import xgboost
import os
import tensorflow as tf
from tensorflow.keras.metrics import top_k_categorical_accuracy 
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.preprocessing import image
from tensorflow.python.keras.backend import set_session
import cv2
from tensorflow.keras.utils import img_to_array
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import load_img, img_to_array

from keras.preprocessing import image
from keras.applications.imagenet_utils import preprocess_input
from tensorflow.keras.models import load_model
import numpy as np
from werkzeug.utils import secure_filename


def get_model(model_path):
    model = load_model(model_path, compile=False)
    return model



################################################skin cancer################################################
# Updated skin cancer prediction function
def pred_skin(path):
    model_path = '/home/cpatwadityasharma/AdityaBackup/medical/website/app_models/skin_model.h5'
    model = get_model(model_path)
    # Load and preprocess the image
    data = load_img(path, target_size=(150, 150))
    data = img_to_array(data)
    data = data / 255.0
    data = np.expand_dims(data, axis=0)
    # Make predictions using the loaded model
    predictions = model.predict(data)
    # Get the class label with the highest probability
    predicted_class = np.argmax(predictions)
    # Assuming you have a binary classification model, round the output to 0 or 1
    predicted_label = np.round(predictions)[0]

    return predicted_label
    
################################################Phenumia################################################ 
def pred_pneumonia(path):
    model_path = '/home/cpatwadityasharma/AdityaBackup/medical/website/app_models/cnn_model.h5'
    model = get_model(model_path)
    # Load and preprocess the image
    data = load_img(path, target_size=(500, 500, 1), color_mode='grayscale')
    data = np.asarray(data).reshape((-1, 500, 500, 1))
    data = data / 255.0
    # Make predictions using the loaded model
    predictions = model.predict(data)
    # Get the class label with the highest probability
    predicted_class = np.argmax(predictions)
    # Assuming you have a binary classification model, round the output to 0 or 1
    predicted_label = np.round(predictions)[0]
    return predicted_label

################################################ Malaria################################################
def pred_malaria(path):
    # Load and resize the image
    data = load_img(path, target_size=(128, 128))
    # Preprocess the image
    data = img_to_array(data)
    data = np.expand_dims(data, axis=0)
    data = data / 255
    # Make the prediction
    predicted = np.round(get_model('/home/cpatwadityasharma/AdityaBackup/medical/website/app_models/InceptionV3.h5').predict(data)[0])[0]
    return predicted

################################################Ocular##################################################
def pred_ocular(path):
    # Load the image and preprocess
    img = load_img(path, target_size=(224, 224))
    img_array = img_to_array(img)
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    model = get_model('/home/cpatwadityasharma/AdityaBackup/medical/website/app_models/ocualr.h5')
    # Make predictions using the loaded model
    predictions = model.predict(img_array)
    # Get the class label with the highest probability
    predicted_class = np.argmax(predictions)
    # Map the class label to a human-readable label based on your label mapping
    label_mapping = {
        0: "Normal",
        1: "Cataract",
        2: "Diabetes",
        3: "Glaucoma",
        4: "Hypertension",
        5: "Myopia",
        6: "Age Issues",
        # Add more labels as needed
    }
    predicted_label = label_mapping.get(predicted_class, "Other")
    return predicted_label
#################################################DR################################################
def pred_dr(path):
    # Load the image and preprocess
    img = load_img(path, target_size=(224, 224))
    img_array = img_to_array(img)
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Load the model
    model = get_model('/home/cpatwadityasharma/AdityaBackup/medical/website/app_models/vgg16.h5')

    # Make predictions using the loaded model
    predictions = model.predict(img_array)

    # Get the class label with the highest probability
    predicted_class = np.argmax(predictions)
    label_mapping = {
        0: "No DR",
        1: "Mild",
        2: "Severe",
        3: "Proliferative DR",
    }
    predicted_label = label_mapping.get(predicted_class, "Other")
    return predicted_label

##################################################Oct################################################ 
def pred_oct(path):
    # Load the image and preprocess
    img = load_img(path, target_size=(150, 150))
    img_array = img_to_array(img)
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    model=(get_model('/home/cpatwadityasharma/AdityaBackup/medical/website/app_models/octa_model.h5'))
    # Make predictions using the loaded model
    predictions = model.predict(img_array)
    # Get the class label with the highest probability
    predicted_class = np.argmax(predictions)
    # Map the class label to a human-readable label based on your label mapping
    label_mapping = {
    0: "Choroidal neovascularization",
    1: "Diabetic macular edema ",
    2: "DRUSEN",
    3: "NORMAL",

}
    predicted_label2 = label_mapping.get(predicted_class, "Other")

    return predicted_label2
#################################################oralcancer################################################
def pred_oral(path):
    # Load the image and preprocess
    img = load_img(path, target_size=(224, 224), color_mode='rgb')
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    model=(get_model('/home/cpatwadityasharma/AdityaBackup/medical/website/app_models/oral cancer-vggg19.h5'))
    # Make predictions using the loaded model
    predictions = model.predict(img_array)
    predicted_class = np.argmax(predictions)
    label_mapping = {0: "benign", 1: "malignant"}
    predicted_label = label_mapping.get(predicted_class, "Other")
    return predicted_label

#################################################pathology################################################   
def ValuePredictor(to_predict_list):
    if len(to_predict_list) == 15:
        page = 'kidney'
        with open('/home/cpatwadityasharma/AdityaBackup/medical/website/app_models/kidney_model.pkl', 'rb') as f:
            kidney_model = pickle.load(f)
        pred = kidney_model.predict(np.array(to_predict_list).reshape(-1, len(to_predict_list)))
    elif len(to_predict_list) == 10:
        page = 'liver'
        with open('/home/cpatwadityasharma/AdityaBackup/medical/website/app_models/liver_model.pkl', 'rb') as f:
            liver_model = pickle.load(f)
        pred = liver_model.predict(np.array(to_predict_list).reshape(-1, len(to_predict_list)))
    elif len(to_predict_list) == 11:
        page = 'heart'
        with open('/home/cpatwadityasharma/AdityaBackup/medical/website/app_models/heart_model.pkl', 'rb') as f:
            heart_model = pickle.load(f)
        pred = heart_model.predict(np.array(to_predict_list).reshape(-1, len(to_predict_list)))
    elif len(to_predict_list) == 9:
        page = 'stroke'
        with open('//home/cpatwadityasharma/AdityaBackup/medical/website/app_models/avc_scaler.pkl', 'rb') as f:
            stroke_scaler = pickle.load(f)
        l1 = np.array(to_predict_list[2:]).reshape((-1, len(to_predict_list[2:]))).tolist()[0]
        l2 = stroke_scaler.transform(np.array(to_predict_list[0:2]).reshape((-1, 2))).tolist()[0]
        l = l2 + l1
        with open('/home/cpatwadityasharma/AdityaBackup/medical/website/app_models/avc_model.pkl', 'rb') as f:
            stroke_model = pickle.load(f)
        pred = stroke_model.predict(np.array(l).reshape(-1, len(l)))
    elif len(to_predict_list) == 8:
        page = 'diabete'
        with open('/home/cpatwadityasharma/AdityaBackup/medical/website/app_models/diabete_model.pkl', 'rb') as f:
            diabete_model = pickle.load(f)
        pred = diabete_model.predict(np.array(to_predict_list).reshape((-1, 8)))
        print(pred[0], page)
    return pred[0], page