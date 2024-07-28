import numpy as np
import cv2
from google.colab.patches import cv2_imshow
from google.colab import files

def resize_image(img, new_height, new_width):
    # Get original image dimensions
    height, width = img.shape[:2]

    # Calculate scale factors for resizing
    scale_x = new_width / width
    scale_y = new_height / height

    # Initialize resized image
    resized_img = np.zeros((new_height, new_width, 3), dtype=np.uint8)

    # Perform bilinear interpolation
    for i in range(new_height):
        for j in range(new_width):
            # Calculate corresponding coordinates in original image
            x = j / scale_x
            y = i / scale_y

            # Find surrounding pixel coordinates in original image
            x0 = int(x)
            y0 = int(y)
            x1 = min(x0 + 1, width - 1)
            y1 = min(y0 + 1, height - 1)

            # Calculate interpolation weights
            dx = x - x0
            dy = y - y0

            # Perform bilinear interpolation for each channel
            for k in range(3):  # Iterate over RGB channels
                # Bilinear interpolation formula
                interpolated_value = (1 - dx) * (1 - dy) * img[y0, x0, k] + \
                                     dx * (1 - dy) * img[y0, x1, k] + \
                                     (1 - dx) * dy * img[y1, x0, k] + \
                                     dx * dy * img[y1, x1, k]

                # Assign interpolated value to resized image
                resized_img[i, j, k] = int(interpolated_value)

    return resized_img


# Upload image
uploaded = files.upload()

# Get the uploaded image file name
for fn in uploaded.keys():
  image_path = fn

# Load the uploaded image
input_image = cv2.imread(image_path)

# Check if image loaded successfully
if input_image is None:
    print(f"Error: Could not load image. Please ensure the uploaded file is a valid image.")
else:
    # Define new dimensions for resizing
    new_height = 600
    new_width = 800

    # Resize the image using bilinear interpolation
    resized_image = resize_image(input_image, new_height, new_width)

    # Display the original and resized images
    cv2_imshow(resized_image)
