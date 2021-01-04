# from imageai.Detection import ObjectDetection
# import os
#
# execution_path = os.getcwd()
#
# detector = ObjectDetection()
# detector.setModelTypeAsRetinaNet()
# detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5"))
# detector.loadModel()
# detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , "image.jpg"), output_image_path=os.path.join(execution_path , "imagenew.jpg"))
#
# for eachObject in detections:
#     print(eachObject["name"] , " : " , eachObject["percentage_probability"] )
from imageai.Detection import ObjectDetection
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

detector = ObjectDetection()

model_path = "./models/yolo-tiny.h5"
input_path = "./input/test.png"
output_path = "./output/newimage.jpg"

detector.setModelTypeAsTinyYOLOv3()
detector.setModelPath(model_path)
detector.loadModel()
detection = detector.detectObjectsFromImage(input_image=input_path, output_image_path=output_path)

for eachItem in detection:
    print(eachItem["name"] , " : ", eachItem["percentage_probability"])
