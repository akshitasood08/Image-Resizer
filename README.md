# Image Resizing using Bilinear Interpolation
This project contains a Python script designed to resize images using bilinear interpolation. The script is intended for use in Google Colab and includes functionality to upload an image, resize it to specified dimensions, and display the resized image.
***

## Image Interpolation
Image interpolation refers to the resizing of a digital image. Interpolation is the problem of approximating the value of a function for a non-given point in some space when given the value of that function in points around (neighboring) that point. 

Image interpolation have three main techniques:
### 1. Nearest Neighbor Interpolation
Nearest-neighbor interpolation (also known as proximal interpolation or, in some contexts, point sampling) is a simple method of multivariate interpolation in one or more dimensions. The nearest neighbor algorithm selects the value of the nearest point and does not consider the values of neighboring points at all, yielding a piecewise-constant interpolant. The algorithm is very simple to implement and is commonly used (usually along with mipmapping) in real-time 3D rendering to select color values for a textured surface ([Wikipedia](https://en.wikipedia.org/wiki/Nearest-neighbor_interpolation#:~:text=Nearest%2Dneighbor%20interpolation%20(also%20known,in%20one%20or%20more%20dimensions.))).

!["Nearest Neighbor Interpolation"](https://github.com/akshitasood08/Image-Resizer/blob/main/Nearest_Neighbor.png?raw=true)

### 2. Bilinear Interpolation
Bilinear interpolation is performed using linear interpolation first in one direction, and then again in the other direction. Bilinear interpolation uses values of only the 4 nearest pixels, located in diagonal directions from a given pixel, in order to find the appropriate color intensity values of that pixel ([Wikipedia](https://en.wikipedia.org/wiki/Bilinear_interpolation)).

!["Bilinear Interpolation"](https://github.com/akshitasood08/Image-Resizer/blob/main/Bilinear_interpolation.png?raw=true)

### 3. Bicubic Interpolation 
In image processing, bicubic interpolation is often chosen over bilinear or nearest-neighbor interpolation in image resampling, when speed is not an issue. In contrast to bilinear interpolation, which only takes 4 pixels (2×2) into account, bicubic interpolation considers 16 pixels (4×4)([Wikipedia](https://en.wikipedia.org/wiki/Bicubic_interpolation#:~:text=In%20mathematics%2C%20bicubic%20interpolation%20is,interpolation%20or%20nearest%2Dneighbor%20interpolation.))

***
## How to use ?
- Clone project
```
$ git clone https://github.com/akshitasood08/Image-Resizer.git
$ pip3 install -r requirements.txt
$ python3 main.py
```
- Open the script in Google Colab.
- Run the script and upload an image when prompted.
- The script will resize the image and display the resized image.
