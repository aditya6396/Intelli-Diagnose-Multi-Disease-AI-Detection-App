# Intelli-Diagnose-Multi-Disease-AI-Detection-App
## Overview
This is a Flask-based web application designed to predict multiple medical conditions using machine learning models. The application allows users to upload medical images for disease prediction (e.g., skin cancer, pneumonia, malaria, ocular diseases, diabetic retinopathy, optical coherence tomography, and oral cancer) and provides a contact form to collect user feedback, which is stored in an SQLite database. By leveraging artificial intelligence (AI), this application aims to assist doctors in preliminary diagnostics, potentially improving efficiency and accuracy in medical practice.

## Features
- **Disease Prediction**: Predicts diseases based on uploaded medical images using pre-trained deep learning models.
- **Supported Diseases**:
  - Skin Cancer
  - Pneumonia
  - Malaria
  - Ocular Diseases
  - Diabetic Retinopathy
  - Optical Coherence Tomography (OCT)
  - Oral Cancer
  - Pathology-based predictions (kidney, liver, heart, stroke, diabetes) using numerical input data
- **User Feedback**: A contact form where users can submit feedback, stored in an SQLite database.
- **Image Upload**: Securely handles image uploads for disease prediction.
- **Responsive UI**: Renders results and feedback forms using HTML templates.

## Project Structure
```plaintext
├── app_functions.py       # Contains prediction functions for various diseases
├── messages.py           # Handles user feedback and SQLite database operations
├── models.py             # Defines the SQLite database model for storing messages
├── prediction.py         # Flask routes for handling predictions and file uploads
├── app_models/           # Directory containing pre-trained machine learning models
├── static/               # Static files (CSS, JS, etc.)
├── templates/            # HTML templates for rendering pages
├── Uploads/              # Directory for storing uploaded images
└── README.md             # This file
```

## Installation

### Prerequisites
- Python 3.8+
- Flask
- TensorFlow/Keras
- NumPy
- OpenCV
- scikit-learn
- XGBoost
- SQLite (included with Python)

### Setup
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/medical-diagnosis-app.git
   cd medical-diagnosis-app
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   Example `requirements.txt`:
   ```plaintext
   flask
   tensorflow
   numpy
   opencv-python
   scikit-learn
   xgboost
   werkzeug
   ```

4. **Download Pre-trained Models**:
   - Place the pre-trained models (e.g., `skin_model.h5`, `cnn_model.h5`, etc.) in the `app_models/` directory.
   - Update the model paths in `app_functions.py` if necessary.

5. **Set Up SQLite Database**:
   - The application uses SQLite to store user feedback.
   - Initialize the database by running:
     ```python
     from your_app_file import db, create_app
     app = create_app()
     with app.app_context():
         db.create_all()
     ```

6. **Run the Application**:
   ```bash
   python your_app_file.py
   ```
   - Access the app at `http://127.0.0.1:5000`.

## Usage
1. **Home Page**: Navigate to the root URL (`/`) to access the main page.
2. **Disease Prediction**:
   - Go to specific routes (e.g., `/upload` for pneumonia, `/upload_maralia` for malaria, etc.).
   - Upload an image to receive a prediction with a label and confidence score.
3. **Feedback Form**:
   - Access the `/msg` route to submit feedback (name, email, message).
   - Feedback is stored in the SQLite database.
4. **View Results**:
   - Prediction results are displayed on dedicated result pages (e.g., `deep_pred.html`, `deep_pred2.html`, etc.).

## Routes
- **/msg**: Handles user feedback submission and storage.
- **/predict**: Processes numerical input for pathology-based predictions (kidney, liver, heart, stroke, diabetes).
- **/upload**: Predicts pneumonia from uploaded images.
- **/upload_maralia**: Predicts malaria from uploaded images.
- **/upload_skin**: Predicts skin cancer from uploaded images.
- **/upload_oclur**: Predicts ocular diseases from uploaded images.
- **/upload_dr**: Predicts diabetic retinopathy from uploaded images.
- **/upload_octa**: Predicts optical coherence tomography conditions from uploaded images.
- **/upload_oral**: Predicts oral cancer from uploaded images.

## Model Details
- **Skin Cancer**: Uses a CNN model (`skin_model.h5`) with 150x150 RGB images.
- **Pneumonia**: Uses a CNN model (`cnn_model.h5`) with 500x500 grayscale images.
- **Malaria**: Uses an InceptionV3 model (`InceptionV3.h5`) with 128x128 RGB images.
- **Ocular Diseases**: Uses a model (`ocualr.h5`) with 224x224 RGB images, predicting multiple conditions (e.g., cataract, glaucoma).
- **Diabetic Retinopathy**: Uses a VGG16 model (`vgg16.h5`) with 224x224 RGB images.
- **OCT**: Uses a model (`octa_model.h5`) with 150x150 RGB images.
- **Oral Cancer**: Uses a VGG19 model (`oral cancer-vggg19.h5`) with 224x224 RGB images.
- **Pathology Models**: Uses XGBoost models (`kidney_model.pkl`, `liver_model.pkl`, etc.) for numerical input predictions.

## Solution (How It Helps Doctors)
This medical diagnosis web application serves as a proof-of-concept for integrating AI into medical diagnostics. By providing preliminary predictions for multiple diseases based on medical images and numerical data, it offers the following benefits to doctors:

- **Efficient Preliminary Screening**: The application can quickly analyze medical images (e.g., X-rays, retinal scans) to provide initial assessments, allowing doctors to prioritize cases that require urgent attention.
- **Decision Support**: AI-driven predictions can act as a second opinion, helping doctors confirm their diagnoses or identify potential conditions they might have overlooked.
- **Time Savings**: Automating initial analysis reduces the time spent on routine diagnostic tasks, enabling doctors to focus on complex cases and patient care.
- **Accessibility**: The web-based interface allows doctors in remote or underserved areas to access advanced diagnostic tools without specialized equipment.
- **Feedback Integration**: The feedback form enables doctors to provide insights on the tool’s performance, fostering continuous improvement of the AI models.

## Future Potential of AI in Medical Diagnostics
The integration of AI, as demonstrated by this application, has significant potential to transform healthcare in the future:

- **Enhanced Accuracy**: As AI models are trained on larger and more diverse datasets, their diagnostic accuracy will improve, potentially surpassing human performance in specific tasks like image-based diagnosis.
- **Personalized Medicine**: AI can analyze patient data to provide tailored treatment recommendations, improving outcomes for chronic conditions like diabetic retinopathy or heart disease.
- **Real-Time Monitoring**: Future iterations could incorporate real-time analysis of medical imaging or wearable device data, enabling continuous monitoring of patient health.
- **Scalability**: AI tools can be deployed globally, making high-quality diagnostics accessible in low-resource settings, thus reducing healthcare disparities.
- **Continuous Learning**: By incorporating user feedback (stored in the SQLite database), the system can be refined over time, adapting to new medical knowledge and improving prediction reliability.
- **Integration with EHRs**: AI systems could integrate with Electronic Health Records (EHRs) to provide holistic patient insights, combining imaging, lab results, and medical history for comprehensive diagnostics.

By serving as a decision-support tool, this application lays the groundwork for AI-driven healthcare solutions that can augment doctors’ expertise, streamline workflows, and improve patient outcomes.

## Notes
- **Model Paths**: Update the hardcoded model paths in `app_functions.py` to match your environment.
- **File Uploads**: Images are saved in the `Uploads/` directory. Ensure this directory exists and is writable.
- **Security**: The application uses `secure_filename` from Werkzeug to prevent malicious file uploads.
- **Database**: The SQLite database stores feedback with fields for `id`, `date`, `name`, `email`, and `messages`.

## Contributing
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -m "Add feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## Disclaimer
This application is for educational and research purposes only. It is not intended for clinical use or medical diagnosis. Always consult a healthcare professional for accurate medical advice.
