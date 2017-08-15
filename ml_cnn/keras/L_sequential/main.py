import cv2
import numpy as np
from keras.preprocessing import image as image_utils

from imagenet_utils import decode_predictions
from imagenet_utils import preprocess_input
from vgg16 import VGG16

# 命令行添加参数 image， 指定需要解析的图片
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True, help="path to the input image")
# args = vars(ap.parse_args())
args = {'image': '/Users/elbert/Downloads/bixiong.jpg'}
orig = cv2.imread(args["image"])

# load the input image using the Keras helper utility while ensuring
# that the image is resized to 224x224 pxiels, the required input
# dimensions for the network -- then convert the PIL image to a
# NumPy array
print("[INFO] loading and preprocessing image...")
image = image_utils.load_img(args["image"], target_size=(224, 224))
image = image_utils.img_to_array(image)

# our image is now represented by a NumPy array of shape (3, 224, 224),
# but we need to expand the dimensions to be (1, 3, 224, 224) so we can
# pass it through the network -- we'll also preprocess the image by
# subtracting the mean RGB pixel intensity from the ImageNet dataset
print(image.shape)
image = np.expand_dims(image, axis=0)
print(image.shape)
image = preprocess_input(image)
print(image.shape)

# load the VGG16 network
print("[INFO] loading network...")
model = VGG16(weights="imagenet")

# classify the image
print("[INFO] classifying image...")
preds = model.predict(image)
result = decode_predictions(preds)

print(result)
(id, label, p) = result[0][0]
# display the predictions to our screen
print("ImageNet Label: {}".format(label))
cv2.putText(orig, "Label: {}".format(label), (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
cv2.imshow("Classification", orig)
cv2.waitKey(0)
