from PIL import Image
import os

# Specify the input and output folder paths
input_folder = '/home/aditya/medical_demo/website/static/images/newmodel_img'  # Replace with the path to your input folder
output_folder = '/home/aditya/medical_demo/website/static/images/model_img'  # Replace with the path to your output folder

# Ensure the output folder exists, or create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Specify the target width and height for the resized images
target_width = 728  # Replace with your desired width
target_height = 455  # Replace with your desired height

# Loop through all files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):  # Add more file extensions if needed
        # Open the image
        image_path = os.path.join(input_folder, filename)
        img = Image.open(image_path)

        # Resize the image
        img = img.resize((target_width, target_height))

        # Save the resized image to the output folder
        output_path = os.path.join(output_folder, filename)
        img.save(output_path)

        print(f'Resized: {filename}')

print('Image resizing complete.')
