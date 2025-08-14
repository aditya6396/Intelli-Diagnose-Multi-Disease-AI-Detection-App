from tensorflow.keras.models import load_model
import mlflow
import mlflow.tensorflow

# Load your trained model
model = load_model('/home/cpatwadityasharma/AdityaBackup/medical/website/app_models/pneumonia_model.h5')





# Start an MLflow run
with mlflow.start_run():
    # Log parameters (you can customize this with your model's hyperparameters)
    mlflow.log_param("epochs", num_epochs)  # Example
    mlflow.log_param("batch_size", batch_size)  # Example

    # If you have metrics (accuracy, loss, etc.)
    mlflow.log_metric("train_loss", train_loss)  # Example
    mlflow.log_metric("val_accuracy", val_accuracy)  # Example

    # Log the model
    mlflow.tensorflow.log_model(tf_model=model, artifact_path="models")

    # Optionally log additional artifacts like model summary, confusion matrix, etc.
    with open("model_summary.txt", "w") as f:
        model.summary(print_fn=lambda x: f.write(x + '\n'))
    mlflow.log_artifact("model_summary.txt")

