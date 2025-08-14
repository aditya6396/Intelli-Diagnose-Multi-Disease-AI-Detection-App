from flask import Blueprint, render_template, request, send_from_directory
from .app_functions import ValuePredictor, pred_skin,pred_dr,pred_malaria,pred_oral,pred_oct,pred_pneumonia,pred_ocular
import os
from werkzeug.utils import secure_filename

prediction = Blueprint('prediction', __name__)

UPLOAD_FOLDER = 'uploads'
STATIC_FOLDER = 'static'

dir_path = os.path.dirname(os.path.realpath(__file__))



@prediction.route('/predict', methods=["POST", 'GET'])
def predict():

    if request.method == "POST":
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        result, page = ValuePredictor(to_predict_list)
        return render_template("result.html", prediction=result, page=page)
    else:
        return render_template('base.html')
    
    

@prediction.route('/upload', methods=['POST','GET'])
def upload_file():
    if request.method=="GET":
        return render_template('pneumonia.html', title='Pneumonia Disease')
    else:
        file = request.files["file"]
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(basepath,'uploads',  secure_filename(file.filename))
        file.save(file_path)
        indices = {0: 'Normal', 1: 'Pneumonia'}
        result =pred_pneumonia(file_path)

        
        # Convert result to float
        result_float = float(result)

        if result_float > 0.5:
            label = indices[1]
            accuracy = result_float * 100
        else:
            label = indices[0]
            accuracy = 100 - result_float


       
        return render_template('deep_pred.html', image_file_name=file.filename, label = label, accuracy = accuracy)

 



@prediction.route('/upload_maralia', methods=['POST','GET'])
def upload_maralia():
    if request.method=="GET":
        return render_template('maralia.html', title='Maralia Disease')
    else:
        file = request.files["file"]
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(basepath,'uploads',  secure_filename(file.filename))
        file.save(file_path)
        indices = {0:'Normal', 1:'Maralia'}
        result = pred_malaria(file_path)

        if result>0.5:
            label = indices[1]
            accuracy = result * 100
        else:
            label = indices[0]
            accuracy = 100 - result
        return render_template('deep_pred2.html', image_file_name=file.filename, label = label, accuracy = accuracy)


@prediction.route('/upload_skin', methods=['POST','GET'])
def upload_skin():
    if request.method=="GET":
        return render_template('skin.html', title='Skin Cancer')
    else:
        file = request.files["file"]
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(basepath,'uploads',  secure_filename(file.filename))
        file.save(file_path)
        indices = {0: 'Begin', 1: 'Melanoma'}
        result =pred_skin(file_path)

        if result>0.5:
            label = indices[1]
            accuracy = result * 100
        else:
            label = indices[0]
            accuracy = 100 - result
        return render_template('deep_pred3.html',image_file_name=file.filename, label = label, accuracy = accuracy)



@prediction.route('/upload_oclur', methods=['POST', 'GET'])
def upload_oclur():
    if request.method == "GET":
        return render_template('oclur.html', title='Oclur Disease')
    else:
        file = request.files["file"]
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(basepath, 'uploads', secure_filename(file.filename))
        file.save(file_path)

        # Get the prediction using the pred function
        predicted_label =pred_ocular(file_path)

        # Display the result in your template
        return render_template('deep_pred4.html', image_file_name=file.filename, label=predicted_label)
    

@prediction.route('/upload_dr', methods=['POST', 'GET'])
def upload_DR():
    if request.method == "GET":
        return render_template('dr.html', title='Diabetic Retinopathy')
    else:
        if 'file' not in request.files:
            return 'No file part'
        file = request.files["file"]
        if file.filename == '':
            return 'No selected file'
        if file:
            # Save the uploaded image
            basepath = os.path.dirname(__file__)
            file_path = os.path.join(basepath, 'uploads', secure_filename(file.filename))
            file.save(file_path)

            # Call predict function and get the result
            result = predict(file_path)

            # Display the result in your template
            return render_template('deep_pred5.html', image_file_name=file.filename, label=result)

        
# def upload_DR():
   
#     if request.method == "GET":
#         return render_template('dr.html', title='Dibetic Rectnography')
#     else:
#         if 'file' not in request.files:
#             return 'No file part'
#         file = request.files["file"]
#         if file.filename == '':
#             return 'No selected file'
#         if file:
#             # Save the uploaded image
#             basepath = os.path.dirname(__file__)
#             file_path = os.path.join(basepath, 'uploads', secure_filename(file.filename))
#             file.save(file_path)

#             # Call predict function and get the result
#             result = predict(file_path)

#             # Display the result in your template
#             return render_template('deep_pred5.html', image_file_name=file.filename, label=result)  
    


    
@prediction.route('/upload_octa', methods=['POST', 'GET'])
def upload_octa():
    if request.method == "GET":
        return render_template('oct.html', title='optical coherence tomography')
    else:
        file = request.files["file"]
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(basepath, 'uploads', secure_filename(file.filename))
        file.save(file_path)

        # Get the prediction using the pred function
        predicted_label = pred_oct(file_path)

        # Display the result in your template
        return render_template('deep_pred6.html', image_file_name=file.filename, label=predicted_label)   
    

@prediction.route('/upload_oral', methods=['POST', 'GET'])
def upload_oral():
    if request.method == "GET":
        return render_template('r.html', title='Oral Cancer')
    else:
        file = request.files["file"]
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(basepath, 'uploads', secure_filename(file.filename))
        file.save(file_path)

        # Get the prediction using the pred function
        predicted_label =pred_oral(file_path)

        # Display the result in your template
        return render_template('deep_pred7.html', image_file_name=file.filename, label=predicted_label)
    
                    


@prediction.route('/uploads/<filename>')
def send_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)
 


           
          
      
    

 
    
